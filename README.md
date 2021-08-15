# IoT-MQTT-Dashboard
 Simple IoT monitoring system for monitoring temperature, humadity, AC/heater status, and location.

# Description
 This project implemented in Python. It consists of some main features:
 * [__Temparature Reader__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/TemperatureReading.py): 
							It mimics the reading of temperature from a real temperature sensor
							by generating a random number which acts as a temperature and puplishes
							it via MQTT under a topic with name of "__Temperature_Celisus__". It also
							changes the status of AC and heater according to the current 
							measured(randomly generated) temperature and it puplishes the status of them 
							to the dashboard under topics with names of "__AC_Updater__" and "__Heater_Updater__".
 * [__Humadity Reader__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/HumadityReading.py): 
						It works in the same way as __Temparature Reader__, generating a random percent which
						acts as the humadity measured from a real humadity sensor. Afterthat, it puplishes 
						the measured(randomly generated) humadity to the dashboard under a topic with name of
						"__Humadity_Updater__"
 * [__Temparature Visualizer__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/Visualizer_Temperature.py): 
								It subscribes the puplished data under the topic of "__Temperature_Celisus__" 
								and plots it virsus time.
 * [__Humadity Visualizer__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/Visualizer_Humadity.py): 
							It works in the same way as __Temparature Visualizer__ but it subscribes the topic of
							"__Humadity_Updater__"
 * [__GPS Tracker__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/GPS_Tracker.py): 
					It sends a HTTP request to a [site](https://ipinfo.io/) which responds with JSON data with all 
					needed information about the location(IP, hostname, city name, region, country, loc[latitude and longitude], timezone, etc.)
					after that it sends the needed data to dashboard to be displayed.
 * [__Firebase Updater__](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/FirebaseUpdater.py): 
					It subscribes all the mentioned topics and sends them to a realtime database(firebase).

 All these topics data are published to [flespi dashboard](https://flespi.io) which visualises all these data
 in widgets as in [this image](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/Flespi%20IoT%20dashboard.JPG).

# Running steps
 You have to follow some steps to run this project correctly and get the best result as follows:
 * Install python 3 and all needed libraries(MQTT, Firebase, etc.).
 * Open [flespi dashboard site](https://flespi.io)
 * Every running code will publish or subscribe data(payloads) to the dashboard need to get access. So, you need to create access as follows:
	* Open [flespi dashboard site](https://flespi.io).
	* Go to __Tokens__ section.
	* Click on the green "+" mark on the bottom right of the site.
	* Mark __expire__ option and set the expiry date of this __token__(user) as you want.
	* Now the __token__ is created. Click on __Copy token__ in the created token.
	* Paste it in python code that publishes or subscribes any topic in the project as a username in 
	  __username_pw_set__ methon in __client__(MQTT client) class.
 * For [firebase code](https://github.com/AhmedWageh97/IoT-Monitoring-Project-MQTT/blob/main/FirebaseUpdater.py),
   you need to add the link to your database as a parameter for __firebase.FirebaseApplication__ method.
 * Open the [flespi dashboard site](https://flespi.io) and go to __MQTT Tiles__ section.
 * Now you can run all the scripts and see the result.