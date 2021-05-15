#Program for Web_Scraping of Weather Stats of any city With API (openweathermap.org).

import datetime
import requests

OW_Api="7e45cc279f5780f859a01df53977590d"  #This is the openweathermap API(free), just replace this api with your own API.

Location=input("Enter you city name:")

OW_link=f"https://api.openweathermap.org/data/2.5/weather?q={Location}&appid={OW_Api}"   


req=requests.get(OW_link)     #Here we getting the url raw data using request module. 
# print("req value :",req)

data=req.json()               #Here we are filtering out the json data in python format. 
# print("Json data :",data)


if data["cod"]!="404":
	temp=(data['main']['temp']-273)

	weather=(data['weather'][0]['description'])

	pressure=(data['main']['pressure']/100)

	humidity=(data['main']['humidity'])

	windspeed=(data['wind']['speed'])

	country=(data['sys']['country'])



	print("______________________________________________________________")
	print(f"The Weather Stats For {(Location.capitalize())} at {(datetime.datetime.now().strftime('%d %b %Y | %I:%M:%S %p'))} is:")
	print("______________________________________________________________")

	print(f"Temperaure          : {temp :.2f} *C  \nWeather Description : {format(weather.capitalize())}  \nPressure            : {pressure} pascal  \nHumidity            : {humidity} %, \nwindspeed           : {windspeed:.2f} kmph  \nCountry             : {country}")


else:
	print("City Not Found!!")

# print(data['timezone'])
# x=datetime.datetime.now()
# print(datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))





















