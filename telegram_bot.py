import os
import telebot
from chat import generate
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda msg: True)
def respond(message):
    bot.send_message(message.chat.id, generate(message.text))


if __name__ == "__main__":
    print("Started")
    bot.infinity_polling()
