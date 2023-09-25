class cocktail:

    def __init__(self, name: str, pumps_sec_list: dict):
        self.name = name
        self.pumps_sec_list = pumps_sec_list

    def __str__(self):
        pumps_str = ", ".join(f"Pump {p}: {s} seconds" for p, s in self.pumps_sec_list.items())
        return f"Name: {self.name}\nPumps and Seconds: {pumps_str}"

    def update_pump(self, n_pump: str, pump_sec: int):
        self.pumps_sec_list[n_pump] = pump_sec

    def delete_pump(self, n_pump: str):
        del self.pumps_sec_list[n_pump]

    def return_recipe(self):
        recipe = []
        for pump in self.pumps_sec_list:
            recipe.append([str(pump), self.pumps_sec_list[pump]])
        print("Recipe of: " + self.name)
        print(recipe)
        return recipe
