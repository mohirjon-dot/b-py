import pyowm
import telebot
from pyowm.exceptions import api_response_error

owm = pyowm.OWM('4086f9b16065b2a2a98b558b17aad533', language='ru' )
bot = telebot.TeleBot("1039356244:AAFxv2NuW7QRx91uw-JuXcqNe_zmZlq-GAw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:

		observation = owm.weather_at_place(message.text)
		w = observation.get_weather() 
		t=w.get_temperature('celsius')["temp"]
		x=w.get_wind()['speed']
		b=w.get_humidity() 		
		o=' в  городе/стране ' + message.text + '🏠 сейчась  '  + w.get_detailed_status() +', '+'\n'
		o+='🌡температура: '+ str(  t  )+ ' градус  ' + " \n "
	
		o+='ветер дует  со скоростью:💨🌬 '+str( x )+ "   км/ч   "' \n '

		o+='влажность: 💧   ' +str(   b  )+' \n \n '


		if  t>25:
		   	o+='☀☀️☀️сейчась жарко,одевайся как хочешь👕👚 '
		elif (t<=24) and (t>=11):
			o+='🌤сейчась тепло, одевайся как хочешь🥼🥼 '
		elif  (t<=10) and (t>=0) :
		  	o+='🌫сейчась холодно, одевайся как танк!!!🧥🧥🧥 '
		elif t<=-1:
		  	o+='❄️сейчась морось, одевайся как танк!!!🧥🧥🧥🧥🧥 '
	except api_response_error.NotFoundError:
		o='исправьте ошибку📌📝📝'		
	bot.send_message(message.chat.id,o)

bot.polling(none_stop = True)





