import time
# import uasyncio as asyncio
import asyncio


class pump:
    def __init__(self, pin):
        self.pin = pin

    async def on(self, sec: int):
        print(f"Pin {self.pin} is ON ")
        time.sleep(sec)
        await asyncio.sleep(sec)
        print(f"Pin {self.pin} is OFF ")
