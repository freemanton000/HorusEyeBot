import telebot
from telebot import types

BOT_TOKEN = "8906985653:AAFC5_j2RTP3n4OLIxJ-G1WZFMVgMAaAgts"
WEBAPP_URL = "https://your-domain.com/index.html"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "👁️ ГЛАЗ ГОРА АКТИВИРОВАН\n\n"
        "«Мы не верим словам. Мы вычисляем энтропию.»\n\n"
        "Это независимый кармический аудитор.\n"
        "Вставь имя политика, корпорации или цитату — "
        "и система прокачает его через фрактальный фильтр.\n\n"
        "Нажми кнопку ниже, чтобы открыть Глаз Гора."
    )

    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="ОТКРЫТЬ ГЛАЗ ГОРА",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    markup.add(btn)

    bot.send_message(message.chat.id, text, reply_markup=markup)

if __name__ == "__main__":
    bot.polling(non_stop=True)
