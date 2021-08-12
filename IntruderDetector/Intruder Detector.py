from microbit import *
import speech
import radio


radio.on()
active = True
passcode = 1234
eye = Image("00000:"
            "09990:"
            "90909:"
            "09990:"
            "00000")
while True:
    if active:
        display.show(eye)
        if accelerometer.get_x() > 500 or accelerometer.get_x() < -500:
            for i in range(5):
                speech.say("INTRUDER ALERT!")
                sleep(2000)
        if accelerometer.get_y() > 500 or accelerometer.get_y() < -500:
            for i in range(5):
                speech.say("INTRUDER ALERT!")
                sleep(2000)
    else:
        display.scroll("DISARMED")
    message = radio.receive()
    if message == passcode:
        active = not active
