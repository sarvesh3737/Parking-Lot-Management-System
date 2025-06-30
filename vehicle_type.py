from enum import Enum

class VehicleType(Enum):
    SMALL_CAR = 1      # Small and compact car
    LARGE_CAR = 2      # Full-size car  
    OVERSIZE_VEHICLE = 3  # SUV or Truck

class SlotSize(Enum):
    SMALL = 1
    LARGE = 2
    OVERSIZE = 3