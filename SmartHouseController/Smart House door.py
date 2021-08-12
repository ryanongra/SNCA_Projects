from microbit import *
import radio
import speech


radio.on()
enter = False
sensitivity = 11
active = True


def alert():
    display.scroll("INTRUDER!")
    for i in range(5):
        speech.say("Intruder")
        sleep(2000)


def checkMovement():
    if active:
        if accelerometer.get_x() > 100*sensitivity:
            alert()
        elif accelerometer.get_x() < -100*sensitivity:
            alert()
        elif accelerometer.get_y() > 100*sensitivity:
            alert()
        elif accelerometer.get_y() < -100*sensitivity:
            alert()


while True:
    if enter:
        display.show(Image.YES)
        checkMovement()
    else:
        display.show(Image.NO)
        checkMovement()
    if button_a.is_pressed():
        radio.send("Someone's at the door")
        sleep(1000)
    try:
        message = radio.receive()
        if message == "Come in":
            enter = True
            active = False
            display.scroll(message)
            message = ""
            sleep(1000)
        if message == "Access denied":
            enter = False
            active = True
            display.scroll(message)
            message = ""
            sleep(1000)
        if message == "Light on":
            pin1.write_digital(1)
            message = ""
            sleep(1000)
        if message == "Light off":
            pin1.write_digital(0)
            message = ""
            sleep(1000)
    except ValueError as e:
        display.scroll("")
