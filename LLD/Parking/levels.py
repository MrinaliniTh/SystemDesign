import random
from spot import Spot
from vehicle_type import VehicleType
from vehicle import Vehicle


class Level:
  def __init__(self, floor_number:int, num_of_spots:int):
    self.floor_number = floor_number
    self.num_of_spots = num_of_spots
    self.available_spots = []
    for spot_no in range(num_of_spots):
      self.available_spots.append(Spot(spot_no, VehicleType=random.choice(list(VehicleType))))

  def park_vehicle(self, vehicle:Vehicle) -> bool:
    for spot_obj in self.available_spots:
      if spot_obj.park_vehicle(vehicle):
        return True
    return False

  def unpark_vehicle(self, vehicle:Vehicle) -> bool:
    for spot_obj in self.available_spots:
      parked_vehicle = spot_obj.get_vehicle()
      if parked_vehicle.vehicle_no == vehicle.vehicle_no:
        spot_obj.unpark_vehicle()
        return True
    return False

  def get_floor_no(self) -> int:
    return self.floor_number

  def display_availibility(self) -> None:
    for spot_obj in self.available_spots:
      if spot_obj.is_availble():
        print("spot number", spot_obj.spot_no)
      
        
        
