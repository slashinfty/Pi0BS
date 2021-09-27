# Imports
import os
import asyncio
import simpleobsws
from dotenv import load_dotenv
from gpiozero import Button, LED

# Set up
load_dotenv()
loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host=os.getenv('HOST'), port=os.getenv('PORT'), password=os.getenv('PASSWORD'), loop=loop)

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
def button1_fn():
    async def fn():
        result = await ws.call('GetVersion')
        print(result)
    loop.run_until_complete(fn())

# Connect websocket
loop.run_until_complete(ws.connect())

# Turn on LED
led.on()

# Watch for button presses
button1.when_pressed = button1_fn

# Keep program running
pause()