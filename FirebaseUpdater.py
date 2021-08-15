import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
from firebase import firebase
import json
from firebase.wrapper import Firebase

def on_message(client, userdata, message):
	print("Received", end = ": ")
	received_message = str(message.payload.decode("utf-8"))
	#print(str(message.payload) + " " + message.topic)
	print(received_message, end = " - ")
	print(message.topic)
	if message.topic == "Temperature_Celisus":
		data =  { 'Temperature': received_message}
		print("Before")
		FirebaseClient.post("/Temperature", data)
		print("Done")
	if message.topic == "location":
		step1 = received_message.split(',')
		longitude = step1[0][2:-1]
		latitude = step1[1][2:-2]
		data =  { 'Longitude': longitude,
		'Latitude': latitude}
		FirebaseClient.post("/Location", data)
	if message.topic == "city_data":
		city_data = received_message.split('_')
		
		city = city_data[0]
		region = city_data[1]
		country = city_data[2]
		
		city_data = {'city': city,
		'region': region,
		'country': country
		}
		FirebaseClient.post("/City Data", city_data)
	if message.topic == "Humadity_Updater":
		data =  { 'Humadity': received_message}
		FirebaseClient.post("/Humadity", data)

#host = "mqtt.flespi.io"
#client = mqtt.Client("FireBaseUpdater")
#client.on_message = on_message
#client.username_pw_set(username = "bAsRJ3lPfPLXPOe23hGdITYUthyZxPnzfFgMwrrB42pJFrzyx4B3NnO6saTQP6fS")
#client.connect(host, port = 1883)
#client.loop_start()
#client.subscribe("Temperature_Celisus")
#client.subscribe("Humadity_Updater")
#client.subscribe("location")
#client.subscribe("city_data")
FirebaseClient = Firebase('https://iot-temperature-monitor-ef062-default-rtdb.firebaseio.com/')


while True:
	Datadd = {'Hi': 5}
	json_object = json.dumps(Datadd, indent = 4)
	FirebaseClient.post("/Test", json_object)
	time.sleep(1)