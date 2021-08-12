from microbit import *
import radio


radio.on()
while True:
    input = radio.receive()
    if input == "light on":
        pin0.write_digital(1)
    if input == "light off":
        pin0.write_digital(0)
    if input == "light flash":
        for i in range(10):
            pin0.write_digital(1)
            sleep(100)
            pin0.write_digital(0)
            sleep(100)
    if input == "slow beep":
        pin1.write_digital(1)
        sleep(500)
        pin1.write_digital(0)
        sleep(500)
    if input == "fast beep":
        pin1.write_digital(1)
        sleep(100)
        pin1.write_digital(0)
        sleep(100)
    if input == "lightTwo on":
        pin2.write_digital(1)
    if input == "lightTwo off":
        pin2.write_digital(0)
