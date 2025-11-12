import telebot
from bot_manyflip import many_flip
from bot_logic import gen_pass
from bot_zetat import zetatfunc
from setings import TG_API_TOKEN
import time, threading, schedule

bot = telebot.TeleBot(TG_API_TOKEN)

bot.message_handler(commands=['begin'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['coinflip'])
def send_hello(message):
    bot.reply_to(message, many_flip())

@bot.message_handler(commands=['password'])
def send_bye(message):
    bot.reply_to(message, gen_pass())

@bot.message_handler(commands=['zytata'])
def send_zedat(message):
    bot.reply_to(message, zetatfunc())

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(content_types= ["sticker"])
def send_stik(message):
    bot.reply_to(message, 'Привет! Я бот!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh) 

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Use /set <seconds> to set a timer")


def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)

bot.polling()