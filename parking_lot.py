from typing import List, Set
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import SlotSize

class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.parking_spots: List[ParkingSpot] = []
            self.parked_vehicles: Set[str] = set()  # Track license plates

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def initialize_parking_lot(self, total_slots: int) -> None:
        """Initialize parking lot with user-specified number of slots"""
        try:
            if total_slots <= 0:
                raise ValueError("Total slots must be a positive number")
            
            if total_slots > 10000:
                raise ValueError("Total slots cannot exceed 10,000")
            
            if self.parking_spots:
                raise ValueError("Parking lot already initialized")
            
            # Handle edge case when total_slots = 1
            if total_slots == 1:
                self.parking_spots.append(ParkingSpot(0, SlotSize.SMALL))
                print(f"Parking lot initialized with {total_slots} slot:")
                print(f"  Small slots: 1")
                print(f"  Large slots: 0")
                print(f"  Oversize slots: 0")
                return
            
            # Distribute slots across sizes for N > 1
            small_slots = max(1, total_slots // 2)  # At least 1 small slot
            large_slots = max(1, total_slots // 3)  # At least 1 large slot
            oversize_slots = max(1, total_slots - small_slots - large_slots)  # At least 1 oversize slot
            
            # Adjust if total exceeds
            while small_slots + large_slots + oversize_slots > total_slots:
                if oversize_slots > 1:
                    oversize_slots -= 1
                elif large_slots > 1:
                    large_slots -= 1
                else:
                    small_slots -= 1
            
            # Create parking spots directly
            spot_number = 0
            
            # Create small slots
            for i in range(small_slots):
                self.parking_spots.append(ParkingSpot(spot_number, SlotSize.SMALL))
                spot_number += 1
            
            # Create large slots
            for i in range(large_slots):
                self.parking_spots.append(ParkingSpot(spot_number, SlotSize.LARGE))
                spot_number += 1
            
            # Create oversize slots
            for i in range(oversize_slots):
                self.parking_spots.append(ParkingSpot(spot_number, SlotSize.OVERSIZE))
                spot_number += 1
            
            print(f"Parking lot initialized with {total_slots} slots:")
            print(f"  Small slots: {small_slots}")
            print(f"  Large slots: {large_slots}")
            print(f"  Oversize slots: {oversize_slots}")
            
        except Exception as e:
            raise Exception(f"Failed to initialize parking lot: {e}")

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        try:
            if not vehicle:
                raise ValueError("Vehicle cannot be None")
            
            if not self.parking_spots:
                raise ValueError("Parking lot not initialized")
            
            # Check for duplicate license plate
            if vehicle.license_plate.upper() in self.parked_vehicles:
                print(f"Vehicle with license plate {vehicle.license_plate} is already parked")
                return False
            
            for spot in self.parking_spots:
                if spot.is_available() and spot.get_slot_size() == vehicle.get_slot_size():
                    spot.park_vehicle(vehicle)
                    self.parked_vehicles.add(vehicle.license_plate.upper())
                    print(f"Vehicle {vehicle.license_plate} parked successfully in spot {spot.get_spot_number()}")
                    return True
                    
            # Remove this line to prevent duplicate messages
            # print(f"No suitable parking spot available for vehicle {vehicle.license_plate}")
            return False
            
        except Exception as e:
            print(f"Error parking vehicle: {e}")
            return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        try:
            if not vehicle:
                raise ValueError("Vehicle cannot be None")
            
            if not self.parking_spots:
                raise ValueError("Parking lot not initialized")
            
            for spot in self.parking_spots:
                parked_vehicle = spot.get_parked_vehicle()
                if not spot.is_available() and parked_vehicle and parked_vehicle.license_plate.upper() == vehicle.license_plate.upper():
                    spot.unpark_vehicle()
                    self.parked_vehicles.discard(vehicle.license_plate.upper())
                    print(f"Vehicle {vehicle.license_plate} unparked successfully")
                    return True

            return False
            
        except Exception as e:
            print(f"Error unparking vehicle: {e}")
            return False

    def find_vehicle(self, license_plate: str) -> tuple:
        """Find vehicle by license plate and return (spot_number, vehicle_type)"""
        try:
            for spot in self.parking_spots:
                parked_vehicle = spot.get_parked_vehicle()
                if not spot.is_available() and parked_vehicle and parked_vehicle.license_plate.upper() == license_plate.upper():
                    return spot.get_spot_number(), parked_vehicle.get_type()
            
            return None, None
            
        except Exception as e:
            print(f"Error finding vehicle: {e}")
            return None, None

    def display_availability(self) -> None:
        try:
            if not self.parking_spots:
                print("Parking lot not initialized")
                return
                
            small_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.SMALL)
            large_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.LARGE)
            oversize_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.OVERSIZE)
            
            total_small = sum(1 for spot in self.parking_spots if spot.get_slot_size() == SlotSize.SMALL)
            total_large = sum(1 for spot in self.parking_spots if spot.get_slot_size() == SlotSize.LARGE)
            total_oversize = sum(1 for spot in self.parking_spots if spot.get_slot_size() == SlotSize.OVERSIZE)
            
            print("\n=== PARKING LOT STATUS ===")
            print(f"Small slots: {small_available}/{total_small} available")
            print(f"Large slots: {large_available}/{total_large} available")
            print(f"Oversize slots: {oversize_available}/{total_oversize} available")
            print(f"Total vehicles parked: {len(self.parked_vehicles)}")
            print("========================\n")
            
        except Exception as e:
            print(f"Error displaying availability: {e}")

    def get_total_availability(self) -> dict:
        """Get total availability"""
        try:
            if not self.parking_spots:
                return {"small": 0, "large": 0, "oversize": 0}
                
            small_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.SMALL)
            large_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.LARGE)
            oversize_available = sum(1 for spot in self.parking_spots if spot.is_available() and spot.get_slot_size() == SlotSize.OVERSIZE)
            
            return {
                "small": small_available,
                "large": large_available,
                "oversize": oversize_available
            }
            
        except Exception as e:
            print(f"Error getting availability: {e}")
            return {"small": 0, "large": 0, "oversize": 0}