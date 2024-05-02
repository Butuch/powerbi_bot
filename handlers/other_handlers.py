from dotenv import load_dotenv
import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_kb import reports_kb
from lexicon.lexicon import LEXICON_COMMANDS_RU

load_dotenv()

# Get list admins
ADMIN_IDS = os.getenv("ADMIN_IDS").split(',')

router = Router()


@router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS_RU['/start'],
                            reply_markup=reports_kb)


@router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_COMMANDS_RU['/help'])


@router.message(Command('contact'))
async def process_contact_command(message: Message):
    await message.reply_contact(
        phone_number='+491772250255',
        first_name='Viktor',
        last_name='Krylov'
        )


@router.message(Command('info_about_user'))
async def process_info_command(message: Message):
    response_text = (
        f"Message from {message.from_user.first_name} (ID: {message.from_user.id})\n"
        f"Chat ID: {message.chat.id}"
    )
    await message.answer(response_text)