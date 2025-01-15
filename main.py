import telebot, os
from dotenv import load_dotenv
from googletrans import Translator
from langdetect import detect

load_dotenv()

translator = Translator()
bot = telebot.TeleBot(os.getenv("TG_TOKEN"))

@bot.message_handler(func=lambda m: True)
def translate_message(message):
    src = detect(message.text)

    dest = 'en'

    translated_text = translator.translate(message.text, src = src, dest = dest).text

    bot.send_message(message.chat.id, translated_text)

bot.polling()