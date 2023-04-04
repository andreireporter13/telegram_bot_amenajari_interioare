#
#
#
from aiogram import types, Dispatcher
from create_bot import dp, bot

# import keyboards from client
from keyboards import kb_client


MESSAGE_START_HELP = """
Salut. Te putem ajuta cu: 
... tra-ta-ta!!!
"""

# start create commands
#
async def send_info_message(message: types.Message): 
    #
    # sent message to user
    await bot.send_message(message.from_user.id, MESSAGE_START_HELP, reply_markup=kb_client) # if keyboard don't need - reply_markup = ReplyKeyboardRemove
    await message.delete()
    

# code for export commands
def register_handlers_client(dp : Dispatcher):
    #
    dp.register_message_handler(send_info_message, commands=['start', 'help'])
    