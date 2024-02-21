from os import getenv

from aiogram import types
from aiogram.types import WebAppInfo

WEB_VIEW_URL = getenv('WEB_VIEW_URL')
web_app = WebAppInfo(url=WEB_VIEW_URL)
print(WEB_VIEW_URL)

# keyboard = types.InlineKeyboardMarkup(
#     inline_keyboard=[
#         [types.InlineKeyboardButton(text='Open site', web_app=web_app)]
#     ],
# )

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='See our products', web_app=web_app)]
    ],
    resize_keyboard=True
)
