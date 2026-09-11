import telebot
from telebot import types

BOT_TOKEN = "8906985653:AAFC5_j2RTP3n4OLIxJ-G1WZFMVgMAaAgts"
WEBAPP_URL = "https://gist.githubusercontent.com/freemanton000/ad598f2a75436929ae8e8471915d3279/raw/952e919a532b82d04bb8926cd505262d96c2ae0e/index.html"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    webapp_info = types.WebAppInfo(WEBAPP_URL)
    btn = types.InlineKeyboardButton(text="👁 ОТКРЫТЬ ГЛАЗ ГОРА", web_app=webapp_info)
    markup.add(btn)
    
    welcome_text = (
        "⚡️ Приветствуем в EYE OF HORUS (Глаз Гора)!\n\n"
        "Это автономный Кармический Фрактальный Аудитор Реальности.\n"
        "Мы сорвем маски с инфошума элит и паразитов прямо с дивана.\n\n"
        "Нажми на кнопку ниже, чтобы запустить аудит истины."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

if __name__ == '__main__':
    print("Глаз Гора активирован... Инфополе под контролем!")
    bot.infinity_polling()
