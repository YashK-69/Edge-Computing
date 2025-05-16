import Adafruit_DHT                #importing Adafruit_DHT sensor liabrary 
import time                                 #importing Time liabrary
import RPi.GPIO as GPIO          #importing General purpose Input Output pins of Rasberry Pi
GPIO.setmode(GPIO.BCM)             #setting Connection Mode of Circuit as BCM (not Board) 
sensor = Adafruit_DHT.DHT11        #declaring DHT sensor
pin = 23                                        #using/declaring BCM pin number 23

while True:
	humidity.temperature = Adafruit_DHT.read_retry(sensor,pin)
	if humidity is None and temperature is None:
		print("Failed to get reading. Try Again!")
	else:
		print("Temp={0:0.1f}*C Humidity={0:0.2f}%".format(temperature, humidity))
	time.sleep(1)