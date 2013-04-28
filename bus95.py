
import display
import stib
from time import time


while True:
    print "updating"
    display.ledall()
    stations = stib.get_stations()
    print [k for k,v in stations.iteritems() if v]
    leds = stib.leds_from_stations(stations)
    start = time()

    while time() - start < 20:
        display.cycle(leds, 3,3)

