import random

import config
from creat_bot import dp
from aiogram.types import Message


@dp.message_handler(commands=['start', 'начать'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, привет!\n'
                              f'Сегодня мы с тобой поиграем в интересную игру.\n'
                              f'Для старта жми: /new\n')

@dp.message_handler(commands=['new'])
async def mes_new_game(message: Message):
    name = message.from_user.first_name
    for game in config.games:
        if message.from_user.id == game:
            await message.answer(f'{name}, ты уже есть в игре! Иди играй!')
            break
    else:
        config.total = 150
        await message.answer(text=f'На столе {config.total} конфет. Кидаем жребий, кто берет первым.')
        coin = random.randint(0, 1)
        config.games[message.from_user.id] = 150
        if coin:
            await message.answer(text=f'{name}, поздравляю!\n'
                                    f'Выпал орел. Ты ходишь первым! Бери от одной до 28 конфет.')
        else:
             await message.answer(text=f'{name}, не расстраивайся!\n'
                                    f'Первый ход делает бот.')
        await bot_turn(message)


@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            await player_turn(message)
        else:
            await message.answer(text=f'Ах, ты, хитрый, {message.from_user.first_name}! Конфет надо взять '
                                      f'хотя бы одну, но не более 28!\n'
                                      f'Попробуй еще раз.')
    else:
        await message.answer(text='Введи цифрами количество конфет.')

async def player_turn(message: Message):
    take_amount = int(message.text)
    print(config.games.get(message.from_user.id))
    config.games[message.from_user.id] = config.games.get(message.from_user.id) - take_amount
    name = message.from_user.first_name
    await message.answer(text=f'{name}, взял {take_amount} конфет и на столе осталось '
                              f'{config.games.get(message.from_user.id)}\n')
    if await check_victory(message, name):
        return
    await message.answer(text=f'Торжественно передаем ход боту!')
    await bot_turn(message)

async def bot_turn(message: Message):
    take_amount = 0
    current_total = config.games.get(message.from_user.id)
    if current_total <= 28:
       take_amount = current_total
    else:
        take_amount = current_total%29 if current_total%29 != 0 else 1
    take_amount = random.randint(1, 28)
    config.games[message.from_user.id] = config.games.get(message.from_user.id) - take_amount
    name = message.from_user.first_name
    await message.answer(text=f'Бот взял {take_amount} конфет и на столе осталось {config.games.get(message.from_user.id)}\n')
    if await check_victory(message, 'Бот'):
        return
    await message.answer(text=f'{name}, теперь твой черед! Бери конфеты.')

async def check_victory(message: Message, name: str):
    if config.games.get(message.from_user.id) <= 0:
        await message.answer(text=f'Победил - {name}! Это была славная игра!\n'
                                  f'Сыграй еще раз!\n'
                                  f'Жми /new')
        config.games.pop(message.from_user.id)
        return True
    return False


