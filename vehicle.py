from abc import ABC
from vehicle_type import VehicleType, SlotSize

class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType, slot_size: SlotSize):
        self.license_plate = license_plate
        self.type = vehicle_type
        self.slot_size = slot_size

    def get_type(self) -> VehicleType:
        return self.type
    
    def get_slot_size(self) -> SlotSize:
        return self.slot_size