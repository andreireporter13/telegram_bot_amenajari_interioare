#
#
#
# here write a script to remove bad words from group

from aiogram import types, Dispatcher
from create_bot import dp, bot

import json, string


# remove bad words for grup
async def catch_bad_word(message: types.Message): 
    if {word.lower().translate(str.maketrans('', '', string.punctuation))\
        for word in message.text.split(' ')}.intersection(set(json.load(open('bad_words.json')))) != set():
            
        await message.reply('Injuraturile sunt interzise!')
        await message.delete()

    # else, catch other messages from user_input
    else: 
        await bot.send_message(message.from_user.id, 'Pentru detalii exacte, va rugam sa folositi comanda /help sau /start!')
        await message.delete()


def register_handler_remove_bad_words(dp : Dispatcher):
    #
    dp.register_message_handler(catch_bad_word)