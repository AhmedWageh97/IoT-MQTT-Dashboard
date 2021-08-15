import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import requests
import json

host = "mqtt.flespi.io"
client = mqtt.Client("GPS_Updater")
client.username_pw_set(username = "l4v4CcYD1jgBrowWl0G9mxqNXZ5Ze74p1nirq6UffYGvd0fmQLl27zDUozJswBGl")
client.connect(host, port = 1883)

res = requests.get('https://ipinfo.io/')	
GPS_data = res.json()
city = GPS_data['city']
region = GPS_data['region']
country = GPS_data['country']

city_data =  str(city + "_" + region + "_" + country)

location = GPS_data['loc'].split(',')
latitude = location[0]
longitude = location[1]

while True:
	client.publish("location", str(location))
	client.publish("Latitude", str(latitude))
	client.publish("Longitude", str(longitude))
	client.publish("city_data", str(city_data))
	client.publish("City_Name", str(city))
	client.publish("rigion_name", str(region))
	client.publish("country_name", str(country))
	time.sleep(1)