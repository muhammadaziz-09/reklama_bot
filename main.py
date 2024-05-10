import sqlite3

from aiogram.types import Message,CallbackQuery
from aiogram import Bot,Dispatcher,executor
from databease import registeruser

api = '7123559250:AAEB2AFnHhF7BmLi3DQxZSFH_LKRz3UUr4A'

bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    fullname = message.from_user.full_name
    username = message.from_user.username
    try:
        registeruser(fullname, username, chatid)
        await bot.send_message(chat_id=chatid, text=f'Xush kelibsiz{fullname}')
    except:
        await bot.send_message(chat_id=chatid, text=f'Qaytganingizdan xursandmiz{fullname}')

@dp.message_handler()
async def reklama(message:Message):

    # databease = sqlite3.connect('databease.sqlite')
    # cursor = databease.cursor()
    # cursor.execute('''SELECT chatid FROM users''')
    # users = cursor.fetchall()
    # for user in users:
    #     await bot.send_message(chat_id=user[0],text=message.text)

    databease = sqlite3.connect('databease.sqlite')
    cursor = databease.cursor()
    cursor.execute('''SELECT chatid FROM users WHERE fullname = ?''',('',))
    users = cursor.fetchone()
    print(users)
    if users:
        await bot.send_message(chat_id=users[0], text=message.text)
    else:
        await bot.send_message(chat_id=message.chat.id,text='siz admin emassiz')
executor.start_polling(dp, skip_updates=True)
