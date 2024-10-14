from levels import Level
from vehicle import Vehicle

class Garage:
  _instance = None

  def __new__(self):
    if not _instance:
      super().__new__(Garage)

  def __init__(self, levels:int, no_of_spots:int)->None:
    self.levels = levels
    self.no_of_spots = no_of_spots
    self.available_levels = []
    for level_no in range(self.levels):
      self.available_levels.append(Level(level_no, self.no_of_spots))

  def park_vehicle(self, vehicle:Vehicle) -> bool:
    for level_obj in self.available_levels:
      if level_obj.park_vehicle(vehicle):
        return True
    return False

  def unpark_vehicle(self, vehicle:Vehicle) -> bool:
    for level_obj in self.available_levels:
      if level_obj.unpark_vehicle(vehicle):
        return True

    print("Vehicle not found in the garage")
