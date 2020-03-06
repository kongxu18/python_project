"""
继承

"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand, speed, battery, power):
        super().__init__(brand, speed)
        self.battery = battery
        self.power = power


co1 = Car('奔驰', 230)
e01 = Electrocar('byd', 120, 15000, 220)
