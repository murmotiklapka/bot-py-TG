import telebot

from setings import TG_API_TOKEN
from bot_logic import gen_pass
from bot_manyflip import many_flip

bot = telebot.TeleBot(TG_API_TOKEN)
    
bot.message_handler(commands=['begin'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['coinflip'])
def send_hello(message):
    bot.reply_to(message, many_flip())

@bot.message_handler(commands=['password'])
def send_bye(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()