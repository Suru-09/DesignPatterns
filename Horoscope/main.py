from businness.Horoscope import Horoscope
from utils.FactoryType import FactoryType

if __name__ == '__main__':
    h = Horoscope()
    factory_type = int(input("Please enter a factory_type(1 - XML, 2 - SQL): \n"))
    h.execute(FactoryType(factory_type))







