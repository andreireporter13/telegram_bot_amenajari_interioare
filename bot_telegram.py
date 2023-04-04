# New Telegram Bot for "Amenajari interioare"
#
############################################################################
#
#
# Author: Andrei C. Cojocaru
# Linkedin: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Facebook: https://www.facebook.com/webautomation.romania
# Tiktok:  https://www.tiktok.com/@andrei_13.py
# Twitter: https://twitter.com/andrei_reporter
# Youtube: https://www.youtube.com/channel/UCgx_Y9OHi5KPVzLJo9setxw/featured
# GitHub: https://github.com/andreireporter13
# Website: https://webautomation.ro/
# 
# 
############################################################################
#
#
# 
from aiogram.utils import executor
from create_bot import dp

from handlers import client, admin, remove_bad_words


# message ---> notification 
async def on_startup(_):
    print('Bot is online now!')


# from handlers
client.register_handlers_client(dp)
remove_bad_words.register_handler_remove_bad_words(dp)
#



# if __name__ == "__main__": -> important construction for every code
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
