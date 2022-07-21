from aiogram import types, Dispatcher
from create_bot import dp, bot

import json, string

# @dp.message_handler()
# async def something(message : types.Message):
#     if message.text == 'Привет':
#
#         await message.answer('Ну приветик')
#     # await message.reply(message.text)
#     # await bot.send_message(message.from_user.id, message.text)

'''Это фильтр нецензурной лексики, пока не работате, тк json пустой'''
# @dp.message_handler()
async def bad_words(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Запрещенное слово!!!!')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(bad_words)
