import telebot
from telebot.types import Message

TOKEN = '704001319:AAHwbOYzZoHaRCN73XGEEhAF2aN_wAb61Pw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_message(message: Message):
    bot.reply_to(message, message.text)

bot.polling()