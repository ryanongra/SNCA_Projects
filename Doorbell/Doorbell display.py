from microbit import *
import radio


radio.on()
enter = False
while True:
    if enter:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    if button_a.is_pressed():
        radio.send("Someone's at the door")
        sleep(100)
    message = radio.receive()
    if message == "Come in":
        enter = True
        display.scroll(message)
    if message == "Access denied":
        enter = False
        display.scroll(message)
