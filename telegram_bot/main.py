from aiogram import types, executor
from aiogram.types.base import MetaTelegramObject

from config import bot, dp

import logging
import os

@dp.message_handler(commands=["start", "help"])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f"Your Telegram ID is {message.from_user.id}\n")


@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo = photo, caption="Мемчик")

@dp.message_handler()
async def echo_handler(message: types.Message):
    text = message.text
    if text.isdigit():
        text_to_number = int(text) * 2
        await message.answer(text = str(text_to_number))
    else:
        await message.answer(text=text)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)