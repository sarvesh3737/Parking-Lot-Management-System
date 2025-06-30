from parking_lot import ParkingLot
from car import SmallCar, LargeCar, SUV, Truck
import sys

class ParkingLotInteractive:
    def __init__(self):
        try:
            self.parking_lot = ParkingLot()
        except Exception as e:
            print(f"Error initializing parking lot: {e}")
            sys.exit(1)
        
    def get_user_input(self) -> int:
        while True:
            try:
                slots = int(input("Enter the total number of parking slots (n): "))
                if slots > 0:
                    return slots
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit(0)
    
    def display_menu(self):
        print("\n=== PARKING LOT MANAGEMENT SYSTEM ===")
        print("1. Park a vehicle")
        print("2. Unpark a vehicle")
        print("3. Display availability")
        print("4. Exit")
        print("=====================================")
    
    def get_license_plate(self) -> str:
        """Get and validate license plate input"""
        while True:
            license_plate = input("Enter license plate: ").strip()
            if not license_plate:
                print("License plate cannot be empty.")
                continue
            
            # Basic length check
            if len(license_plate) < 3:
                print("License plate must be at least 3 characters long.")
                continue
            
            if len(license_plate) > 10:
                print("License plate cannot exceed 10 characters.")
                continue
            
            # Check for valid characters
            if not license_plate.replace(" ", "").replace("-", "").isalnum():
                print("License plate can only contain letters, numbers, spaces, and hyphens.")
                continue
            
            return license_plate.upper()
    
    def park_vehicle_menu(self):
        try:
            print("\nSelect vehicle type:")
            print("1. Small Car")
            print("2. Large Car")
            print("3. SUV")
            print("4. Truck")
            
            choice = input("Enter your choice (1-4): ").strip()
            if not choice:
                print("Please enter a valid choice.")
                return
            
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice! Please select 1-4.")
                return
            
            # Check availability first
            availability = self.parking_lot.get_total_availability()
            
            if choice == "1" and availability["small"] == 0:
                print("No small slots available!")
                return
            elif choice == "2" and availability["large"] == 0:
                print("No large slots available!")
                return
            elif choice == "3" and availability["oversize"] == 0:
                print("No oversize slots available!")
                return
            elif choice == "4" and availability["oversize"] == 0:
                print("No oversize slots available!")
                return
            
            # If slots are available, then ask for license plate
            license_plate = self.get_license_plate()
            
            vehicle = None
            if choice == "1":
                vehicle = SmallCar(license_plate)
            elif choice == "2":
                vehicle = LargeCar(license_plate)
            elif choice == "3":
                vehicle = SUV(license_plate)
            elif choice == "4":
                vehicle = Truck(license_plate)
            
            if vehicle:
                success = self.parking_lot.park_vehicle(vehicle)
                if not success:
                    print(f"Failed to park vehicle {license_plate}.")
                    
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error parking vehicle: {e}")

    def unpark_vehicle_menu(self):
        try:
            license_plate = input("Enter license plate to unpark: ").strip()
            if not license_plate:
                print("License plate cannot be empty.")
                return
            
            # Create a dummy vehicle for searching
            dummy_vehicle = SmallCar(license_plate)
            success = self.parking_lot.unpark_vehicle(dummy_vehicle)
            if not success:
                print(f"Vehicle with license plate {license_plate} not found in parking lot.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"Error unparking vehicle: {e}")
    
    def run(self):
        try:
            print("Welcome to Parking Lot Management System!")
            total_slots = self.get_user_input()
            
            try:
                self.parking_lot.initialize_parking_lot(total_slots)
            except Exception as e:
                print(f"Error initializing parking lot: {e}")
                return
            
            while True:
                try:
                    self.display_menu()
                    choice = input("Enter your choice (1-4): ").strip()
                    
                    if choice == "1":
                        self.park_vehicle_menu()
                    elif choice == "2":
                        self.unpark_vehicle_menu()
                    elif choice == "3":
                        self.parking_lot.display_availability()
                    elif choice == "4":
                        print("Thank you for using Parking Lot Management System!")
                        break
                    else:
                        print("Invalid choice! Please try again.")
                        
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    
        except KeyboardInterrupt:
            print("\nExiting...")
        except Exception as e:
            print(f"Fatal error: {e}")

if __name__ == "__main__":
    try:
        app = ParkingLotInteractive()
        app.run()
    except Exception as e:
        print(f"Failed to start application: {e}")
        sys.exit(1)