from aiogram import Router, F
from keybords.inline import xz_kb, bob_kb, good_kb, bb_kb
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext


callback_router = Router()


@callback_router.callback_query(F.data == "show_help")
async def show_help_text(callback: CallbackQuery):
    await callback.message.answer(text="Если нужна помощь обращайтесь @sh1r0_grio")


@callback_router.callback_query(F.data == 'keep')
async def start_text(callback: CallbackQuery):
    await callback.answer("")
    text = "<b> Я твой бот, я могу помочь найти твою любимую или музыку по настроению:</b>\n"

    media = InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=text, parse_mode="HTML")
    await callback.message.edit_media(media=media, reply_markup=xz_kb)


@callback_router.callback_query(F.data == "mood")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bob_kb)


@callback_router.callback_query(F.data == "home")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Я твой бот, я могу помочь найти твою любимую или музыку по настроению:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=good_kb)


@callback_router.callback_query(F.data == "back")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Я твой бот, я могу помочь найти твою любимую или музыку по настроению:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=xz_kb)


@callback_router.callback_query(F.data == "artist")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bob_kb)


@callback_router.callback_query(F.data == "years")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bob_kb)


@callback_router.callback_query(F.data == "genre")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bob_kb)


@callback_router.callback_query(F.data == "")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bob_kb)


@callback_router.callback_query(F.data == "sev")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bb_kb)


@callback_router.callback_query(F.data == "eig")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bb_kb)


@callback_router.callback_query(F.data == "nine")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bb_kb)


@callback_router.callback_query(F.data == "ten")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bb_kb)


@callback_router.callback_query(F.data == "new")
async def home(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.clear()
    home_text = "<b> Ты можешь выбрать что тебе угодно:</b>\n"

    media_start= InputMediaPhoto(media="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption=home_text, parse_mode="HTML")
    await callback.message.edit_media(media=media_start, reply_markup=bb_kb)



@callback_router.callback_query(F.data == "rep")
async def help_text(callback: CallbackQuery):
    await callback.message.answer(text="Эта ссылка на ваш жанр:\nhttps://zvuk.com/search?query=%D1%80%D0%B5%D0%BF")


@callback_router.callback_query(F.data == "rok")
async def help_text(callback: CallbackQuery):
    await callback.message.answer(text="Эта ссылка на ваш жанр:\nhttps://zvuk.com/search?query=%D1%80%D0%BE%D0%BA")


@callback_router.callback_query(F.data == "xip")
async def help_text(callback: CallbackQuery):
    await callback.message.answer(text="Эта ссылка на ваш жанр:\nhttps://zvuk.com/search?query=%D1%85%D0%B8%D0%BF%20%D1%85%D0%BE%D0%BF")


@callback_router.callback_query(F.data == "djaz")
async def help_text(callback: CallbackQuery):
    await callback.message.answer(text="Эта ссылка на ваш жанр:\nhttps://zvuk.com/search?query=%D0%B4%D0%B6%D0%B0%D0%B7")
