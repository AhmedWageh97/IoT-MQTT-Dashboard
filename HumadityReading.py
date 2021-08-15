import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
from random import seed
from random import random

min_Humadity= 30
max_Humadity= 50

def get_humadity():
	rand_value = random()
	value = -1 + (rand_value * (1 - (-1)))
	get_humadity.temp = get_humadity.temp + value
	if get_humadity.temp > 100:
		get_humadity.temp = 100
	if get_humadity.temp < 0:
		get_humadity.temp = 0
	return round(get_humadity.temp, 2)
get_humadity.temp = min_Humadity + (random() * (max_Humadity - min_Humadity))


host = "mqtt.flespi.io"
client = mqtt.Client("Humadity_Updater")
client.username_pw_set(username = "AOpERWQKeDri4nfVs9673FsgfWoNKGvajKEYvizzLOFEZLpfIjdBOvIUiUvQoQQx")
client.connect(host, port = 1883)

while True:
	client.publish("Humadity_Updater", str(get_humadity()))
	print("Humadity = ", get_humadity())
	time.sleep(1)