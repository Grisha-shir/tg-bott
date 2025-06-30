from email.policy import default

from aiogram import Router, F
from aiogram.types import CallbackQuery
from pydantic.v1.class_validators import all_kwargs
from keybords.inline import buttons_kb1, buttons_kb2, kod_kb1, kod_kb2

callback_router = Router()

@callback_router.callback_query(F.data == "show_help")
async def show_help_text(callback: CallbackQuery):
    await callback.message.answer(text="Если нужна помощь обращайтесь @sh1r0_grio ")

@callback_router.callback_query(F.data.in_(['prev', 'next']))
async  def pagenatuon(callback: CallbackQuery):
    if F.data == "next":
        await callback.message.edit_text(text="text for page 2", reply_markup=buttons_kb1)
    elif F.data== "prev":
        await callback.message.edit_text(text="text for page 1", reply_markup=buttons_kb2)

@callback_router.callback_query(F.data == "rep")
async def rep_text(callback: CallbackQuery):
    await callback.message.answer(text="Если вы выбрали Реп нажмите /years")

@callback_router.callback_query(F.data == "R&B")
async def rnb_text(callback: CallbackQuery):
    await callback.message.answer(text="Если вы выбрали R&B нажмите /years")

@callback_router.callback_query(F.data.in_(['prev', 'next']))
async  def pagen(callback: CallbackQuery):
    if F.data == "next":
        await callback.message.edit_text(text="text for page 2", reply_markup=kod_kb1)
    elif F.data== "prev":
        await callback.message.edit_text(text="text for page 1", reply_markup=kod_kb2)


