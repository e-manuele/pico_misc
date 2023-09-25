import time


class cocktail_manager:
    def __init__(self, cocktails_list: dict, pumps_list: dict):
        self.cocktails_list = cocktails_list
        self.pumps_list = pumps_list

    def spill(self, cocktail_name: str):
        # return_recipe = [ [1,4] ,[2,5] ]
        print("Spilling")
        cocktail = self.cocktails_list[cocktail_name]
        recipe =  cocktail.return_recipe()
        for pump in recipe:
            print(pump)
            self.pumps_list[pump[0]].on()
        sec =0
        while sec <=  int(cocktail.max_sec()):
            time.sleep(1)
            sec = sec+1
            print("SEC : " +str(sec))
            for pump in recipe:
                if int(pump[1]) == sec:
                    self.pumps_list[pump[0]].off()

    def return_cocktails_list(self):
        return [cocktail for cocktail in self.cocktails_list]


'''
import asyncio
import time

class Pump:
    def __init__(self, pin):
        self.pin = pin

    async def on(self, sec: int):
        print(f"Pin {self.pin} is ON ")
        await asyncio.sleep(sec)
        print(f"Pin {self.pin} is OFF ")

class CocktailMachine:
    def __init__(self, cocktails_list, pumps_list):
        self.cocktails_list = cocktails_list
        self.pumps_list = pumps_list

    async def spill(self, cocktail_name: str):
        print("Spilling")
        recipe = self.cocktails_list.get(cocktail_name)
        if recipe:
            tasks = [self.pumps_list[pump].on(time) for pump, time in recipe]
            await asyncio.gather(*tasks)
        else:
            print(f"Cocktail '{cocktail_name}' not found")

async def main():
    pump1 = Pump(1)
    pump2 = Pump(2)

    cocktails = {
        "Margarita": [(1, 4), (2, 5)],
        "Cosmopolitan": [(1, 3), (2, 4)],
    }

    pumps = {1: pump1, 2: pump2}

    cocktail_machine = CocktailMachine(cocktails, pumps)

    await cocktail_machine.spill("Margarita")

if __name__ == "__main__":
    asyncio.run(main())


'''
