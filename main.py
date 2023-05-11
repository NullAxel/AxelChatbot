from random import choice
import os
import telebot
import json
CONFIG = json.load(open("config.json", "r"))
BOT_TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]
ERROR_RESPONSES=CONFIG["ERROR_RESPONSES"]
INTENTS=CONFIG["INTENTS"]


def debug(result: str):
    print(f"DEBUG: {result}")

def generate(inp: str):
    intent = [intent for intent in INTENTS if inp in intent["patterns"]]
    if intent == []:
        out = choice(ERROR_RESPONSES)
        debug(f"{inp};unknown;{out}")
        return out
    else:
        out = choice(intent[0]["responses"])
        debug(f"{inp};{intent[0]['tag']};{out}")
        return out


bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.chat.id, generate(message.text))


if __name__ == "__main__":
    bot.infinity_polling()
