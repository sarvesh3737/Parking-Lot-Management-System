from vehicle_type import VehicleType, SlotSize
from vehicle import Vehicle
from typing import Optional

class ParkingSpot:
    def __init__(self, spot_number: int, slot_size: SlotSize):
        self.spot_number = spot_number
        self.slot_size = slot_size
        self.parked_vehicle: Optional[Vehicle] = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if self.is_available() and vehicle.get_slot_size() == self.slot_size:
            self.parked_vehicle = vehicle
        else:
            raise ValueError(f"Invalid slot size or spot already occupied. Vehicle requires {vehicle.get_slot_size()}, spot is {self.slot_size}")

    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None

    def get_slot_size(self) -> SlotSize:
        return self.slot_size

    def get_parked_vehicle(self) -> Optional[Vehicle]:
        return self.parked_vehicle

    def get_spot_number(self) -> int:
        return self.spot_number