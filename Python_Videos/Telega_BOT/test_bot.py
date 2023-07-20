from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN: str = '5947498423:AAE3ve6bCjFoYVBhk9lbnPa1fTTqy8Z6yCY'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)



def main(bot, dp):

    @dp.message_handler(commands=['start'])
    async def process_start_command(message):
        await message.answer("Привет!\nМеня зовут ЭХО Бот\nНапиши мне что-нибудь\n")


    @dp.message_handler(commands=['help'])
    async def process_help_command(message):
        await message.answer("Напиши мне что-нибудь и я отправлю тебе в ответ сообщение")


    @dp.message_handler(content_types=['text'])
    async def send_echo(message):
        await message.reply(text=message.text)




if __name__ == "__main__":
    main(bot, dp)







