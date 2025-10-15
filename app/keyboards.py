from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

async_pract_reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='AsyncPract')]
], resize_keyboard=True,
   input_field_placeholder='PractField')

names = ['Ilya', 'Ivan', 'John', 'Alex']

call_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Gmail', callback_data='email'),
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

call2_back_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Catalog', callback_data='a')],
    [InlineKeyboardButton(text='Email', callback_data = 'b'),
     InlineKeyboardButton(text='Contacts', callback_data='c')]
])

