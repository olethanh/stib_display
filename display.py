from time import sleep
from itertools import chain

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

status = {}
ins = [8, 10, 12]
outs = [7,5,3]
leds_list = list(chain(*[[(i,o) for o in outs] for i in ins]))

def set(channel, state):
    if channel not in status:
        GPIO.setup(channel, GPIO.OUT, initial=state)
    else:
        GPIO.output(channel, state)
        print 'set ', channel, 'to ', state
        status[channel] = state

def on(channel):
    set(channel, GPIO.HIGH)

def off(channel):
    set(channel, GPIO.LOW)

def reset():
    for i in ins: off(i)
    for o in outs: on(o)

def ledall():
    for i in ins: on(i)
    for o in outs: off(o)

def led(i):
    on(leds_list[i][0])
    off(leds_list[i][1])

def ledoff(i):
    off(leds_list[i][0])
    on(leds_list[i][1])

def cycle(leds, rows, cols):
    for r in range(rows):
        reset()
        for u in range(r*cols, (r+1)*cols):
            if u in leds:
                led(u)
        sleep(10.0/1000)

