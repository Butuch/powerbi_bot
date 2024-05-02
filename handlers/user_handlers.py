from datetime import datetime
import sys
sys.path.append('.')

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import asyncio

from powerbi.powerbi_get_data import (
    report_sales,
    report_cash,
    report_cash_acc,
    report_cash_inc_by_counterparty,
    report_cash_out_by_counterparty,
    report_sales_top_counter,
    report_sales_top_goods,
    report_sales_top_managers
    )
from powerbi.powerbi_reports_description import reports_description as rd
from keyboards.inline_kb import (
    inline_reports_on_keyboard_sales,
    inline_reports_off_keyboard_sales,
    inline_reports_on_keyboard_cash,
    inline_reports_off_keyboard_cash,
    inline_refresh_keyboard_yes_no,
    inline_reports_cash_details,
    inline_reports_sales_details
    )
from keyboards.main_kb import reports_kb
from lexicon.lexicon import REPORTS_RU, LEXICON_COMMANDS_RU, OTHER_TEXT
from services.functions import text_by_rows, text_by_rows_simple

router = Router()
    

# sales report
@router.message(F.text == REPORTS_RU['sales']['name'])
async def sales_report(message: Message):
    report_name = REPORTS_RU['sales']['name'][1:]
    description = text_by_rows_simple(rd['sales'])
    
    if rd['sales']['<b>Рассылка</b>'] == OTHER_TEXT['notif_off']:
        var_reply_markup = inline_reports_on_keyboard_sales
    else:
        var_reply_markup = inline_reports_off_keyboard_sales
        
    await message.answer(
        text=f'<b>{report_name}</b>\n\n{description}',
        reply_markup=var_reply_markup
        )


@router.callback_query(F.data == REPORTS_RU['sales']['callbacks']['get_report'])
async def get_sales_report(callback: CallbackQuery):
    # splitting the dictionary line by line
    report_name = f"{REPORTS_RU['sales']['name']} на <b>{rd['sales']['<b>Обновлено</b>']}</b>"
    report = text_by_rows(report_sales)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'{report_name}\n\n{report}',
        reply_markup=inline_reports_sales_details
        )
    
# get report sales top 10 counter
@router.callback_query(F.data == REPORTS_RU['sales_top_counter']['callback'])
async def get_sales_top_counter_report(callback: CallbackQuery):
    report_name = REPORTS_RU['sales_top_counter']['name']
    report = text_by_rows(report_sales_top_counter)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'<b>{report_name}</b>\n\n{report}',
        reply_markup=inline_reports_sales_details
        )
# get report sales top 10 goods
@router.callback_query(F.data == REPORTS_RU['sales_top_goods']['callback'])
async def get_sales_top_goods_report(callback: CallbackQuery):
    report_name = REPORTS_RU['sales_top_goods']['name']
    report = text_by_rows(report_sales_top_goods)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'<b>{report_name}</b>\n\n{report}',
        reply_markup=inline_reports_sales_details
        )
# get report sales top 10 managers
@router.callback_query(F.data == REPORTS_RU['sales_top_managers']['callback'])
async def get_sales_top_managers_report(callback: CallbackQuery):
    report_name = REPORTS_RU['sales_top_managers']['name']
    report = text_by_rows(report_sales_top_managers)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'<b>{report_name}</b>\n\n{report}',
        reply_markup=inline_reports_sales_details
        )
    
    
@router.callback_query(F.data == REPORTS_RU['sales']['callbacks']['notif'])
async def sales_notif(callback: CallbackQuery):
    if rd['sales']['<b>Рассылка</b>'] == OTHER_TEXT['notif_off']:
        rd['sales']['<b>Рассылка</b>'] = OTHER_TEXT['notif_on']
        rd['sales']['<b>Время рассылки</b>'] = '07:30'
        var_reply_markup = inline_reports_off_keyboard_sales
    else:
        rd['sales']['<b>Рассылка</b>'] = OTHER_TEXT['notif_off']
        del rd['sales']['<b>Время рассылки</b>']
        var_reply_markup = inline_reports_on_keyboard_sales
        
    report_name = REPORTS_RU['sales']['name'][1:]
    description = '\n'.join([f'{key}: {value}' for key, value in rd['sales'].items()])
        
    await callback.message.edit_text(
            text=f'<strong>{report_name}</strong>\n\n{description}',
            reply_markup=var_reply_markup
        )
    await callback.answer(text='')

   
@router.callback_query(F.data == REPORTS_RU['sales']['text_notif']['change'])
async def sales_notif_change(callback: CallbackQuery):
    await callback.answer(text='Soon')


