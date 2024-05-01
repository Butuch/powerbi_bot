from dotenv import load_dotenv
import os

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
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
    await message.reply(text=LEXICON_COMMANDS_RU['/contact'])
    
    
@router.message(Command('support'))
async def process_support_command(message: Message):
    await message.reply(text=LEXICON_COMMANDS_RU['/support'])


@router.message(Command('info_about_user'))
async def process_info_command(message: Message):
    response_text = (
        f"Message from {message.from_user.first_name} (ID: {message.from_user.id})\n"
        f"Chat ID: {message.chat.id}"
    )
    await message.answer(response_text)


@router.message(Command('test'))
async def process_info_command(message: Message):
    response_text = '''
    <b>bold</b>\n
    <strong>bold</strong>\n
    <i>italic</i>\n
    <em>italic</em>\n
    <u>underline</u>\n
    <ins>underline</ins>\n
    <s>strikethrough</s>\n
    <strike>strikethrough</strike>\n
    <del>strikethrough</del>\n
    <span class="tg-spoiler">spoiler</span>
    '''
    await message.answer(response_text)