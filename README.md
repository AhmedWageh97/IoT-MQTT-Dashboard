# IoT-MQTT-Dashboard
 Simple IoT monitoring system for monitoring temperature, humadity, AC/heater status, and location.

# Description
 This project implemented in Python. It consists of some main features:
 * __Temparature Reader__: It mimics the reading of temperature from a real temperature sensor
							by generating a random number which acts as a temperature and puplishes
							it via MQTT under a topic with name of "__Temperature_Celisus__". It also
							changes the status of AC and heater according to the current 
							measured(randomly generated) temperature and it puplishes the status of them 
							to the dashboard under topics with names of "__AC_Updater__" and "__Heater_Updater__".
 * __Humadity Reader__: It works in the same way as __Temparature Reader__, generating a random percent which
						acts as the humadity measured from a real humadity sensor. Afterthat, it puplishes 
						the measured(randomly generated) humadity to the dashboard under a topic with name of
						"__Humadity_Updater__"
 * __Temparature Visualizer__: It subscribes the puplished data under the topic of "__Temperature_Celisus__" 
								and plots it virsus time.
 * __Humadity Visualizer__: It works in the same way as __Temparature Visualizer__ but it subscribes the topic of
							"__Humadity_Updater__"
 * __GPS Tracker__: It sends a HTTP request to a [site](https://ipinfo.io/) which responds with JSON data with all 
					needed information about the location(IP, hostname, city name, region, country, loc[latitude and longitude], timezone, etc.)
					after that it sends the needed data to dashboard to be displayed.
 * __Firebase Updater__: It subscribes all the mentioned topics and sends them to a realtime database(firebase).

