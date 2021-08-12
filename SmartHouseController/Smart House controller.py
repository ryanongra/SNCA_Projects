from microbit import *
import radio


radio.on()
while True:
    if accelerometer.current_gesture() == "up":
        radio.send("Come in")
        sleep(1)
    elif accelerometer.current_gesture() == "shake":
        radio.send("Access denied")
        sleep(1)
    elif accelerometer.current_gesture() == "face down":
        radio.send("Light on")
        sleep(1)
    elif accelerometer.current_gesture() == "face up":
        radio.send("Light off")
        sleep(1)
    else:
        radio.send("nothing")
        sleep(1)
    message = radio.receive()
    if message == "Someone's at the door":
        display.scroll(message)
        message = ""
        sleep(1)