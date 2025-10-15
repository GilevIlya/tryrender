from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import db

router2 = Router()

class Register(StatesGroup):
    name = State()
    age = State()

@router2.message(Command('register'))
async def register_func(message: Message, state: FSMContext):
    if await db.validation(message.from_user.id):
        await message.answer('Your account is in db already')
        return
    await message.answer('Enter your name')
    await state.set_state(Register.name)
    
@router2.message(Register.name)
async def set_name(message:Message, state:FSMContext):
    if not message.text or len(message.text.strip()) == 0:
        await message.answer('Name has to be str obj and len>0')
        return
    await state.update_data(name=message.text)
    await message.answer('Enter your age')
    await state.set_state(Register.age)

@router2.message(Register.age)
async def set_age(message: Message, state:FSMContext):
    if not message.text.isdigit():
        await message.answer('Enter int obj')
        return
    
    if not 18 <= int(message.text) <= 120:
        await message.answer('Age has to be from 18 to 120')
        return
    
    await state.update_data(age=message.text)
    data = await state.get_data()
    await db.reg_acc(message.from_user.id, data['name'], data['age'])
    await message.answer(f'Your data:\nname: {data['name']}\nage: {data['age']}')
    await state.clear()