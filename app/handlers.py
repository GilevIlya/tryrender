from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
import app.keyboards as kb
from app.register import router2 as router2

router = Router()
router.include_router(router2)

@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer('Hello', reply_markup = kb.call_back_keyboard)

@router.callback_query(F.data == 'catalog')
async def callback_catalog(callback: CallbackQuery):
    await callback.answer('Catalog')
    await callback.message.edit_text('Choose', reply_markup=kb.call2_back_keyboard)