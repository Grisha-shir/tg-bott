from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


good_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎶Найти музыку🎶", callback_data="keep")],
        [InlineKeyboardButton(text="🆘Помощь🆘", callback_data="show_help")]

]
)


daun_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙В главное меню🔙", callback_data="home")]

]
)


xz_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="По жанру", callback_data="genre")],
        [InlineKeyboardButton(text="🔙В главное меню🔙", callback_data="home")]

]
)



bob_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="70-е годы", callback_data="sev"),
     InlineKeyboardButton(text="80-е годы", callback_data="eig")],
    [InlineKeyboardButton(text="90-е годы", callback_data="nine"),
     InlineKeyboardButton(text="00-е годы", callback_data="ten")],
    [InlineKeyboardButton(text="Новая музыка", callback_data="new")],
    [InlineKeyboardButton(text="🔙Назад🔙", callback_data="back")],
    [InlineKeyboardButton(text="🔙В главное меню🔙", callback_data="home")]

]
)


bb_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="Реп", callback_data="rep"),
     InlineKeyboardButton(text="Рок", callback_data="rok")],
    [InlineKeyboardButton(text="Хип-Хоп", callback_data="xip"),
     InlineKeyboardButton(text="Джаз", callback_data="djaz")],
    [InlineKeyboardButton(text="🔙Назад🔙", callback_data="back")],
    [InlineKeyboardButton(text="🔙В главное меню🔙", callback_data="home")]

]
)


top_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Топ 100 Реп", url="https://zvuk.com/playlist/1062105"),
         InlineKeyboardButton(text="Топ 100 Поп", url="https://zvuk.com/playlist/8404354")],
        [InlineKeyboardButton(text="Топ 100 Джаз", url="https://zvuk.com/release/19604516"),
         InlineKeyboardButton(text="Топ 100 Хип-Хоп", url="https://zvuk.com/playlist/8127767")],
        [InlineKeyboardButton(text="Топ 100 Всех жанров", url="https://zvuk.com/playlist/5460882")],

]
)


cop_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Weeknd", url="https://zvuk.com/artist/873552"),
         InlineKeyboardButton(text="PlayBoi Carti", url="https://zvuk.com/artist/3471532")],
        [InlineKeyboardButton(text="Lil Uzi Vert", url="https://zvuk.com/artist/3331465"),
         InlineKeyboardButton(text="Lil Tecca", url="https://zvuk.com/artist/209550423")],
        [InlineKeyboardButton(text="Partynextdoor", url="https://zvuk.com/artist/1276994"),
         InlineKeyboardButton(text="Drake", url="https://zvuk.com/artist/680032")],
        [InlineKeyboardButton(text="Профиль автора", url="https://zvuk.com/profile/929907170")]

]
)




