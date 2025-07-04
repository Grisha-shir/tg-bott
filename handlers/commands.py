from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.filters import Command

from keybords.inline import good_kb, top_kb, bb_kb, cop_kb
from keybords.reply import menu_kb
from aiogram.types import InputProfilePhoto
from database import sqlite3, add_user

from keybords.states import Music

command_router = Router()


@command_router.message(Command("information"))
async def information_handler(message: Message):
    information_text = (
        "Я могу помочь найти тебе новую музыку или твоего любимого артиста, на твой вкус, нажми /Form.\n"
        ""
        )
    await message.answer(text=information_text, parse_mode="HTML")


@command_router.message(Command("help"))
async def help_handler(message: Message):
    help_text = (
        "Эти команды могут помочь вам:\n"
        "/start - запустить бота.\n"
        "/help - список команд.\n"
        "/information - информация о боте.\n"
        "/about - ссылки на сайт.\n"
        "/poll - отзыв о боте.\n"
        "/tell - топ 100 всех жанров.\n"
        "/best - любимые артисты автора.\n"
        )
    await message.answer(text=help_text)


@command_router.message(Command("start"))
async def about_info(message: Message):
    start_message = " Привет! Я твой бот помощник, я могу найти тебе новую музыку или твоего любимого артиста, нажми /help чтобы увидеть список команд\n"
    await message.answer_photo(photo="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg", caption
    =start_message, reply_markup=good_kb)


@command_router.message(Command("tell"))
async def about_info(message: Message):
    start_message = "⬇️Это Топ 100 всех жанров музыки:⬇️\n"
    await message.answer_photo(photo="https://www.billboard.com/wp-content/uploads/media/Lil-Tecca-press-by-Orlando-IV-2019-billboard-1548.jpg?w=942&h=623&crop=1", caption
    =start_message, reply_markup=top_kb)


@command_router.message(Command("best"))
async def about_info(message: Message):
    start_message = "⬇️Это любимые аритисты автора:⬇️\n"
    await message.answer_photo(photo="https://hiphop4real.com/wp-content/uploads/2017/01/340.jpg", caption
    =start_message, reply_markup=cop_kb)


@command_router.message(Command("poll"))
async def send_poll_handler(message: Message):
    await message.answer_poll(
        question="Как тебе бот?",
        options=["Отлично","Хорошо","Плохо"],
        is_anonymous=False
    )


@command_router.message(Command("quiz"))
async def send_quiz_handler(message: Message):
    await message.answer_poll(
        question="Какой ваш любимый жанр музыки?",
        options=["Реп","Хип-Хоп","R&B","Рок","Поп","Джаз"],
        is_anonymous=False
    )

@command_router.message(Command("form"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("🎵Какой твой любимый жанр музыки?🎵")
    await state.set_state(Music.genre)


@command_router.message(Music.genre)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(Music.years)
    await message.answer(text="🎶Какие года вы хотите послушать в этом жанре?🎶")


@command_router.message(Music.years, F.text.isdigit())
async def process_years(message: Message, state: FSMContext):
    await state.update_data(years=message.text)
    await state.set_state(Music.love_music)
    data = await state.get_data()
    await message.answer(text=f"🎼Как часто вы слушаете музыку жанра {data['genre']}, {data['years']} годов?🎼")


@command_router.message(Music.love_music)
async def process_love_music(message: Message, state: FSMContext):
    await state.update_data(love_music=message.text)
    await state.set_state(Music.artist)
    data = await state.get_data()
    await message.answer(text=f"🎤Какой ваш любимый исполнитель {data['genre']}, {data['years']} годов?🎤")


@command_router.message(Music.artist)
async def process_artist(message: Message, state: FSMContext):
    await state.update_data(artist=message.text)
    data = await state.get_data()
    await message.answer(text=f"✅Хороший выбор, сейчас подберем для вас что нибудь...✅")
    id = message.from_user.id
    add_user(user_id=id,genre=data["genre"], years=data["years"], love_music=data["love_music"], artist=data["artist"])
    await state.clear()



