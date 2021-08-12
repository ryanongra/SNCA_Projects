from microbit import *
import radio

threshold = 80
radio.on()


def ring():
    for i in range(10):
            pin0.write_digital(1)
            sleep(100)
            pin0.write_digital(0)
            sleep(100)


while True:
    if button_a.is_pressed():
        threshold -= 5
        display.scroll(str(threshold))
    if button_b.is_pressed():
        threshold += 5
        display.scroll(str(threshold))
    if temperature() > threshold:
        radio.send("0")
        ring()
    message = radio.receive()
    if message == "0":
        ring()
