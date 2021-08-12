from microbit import *
import radio


radio.on()
while True:
    if accelerometer.current_gesture() == "face up":
        radio.send("light on")
        sleep(10)
    elif accelerometer.current_gesture() == "face down":
        radio.send("light off")
        sleep(10)
    elif accelerometer.current_gesture() == "shake":
        radio.send("light flash")
        sleep(10)
    elif accelerometer.current_gesture() == "up":
        radio.send("slow beep")
        sleep(10)
    elif accelerometer.current_gesture() == "down":
        radio.send("fast beep")
        sleep(10)
    elif accelerometer.current_gesture() == "left":
        radio.send("lightTwo on")
        sleep(10)
    elif accelerometer.current_gesture() == "right":
        radio.send("lightTwo off")
        sleep(10)
    else:
        radio.send("nothing")
        sleep(10)

