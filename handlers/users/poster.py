from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from data.config import admins, channels
from keyboards.inline.confirm_key import confirm_key, post_callback
from loader import dp, bot
from states.poster import NewPost


@dp.message_handler(Command("create_post"))
async def create_post(m: types.Message):
    await m.answer("Отправте мне текст на публикацию")
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(m: types.Message, state: FSMContext):
    await state.update_data(text=m.html_text, mention=m.from_user.get_mention())
    await m.answer("Вы уверены, что хотите отпарвить это?",
                   reply_markup=confirm_key)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Вы отпрали пост на проверку")

    await bot.send_message(chat_id=admins[0], text=f"Пользователь {mention} хочет сделать пост:")
    await bot.send_message(chat_id=admins[0], text=text, parse_mode="HTML", reply_markup=confirm_key)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery,    state: FSMContext):
    await state.finish()
    await call.edit_reply_markup()
    await call.message.answer("Вы отклонили пост")


@dp.message_handler(state=NewPost.Confirm)
async def _post_unknown(m: types.Message):
    await m.answer("Сделайте выбор")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=admins)
async def approve_newpost(call: CallbackQuery):
    await call.answer("Вы одобрили этот пост", show_alert=True)
    target_channel = channels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=admins)
async def decline_post(call: CallbackQuery):
    await call.answer("Вы отклонили этот пост", show_alert=True)
    await call.message.edit_reply_markup()
