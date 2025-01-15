import telebot
from googletrans import Translator
from langdetect import detect

translator = Translator()
bot = telebot.TeleBot("7533179279:AAEnTFdF4IPX1GwbomBmEs_gG2qs87sN5pc")

@bot.message_handler(func=lambda m: True)
def translate_message(message):
    src = detect(message.text)

    dest = 'en'

    translated_text = translator.translate(message.text, src = src, dest = dest).text

    bot.send_message(message.chat.id, translated_text)

bot.polling()