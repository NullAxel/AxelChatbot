import os
import telebot
from chat import generate
BOT_TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda msg: True)
def respond(message):
    bot.send_message(message.chat.id, generate(message.text))


if __name__ == "__main__":
    bot.infinity_polling()
