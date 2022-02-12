import COVID19Py as covid
import telebot
from telebot import types


covid19 = covid.COVID19()

bot = telebot.TeleBot('5154254007:AAG2l3rauYMh4LrV35yMzV6DpIWrh7h1dDo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Во всем мире")
    btn2 = types.KeyboardButton("Россия")
    btn3 = types.KeyboardButton("Украина")
    btn4 = types.KeyboardButton("США")
    btn5 = types.KeyboardButton("Узбекистан")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    send_mess =  f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'сша':
        location = covid19.getLocationByCountryCode('US')
    elif get_message_bot == 'украина':
        location = covid19.getLocationByCountryCode('UA')
    elif get_message_bot == 'россия':
        location = covid19.getLocationByCountryCode('RU')
    elif get_message_bot == 'узбекистан':
        location  = covid19.getLocationByCountryCode('UZ')
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b> Заболевшие: </b>{location['confirmed']}\n"

    if final_message == '':
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране</u>\nНаселение: {location[0]['country_population']}\n" \
                        f"Последниее обновление: {date[0]} {time[0]}\nПоследнее данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)


latest = covid19.getLatest()

location = covid19.getLocationByCountryCode('US')

print(location[0]['last_updated'])
