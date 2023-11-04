from messages import diilers as msg_dills

from funcs.admins import AdminFilter
from keyboards.inline.dillers import kb_dillers

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


diller_routers = Router()


class NewDiller(StatesGroup):
    name = State()
    phone = State()
    address = State()


@diller_routers.callback_query(AdminFilter(), F.data == 'main_menu_dillers')
async def menu_dillers(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(msg_dills.title, reply_markup=kb_dillers)


@diller_routers.callback_query(AdminFilter(), F.data == 'dillers_new')
async def new_diller(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(f'{msg_dills.NewDiller.title}\n'
                                  f'{msg_dills.NewDiller.get_name}')
    await state.set_state(NewDiller.name)


@diller_routers.message(NewDiller.name)
async def new_diller_get_name(m: Message, state: FSMContext):
    name = m.text.strip()
    await state.update_data(name=name)
    await m.answer(msg_dills.NewDiller.get_phone)
    await state.set_state(NewDiller.phone)


@diller_routers.message(NewDiller.phone)
async def new_diller_get_phone(m: Message, state: FSMContext):
    phone = m.text.strip()
    await state.update_data(phone=phone)
    await m.answer(msg_dills.NewDiller.get_address)
    await state.set_state(NewDiller.address)


@diller_routers.message(NewDiller.address)
async def new_diller_get_address(m: Message, state: FSMContext):
    address = m.text.strip()
    await state.update_data(address=address)
    data = await state.get_data()
    await state.clear()
