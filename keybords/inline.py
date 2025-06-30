from xml.dom.expatbuilder import TEXT_NODE

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
about_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Github", url="github.com"),
        InlineKeyboardButton(text="Zvuk", url="https://zvuk.com/?utm_referrer=https%3A%2F%2Fzvuk.com%2F%3Futm_referrer%3Dhttps%253a%252f%252fwww.google.com%252f")],
        [InlineKeyboardButton(text="Помощь", callback_data="show_help")]

    ]

)

buttons_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Реп", callback_data="rep"),
         InlineKeyboardButton(text="R&B", callback_data="R&B")],
        [InlineKeyboardButton(text="️⬅", callback_data="prev"),
         InlineKeyboardButton(text="➡", callback_data="next")]

    ]
)
buttons_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Хип-Хоп", callback_data="Хип-Хоп"),
         InlineKeyboardButton(text="", callback_data="")],
        [InlineKeyboardButton(text="️⬅", callback_data="prev"),
         InlineKeyboardButton(text="➡", callback_data="next")]

    ]
)

kod_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="80", callback_data="50"),
         InlineKeyboardButton(text="90", callback_data="60")],
        [InlineKeyboardButton(text="️⬅", callback_data="prev"),
         InlineKeyboardButton(text="➡", callback_data="next")]
    ]
)

kod_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="80", callback_data="60"),
         InlineKeyboardButton(text="90", callback_data="70")],
        [InlineKeyboardButton(text="️⬅", callback_data="prev"),
         InlineKeyboardButton(text="➡", callback_data="next")]
    ]
)


