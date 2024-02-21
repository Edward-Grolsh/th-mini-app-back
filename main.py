import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.keyboards import keyboard

BOT_API_TOKEN = getenv("BOT_API_TOKEN")

dp = Dispatcher()

bot = Bot(BOT_API_TOKEN, parse_mode=ParseMode.HTML)


# @dp.message(CommandStart())
# async def start(message: types.Message):
#     await bot.send_message(message.chat.id, 'Тестируем WebApp!',
#                                reply_markup=keyboard)


async def main() -> None:
    from bot.handlers import dp
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
