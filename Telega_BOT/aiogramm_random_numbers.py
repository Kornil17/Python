from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType
from dataclasses import dataclass
import random
from magic_filter import F

BOT_TOKEN: str = '5947498423:AAE3ve6bCjFoYVBhk9lbnPa1fTTqy8Z6yCY'
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)

# Количество попыток, доступных пользователю в игре
ATTEMPTS: int = 5

# Словарь, в котором будут храниться данные пользователя
user: dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}


# Функция возвращающая случайное целое число от 1 до 100
def get_random_number() -> int:
    return random.randint(1, 100)


async def process_start_command(message: types.Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')


async def process_help_command(message: types.Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


async def process_stat_command(message: types.Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}')


async def process_cancel_command(message: types.Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        user['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


async def process_positive_answer(message: types.Message):
    if not user['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


async def process_negative_answer(message: types.Message):
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


async def process_numbers_answer(message: types.Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Мое число меньше')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Мое число больше')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


async def process_other_text_answers(message: types.Message):
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')

# Этот хэндлер будет срабатывать на команду "/start"
dp.register_message_handler(process_start_command, commands=['start'])

# Этот хэндлер будет срабатывать на команду "/help"
dp.register_message_handler(process_help_command, commands=['help'])

# Этот хэндлер будет срабатывать на команду "/stat"
dp.register_message_handler(process_stat_command, commands=['stat'])

# Этот хэндлер будет срабатывать на команду "/cancel"
dp.register_message_handler(process_cancel_command, commands=['cancel'])

# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
# dp.register_message_handler(process_positive_answer, text=['Да', 'Давай', 'Сыграем', 'Игра','Играть', 'Хочу играть'])
dp.register_message_handler(process_positive_answer, F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']))

# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
# dp.register_message_handler(process_negative_answer, text=['Нет', 'Не', 'Не хочу', 'Не буду'])
dp.register_message_handler(process_negative_answer, F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))

# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
dp.register_message_handler(process_numbers_answer, lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)

# # Этот хэндлер будет срабатывать на остальные любые сообщения
# dp.register_message_handler(process_other_text_answers, content_types=['text'])

if __name__ == '__main__':
    executor.start_polling(dp)