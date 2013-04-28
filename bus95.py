
import display
import stib

stations = stib.get_stations()
leds = stib.leds_from_stations(stations)

while True: display.cycle(leds, 3,3)

