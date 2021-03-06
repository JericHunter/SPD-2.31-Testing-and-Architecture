# by Kami Bigdely
# Split temporary variable

class Burger:
    PATTY = 70
    PICKLE = 20
    TOMATO = 25 
    LETTUCE = 15 
    BUN = 95 

    def __init__(self, name):
        self.name = name

    def calc_weight(self):
        return 2 * self.PATTY + 4 * self.PICKLE + 3 * self.TOMATO + 2 * self.LETTUCE + 2 * self.BUN

    def get_info(self):
        print(f'{self.name}: {self.calc_weight()} grams')

class SeoulBurger(Burger):
    KIMCHI = 30
    MAYO = 5

    def __init__(self, name):
        super().__init__(name)

    def calc_weight(self):
        return super().calc_weight() + self.KIMCHI + self.MAYO

ny_burger = Burger('NY Burger').get_info()
seoul_burger = SeoulBurger('Seoul Kimchi Burger').get_info()