from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.filters import Command
from aiohttp.web_routedef import options
from handlers.callback import callback_router
from keybords.inline import about_kb
from keybords.inline import buttons_kb1, kod_kb1
from keybords.reply import menu_kb
from aiogram.types import InputProfilePhoto


command_router = Router()

@command_router.message(Command(""))
async def start_handler(message: Message):
    start_text = (
        "Привет - это бот помощник!\n"
        "Нажми /help чтобы узнать список команд."
        )
    await message.answer(text=start_text)

@command_router.message(Command("information"))
async def information_handler(message: Message):
    information_text = (
        "Я могу помочь найти тебе новую музыку или твоего любимого артиста, на твой вкус.\n"
        ""
        )
    await message.answer(text=information_text, parse_mode="HTML")

@command_router.message(Command("help"))
async def help_handler(message: Message):
    help_text = (
        "Эти команды могут помочь вам.\n"
        ""
        "/start - запустить бота.\n"
        "/help - список команд.\n"
        "/information - информация о боте.\n"
        "/about - ссылки на сайт.\n"
        "/poll - отзыв о боте.\n"
        "/artist - артист которого вы хотите послушать.\n"
        "/genre - жанр музыки который вы хотите послушать.\n"
        "/quiz - опрос о вашем любимом жанре музыки."
        "/years - "
        )
    await message.answer(text=help_text)

@command_router.message(F.text == "hi")
async def say_hi(message: Message):
    await message.reply(text="Hi!\nHow are you?")

@command_router.message(F.photo)
async def react_to_photo(m: Message):
    text_to_photo = "Отличное фото."
    await m.reply(text=text_to_photo)
@command_router.message(Command("menu"))
async def show_menu(message: Message):
    about_message = "Ты вызвал команду /menu\nВыбери что хочешь сделать."
    await message.answer(text=about_message, reply_markup=menu_kb)

@command_router.message(Command("/help"))
async def semu_docs(message: Message):
    await message.reply(text="Some doc info:\n bla-bla-bla")

@command_router.message(F.text.lower().contains("привет"))
async def say_hi(message:Message):
    text_hi="Привет!\nЯ могу помочь тебе с выбором музыки\nЕсли хочешь найти новую музыку нажми /genre"
    await message.answer(text=text_hi)

@command_router.message(F.text.lower().contains("пока"))
async def say_hi(message:Message):
    text_hi="До свидания."
    await message.answer(text=text_hi)

@command_router.message(F.sticker)
async def react_to_message(message:Message):
    await message.answer(text="Классный стикер.")

@command_router.message(F.text.lower().contains("❤️"))
async def say_hi(message:Message):
    text_hi="Спасибо за сердечко."
    await message.answer(text=text_hi)

@command_router.message(Command("about"))
async def about_info(message: Message):
    about_message = "Ты вызвал команду /about\nПо этим ссылкам ты можешь узнать информацию которая тебе нужна."
    await message.answer(text=about_message, reply_markup=about_kb)

@command_router.message(Command("album"))
async def send_album(message: Message):
    media = [
        InputProfilePhoto(media=""),
        InputProfilePhoto(media=""),
        InputProfilePhoto(media=""),
    ]
    await message.answer_media_group(media)

@command_router.message(Command("start"))
async def send_photo(message: Message):
    await message.answer_photo(
        photo="https://www.billboard.com/wp-content/uploads/2025/03/playboi-carti-rolling-loud-california-2025-billboard-1548.jpg",
        caption="<b>Привет!</b> -- <strong>bold</strong>Привет!\nЯ твой бот помощник, я могу найтитебе новую музыку или твоего любимого артиста",
    )

@command_router.message(Command("poll"))
async def send_poll_handler(message: Message):
    await message.answer_poll(
        question="Как тебе бот?",
        options=["Отлично","Хорошо","Плохо"],
        is_anonymous=False
    )

@command_router.message(Command("genre"))
async def pages_command(message: Message):
    await message.answer("Страница 1", reply_markup=buttons_kb1)

@command_router.callback_query(F.data.in_(["prev", "next"]))
async def page_callback(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.edit_text("Страница 2", reply_markup=buttons_kb1)
    else:
        await callback.message.edit_text("Страница 1", reply_markup=buttons_kb1)
    await callback.answer()

@command_router.message(Command("years"))
async def pages_command(message: Message):
    await message.answer("Страница 1", reply_markup=kod_kb1)

@command_router.callback_query(F.data.in_(["prev", "next"]))
async def page_callback(callback: CallbackQuery):
    if callback.data == "next":
        await callback.message.edit_text("Страница 2", reply_markup=kod_kb1)
    else:
        await callback.message.edit_text("Страница 1", reply_markup=kod_kb1)
    await callback.answer()

@command_router.message(F.text.lower().contains("я хочу найти новую музыку"))
async def say_hi(message:Message):
    text_hi="Привет!\nЯ могу помочь тебе с выбором музыки.\nЕсли хочешь найти новую музыку нажми /genre"
    await message.answer(text=text_hi)

@command_router.message(Command("quiz"))
async def send_quiz_handler(message: Message):
    await message.answer_poll(
        question="Какой ваш любимый жанр музыки?",
        options=["Реп","Хип-Хоп","R&B"],
        is_anonymous=False
    )

@command_router.message()
async def echo_handler(message: Message):
    await message.answer(message.text)



