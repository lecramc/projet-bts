import RPi.GPIO as GPIO  # Gestion des GPIO
import subprocess
from time import sleep  # Gestion du temps
from IPyhon.display import clear_output

GPIO.setmode(GPIO.BCM)  # La numerotation choisie
GPIO.setup(16, GPIO.IN)  # Une entree : le poussoir
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

def my_callback(channel1, channel2, channel3):
        if GPIO.input(channel1):
        subprocess.call("twinkle --immediate --call sip:300@192.168.1.29", shell=True)
        else if GPIO.input(channel2):
        subprocess.call("twinkle --immediate --call sip:300@192.168.1.31", shell=True)
        else if GPIO.input(channel3):
        subprocess.call("twinkle --immediate --call sip:300@192.168.1.32", shell=True)

GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback(channel1))
GPIO.add_event_detect(23, GPIO.BOTH, callback=my_callback(channel2))
GPIO.add_event_detect(25, GPIO.BOTH, callback=my_callback(channel3))
print("Maintenant, le programme surveille les actions sur le poussoir\n")

while True:
    sleep(30)
