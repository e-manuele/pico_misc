import asyncio


class cocktail_manager:
    def __init__(self, cocktails_list: dict, pumps_list: dict):
        self.cocktails_list = cocktails_list
        self.pumps_list = pumps_list

    async def spill(self, cocktail_name: str):
        # return_recipe = [ [1,4] ,[2,5] ]
        print("Spilling")
        for pump in self.cocktails_list[cocktail_name].return_recipe():
            print(pump)
            turn_on_pump = asyncio.create_task(self.pumps_list[pump[0]].on(pump[1]))
            await turn_on_pump

    def return_cocktails_list(self):
        return [cocktail for cocktail in self.cocktails_list]

'''
from machine import Pin
import uasyncio as asyncio

# Definisci i pin GPIO per i LED
led_pins = [2, 3, 4]

# Inizializza i pin GPIO come pin di uscita
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

# Funzione asincrona per lampeggiare un LED con un determinato intervallo
async def blink_led(led, interval_ms):
    for _ in range(10):  # Esegui il ciclo 10 volte (o quante volte desideri)
        led.value(not led.value())  # Inverti lo stato del LED
        await asyncio.sleep_ms(interval_ms)

# Avvia le funzioni asincrone per ciascun LED con intervalli diversi
loop = asyncio.get_event_loop()
for led, interval_ms in zip(leds, [500, 1000, 1500]):
    loop.create_task(blink_led(led, interval_ms))

# Avvia il ciclo di eventi asincroni
loop.run_until_complete(asyncio.gather())

'''