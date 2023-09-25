import time
# import uasyncio as asyncio

class pump:
    def __init__(self, pin):
        self.pin = pin

    def on(self):#, sec: int):
        print(f"Pin {self.pin} is ON ")

    def off(self):
        # time.sleep(sec)
        print(f"Pin {self.pin} is OFF ")
