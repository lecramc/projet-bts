import RPi.GPIO as GPIO  # Gestion des GPIO
import subprocess
from time import sleep  # Gestion du temps
from IPython.display import clear_output

GPIO.setmode(GPIO.BCM)  # La numerotation choisie
GPIO.setup(16, GPIO.IN)  # Une entree : le poussoir


def my_callback(channel):
	if GPIO.input(channel):
       		subprocess.call("twinkle --immediate --call sip:300@192.168.1.29", shell=True)


print("Vous pouvez aussi terminer avec CTRL+C \n")
GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)

while True:
	sleep(30)
	clear_output()
