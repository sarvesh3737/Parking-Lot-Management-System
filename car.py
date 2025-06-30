from vehicle_type import VehicleType, SlotSize
from vehicle import Vehicle

class SmallCar(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.SMALL_CAR, SlotSize.SMALL)

class LargeCar(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.LARGE_CAR, SlotSize.LARGE)

class SUV(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.OVERSIZE_VEHICLE, SlotSize.OVERSIZE)

class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.OVERSIZE_VEHICLE, SlotSize.OVERSIZE)