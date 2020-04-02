import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('907223123:AAFnerHYgAzRTEOJuXQRzK3UB5M-pTT1nlM')

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton("Ukraine")
	btn2 = types.KeyboardButton("World")
	btn3 = types.KeyboardButton("Canada")
	btn4 = types.KeyboardButton("Turkey")
	markup.add(btn1, btn2, btn3, btn4)


	send_mess = "Hi, {0.first_name}\nEnter country".format(message.from_user)
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "ukraine":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "canada":
		location = covid19.getLocationByCountryCode("CA")
	elif get_message_bot == "turkey":
		location = covid19.getLocationByCountryCode("TR")
	elif get_message_bot == "world":
		location = covid19.getLatest()
		final_message = "<b>World</b>\nConfirmed: {0}\nDeaths: {1}".format(location['confirmed'], location['deaths'])
	else:
		final_message = "Enter country, please"

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = "<b>{2}</b>\nLast updated: {3} {4}\nConfirmed: {0}\nDeaths: {1}".format(location[0]['latest']['confirmed'], location[0]['latest']['deaths'], location[0]['country'], date[0], time[0])


	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)