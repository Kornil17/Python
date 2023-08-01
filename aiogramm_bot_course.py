from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType


API_TOKEN: str = '5947498423:AAE3ve6bCjFoYVBhk9lbnPa1fTTqy8Z6yCY'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


async def process_about_command(message: types.Message):
    await message.reply("Команда обо мне)")

# @dp.message_handler()
# async def echo_message(m: types.Message):
#     await m.reply(text=m.text)

# @dp.message_handler()
async def echo_message1(message: types.Message):
    a = 5 * 25
    await message.reply(str(a))

async def send_photo_echo(message: types.Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

dp.register_message_handler(process_start_command, commands=["start"])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(process_about_command, commands=['about'])
# dp.register_message_handler(echo_message, content_types=['text'])
dp.register_message_handler(send_photo_echo, content_types=['photo', 'document', 'animation'])
dp.register_message_handler(echo_message1, content_types=['text'])



if __name__ == '__main__':
    executor.start_polling(dp)
