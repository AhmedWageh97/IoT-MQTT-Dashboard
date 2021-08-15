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
	print("Humadity = ", "{0:.2f}".format(temperature), " %")
	on_message.x_list.append(on_message.counter)
	on_message.y_list.append(temperature)
	on_message.counter = on_message.counter + 1
on_message.counter = 0
on_message.x_list = []
on_message.y_list = []

def animate(i):
    plt.cla()

    plt.plot(on_message.x_list, on_message.y_list, 'r', label='Humadity')

    plt.legend(loc='upper left')
    plt.tight_layout()
	

host = "mqtt.flespi.io"
client = mqtt.Client("HumadityVisualizer")
client.on_message = on_message
client.username_pw_set(username = "tnHFCgweyZomOaCJJEf89cvUGLPI08YhltMMz9OXY08A1yay1dwYfPJKomgcl2ju")
client.connect(host, port = 1883)
client.loop_start()
client.subscribe("Humadity_Updater")



plt.style.use('fivethirtyeight')
fig = plt.gcf()
ani = FuncAnimation(fig, animate, interval=1000)

plt.tight_layout()
fig.canvas.set_window_title('Humadity Monitor')
plt.show()

while True:
	
	time.sleep(1)