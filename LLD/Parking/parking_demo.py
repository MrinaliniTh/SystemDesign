from garage import Garage
from car import Car
from bike import Bike

def run():
    garage = Garage(4, 10)
    car = Car(12003)
    bike = Bike(12433)
    garage.park_vehicle(car)
    garage.park_vehicle(bike)
    garage.unpark_vehicle(car)
    garage.unpark_vehicle(bike)


if __name__ == "__main__":
    run()