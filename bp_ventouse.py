import RPi.GPIO as GPIO  # Gestion des GPIO
from time import sleep   # Gestion du temps

GPIO.setmode(GPIO.BCM)   # La numerotation choisie
GPIO.setup(21, GPIO.IN) # Une sortie : la poussoir

def my_callback(channel):
  if GPIO.input(channel):
    print('GPIO %s 0->1' %channel)
    GPIO.output(21, GPIO.LOW)
  else:
    print('GPIO %s 1->0' %channel)
    GPIO.output(21, GPIO.HIGH)

print("Vous pouvez aussi terminer avec CTRL+C \n")

GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback)
print("Maintenant, le programme surveille les actions sur le poussoir\n")

while True:
  sleep(30)
