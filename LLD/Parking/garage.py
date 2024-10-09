class Garage:
  _instance = None
  def __new__(self):
    if not _instance:
      super().__new__(Garage)
