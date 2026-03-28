import gpiozero
from time import sleep

led = gpiozero.LED(17)  # GPIO 17

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)