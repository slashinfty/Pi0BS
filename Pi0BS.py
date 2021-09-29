# Imports
import os
import asyncio
from simpleobsws import obsws
from gpiozero import Button, LED

# Set up - edit the host, port, and password
load_dotenv()
loop = asyncio.get_event_loop()
ws = obsws(host='192.1.168.1', port=4444, password='password', loop=loop)

# Pins use the physical numbering of the board
led = LED('BOARD3')
button1 = Button('BOARD5')
button2 = Button('BOARD7')
button3 = Button('BOARD8')
button4 = Button('BOARD10')
button5 = Button('BOARD11')
button6 = Button('BOARD12')
button7 = Button('BOARD13')
button8 = Button('BOARD15')
button9 = Button('BOARD16')
button10 = Button('BOARD18')
button11 = Button('BOARD19')
button12 = Button('BOARD21')
button13 = Button('BOARD22')
button14 = Button('BOARD23')
button15 = Button('BOARD24')
button16 = Button('BOARD26')
button17 = Button('BOARD29')
button18 = Button('BOARD31')
button19 = Button('BOARD32')
button20 = Button('BOARD33')
button21 = Button('BOARD35')
button22 = Button('BOARD36')
button23 = Button('BOARD37')
button24 = Button('BOARD38')
button25 = Button('BOARD40')

# Functions - edit these!
# Button 1 - Function
def button1_fn():
    async def fn():
        result = await ws.call('GetVersion')
        print(result)
    loop.run_until_complete(fn())

# Button 2 - Function


# Button 3 - Function


# Button 4 - Function


# Button 5 - Function


# Button 6 - Function


# Button 7 - Function


# Button 8 - Function


# Button 9 - Function


# Button 10 - Function


# Button 11 - Function


# Button 12 - Function


# Button 13 - Function


# Button 14 - Function


# Button 15 - Function


# Button 16 - Function


# Button 17 - Function


# Button 18 - Function


# Button 19 - Function


# Button 20 - Function


# Button 21 - Function


# Button 22 - Function


# Button 23 - Function


# Button 24 - Function


# Button 25 - Function


# Connect websocket
loop.run_until_complete(ws.connect())

# Turn on LED
led.on()

# Watch for button presses
button1.when_pressed = button1_fn
button2.when_pressed = button2_fn
button3.when_pressed = button3_fn
button4.when_pressed = button4_fn
button5.when_pressed = button5_fn
button6.when_pressed = button6_fn
button7.when_pressed = button7_fn
button8.when_pressed = button8_fn
button9.when_pressed = button9_fn
button10.when_pressed = button10_fn
button11.when_pressed = button11_fn
button12.when_pressed = button12_fn
button13.when_pressed = button13_fn
button14.when_pressed = button14_fn
button15.when_pressed = button15_fn
button16.when_pressed = button16_fn
button17.when_pressed = button17_fn
button18.when_pressed = button18_fn
button19.when_pressed = button19_fn
button20.when_pressed = button20_fn
button21.when_pressed = button21_fn
button22.when_pressed = button22_fn
button23.when_pressed = button23_fn
button24.when_pressed = button24_fn
button25.when_pressed = button25_fn

# Keep program running
pause()
