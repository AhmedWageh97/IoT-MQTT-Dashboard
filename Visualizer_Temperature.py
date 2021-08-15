import random
from itertools import count
import pandas as pd
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def on_message(client, userdata, message):
	temperature = float(str(message.payload.decode("utf-8")))
	print("Temp = ", "{0:.2f}".format(temperature), " °C")
	on_message.x_list.append(on_message.counter)
	on_message.y_list.append(temperature)
	on_message.counter = on_message.counter + 1
on_message.counter = 0
on_message.x_list = []
on_message.y_list = []

def animate(i):
    plt.cla()

    plt.plot(on_message.x_list, on_message.y_list, label='Temperature')

    plt.legend(loc='upper left')
    plt.tight_layout()
	

host = "mqtt.flespi.io"
client = mqtt.Client("TemperatureVisualizer")
client.on_message = on_message
client.username_pw_set(username = "2ttM6aY8F1Nrpsks3ZqakxP7uEbmk1fcjwMduy9ZqLeD3nVWc9WluBgP5h1d74de")
client.connect(host, port = 1883)
client.loop_start()
client.subscribe("Temperature_Celisus")



plt.style.use('fivethirtyeight')
fig = plt.gcf()
ani = FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
fig.canvas.set_window_title('Temperature Monitor')
plt.show()

while True:
	
	time.sleep(1)