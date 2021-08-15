import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
from random import seed
from random import random

min_temparature = 22.0
max_temparature = 28.0

def get_temparature():
	rand_value = random()
	value = -1 + (rand_value * (1 - (-1)))
	get_temparature.temp = get_temparature.temp + value
	return round(get_temparature.temp, 2)
get_temparature.temp = min_temparature + (random() * (max_temparature - min_temparature))

AC_State = 0
Heater_State = 0

host = "mqtt.flespi.io"
client = mqtt.Client("Temperature_Updater")
client.username_pw_set(username = "iQ0pdwA4qWdX21Eg8m4Bi4wY53j1ecQkRFAU10MiMO3CFxIDHB3NvpzqgJfkJUvq")
client.connect(host, port = 1883)

while True:
	temperature = get_temparature()
	client.publish("Temperature_Celisus", str(temperature))	
	if temperature >= 25:
		if AC_State == 0:
			print("Turn on AC", temperature)
			AC_State = 1
			client.publish("AC_Updater", str(AC_State))
	else:
		if AC_State == 1:
			print("Turn off AC", temperature)
			AC_State = 0
			client.publish("AC_Updater", str(AC_State))
	if temperature <= 18:
		if Heater_State == 0:
			print("Turn on Heater", temperature)
			Heater_State = 1
			client.publish("Heater_Updater", str(Heater_State))
	else:
		if Heater_State == 1:
			print("Turn off Heater", temperature)
			Heater_State = 0
			client.publish("Heater_Updater", str(Heater_State)) 
	time.sleep(1)