# cash report
@router.message(F.text == REPORTS_RU['cash']['name'])
async def cash_report(message: Message):
    report_name = REPORTS_RU['cash']['name'][1:]
    description = text_by_rows_simple(rd['cash'])
    
    if rd['cash']['<b>Рассылка</b>'] == OTHER_TEXT['notif_off']:
        var_reply_markup = inline_reports_on_keyboard_cash
    else:
        var_reply_markup = inline_reports_off_keyboard_cash
        
    await message.answer(
        text=f'<b>{report_name}</b>\n\n{description}',
        reply_markup=var_reply_markup
        )
    
    
# get report cash
@router.callback_query(F.data == REPORTS_RU['cash']['callbacks']['get_report'])
async def get_cash_report(callback: CallbackQuery):
    report_name = REPORTS_RU['cash']['name']
    report_name_2 = f"и движение денег за <b>{rd['cash']['<b>Обновлено</b>']}</b>"
    report = text_by_rows(report_cash)
    await callback.answer(text='')
    await callback.message.answer(
        text=f"{report_name}\n{report_name_2}\n\n{report}",
        reply_markup=inline_reports_cash_details
        )
# get report cash by accounts
@router.callback_query(F.data == REPORTS_RU['cash_acc']['callback'])
async def get_cash_acc_report(callback: CallbackQuery):
    report_name = f"{REPORTS_RU['cash_acc']['name']} на <b>{rd['cash']['<b>Обновлено</b>']}</b>"
    report = text_by_rows(report_cash_acc)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'{report_name}\n\n{report}',
        reply_markup=inline_reports_cash_details
        )
# get report cash inc by counterparty
@router.callback_query(F.data == REPORTS_RU['cash_inc_counter']['callback'])
async def get_cash_inc_report(callback: CallbackQuery):
    report_name = f"{REPORTS_RU['cash_inc_counter']['name']} за <b>{rd['cash']['<b>Обновлено</b>']}</b>"
    report = text_by_rows(report_cash_inc_by_counterparty)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'{report_name}\n\n{report}',
        reply_markup=inline_reports_cash_details
        )
# get report cash out by counterparty
@router.callback_query(F.data == REPORTS_RU['cash_out_counter']['callback'])
async def get_cash_out_report(callback: CallbackQuery):
    report_name = f"{REPORTS_RU['cash_out_counter']['name']} за <b>{rd['cash']['<b>Обновлено</b>']}</b>"
    report = text_by_rows(report_cash_out_by_counterparty)
    await callback.answer(text='')
    await callback.message.answer(
        text=f'{report_name}\n\n{report}',
        reply_markup=inline_reports_cash_details
        )

    
@router.callback_query(F.data == REPORTS_RU['cash']['callbacks']['notif'])
async def cash_notif(callback: CallbackQuery):
    if rd['cash']['<b>Рассылка</b>'] == OTHER_TEXT['notif_off']:
        rd['cash']['<b>Рассылка</b>'] = OTHER_TEXT['notif_on']
        rd['cash']['<b>Время рассылки</b>'] = '07:30'
        var_reply_markup = inline_reports_off_keyboard_cash
    else:
        rd['cash']['<b>Рассылка</b>'] = OTHER_TEXT['notif_off']
        del rd['cash']['<b>Время рассылки</b>']
        var_reply_markup = inline_reports_on_keyboard_cash
        
    report_name = REPORTS_RU['cash']['name'][1:]
    description = '\n'.join([f'{key}: {value}' for key, value in rd['cash'].items()])
        
    await callback.message.edit_text(
            text=f'<strong>{report_name}</strong>\n\n{description}',
            reply_markup=var_reply_markup
        )
    await callback.answer(text='')

   
@router.callback_query(F.data == REPORTS_RU['cash']['text_notif']['change'])
async def cash_notif_change(callback: CallbackQuery):
    await callback.answer(text='Soon')
    

# refresh DWH and reports
@router.message(F.text == REPORTS_RU['refresh']['name'])
async def refresh_reports(message: Message):
    await message.answer(
        text=OTHER_TEXT['sure'],
        reply_markup=inline_refresh_keyboard_yes_no
        )
    
    
@router.callback_query(F.data == OTHER_TEXT['yes']['callback'])
async def yes_refresh(callback: CallbackQuery):
    await callback.answer(text='')
    await asyncio.sleep(1)
    await callback.message.answer(text='Обновление отчетов запущено\nВы получите уведомление о завершении')
    await asyncio.sleep(2)
    
    for category, data in rd.items():
        if '<b>Обновлено</b>' in data:
            now = datetime.now()
            data['<b>Обновлено</b>'] = now.strftime("%d.%m.%Y %H:%M")
        
    await callback.message.answer(
        text='Отчеты обновлены',
        reply_markup=reports_kb
        )
    
    
# return to main menu
@router.callback_query(F.data.in_(['back',
                                   OTHER_TEXT['no']['callback']]))
async def go_to_reports_list(callback: CallbackQuery):
    await callback.answer(text='')
    await callback.message.answer(
        text=LEXICON_COMMANDS_RU['/start'],
        reply_markup=reports_kb
        )