from os import getenv

from aiogram import F, types
from aiogram.enums import ContentType
from aiogram.filters import CommandStart

from bot.keyboards import keyboard
from main import bot, dp

PAYMENT_API_TOKEN = getenv("PAYMENT_API_TOKEN")


@dp.message(CommandStart())
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Тестируем WebApp!',
                           reply_markup=keyboard)

PRICE = {
    '1': [types.LabeledPrice(label='NEU X 200W', amount=10000)],
    '2': [types.LabeledPrice(label='Lama 2 150W', amount=5800000)],
    '3': [types.LabeledPrice(label='Light Pro 300W', amount=1400000)],
    '4': [types.LabeledPrice(label='NEU Z 100W', amount=12000000)],
    '5': [types.LabeledPrice(label='Edison 100W', amount=12700000)],
    '6': [types.LabeledPrice(label='Tesla Model S 400W', amount=50000000)]
}


@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def buy_process(web_app_message):
    print('web_app_message', web_app_message)

    await bot.send_invoice(web_app_message.chat.id,
                           title='Magic lamp',
                           description='Online shop kgrow payment',
                           provider_token=PAYMENT_API_TOKEN,
                           currency='rub',
                           need_email=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')


@dp.pre_checkout_query(lambda query: True)
async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message(F.successful_payment)
async def successful_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Платеж прошел успешно!')
