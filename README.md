# Parking Lot Management System

A comprehensive parking lot management system that allows users to manage parking slots with different vehicle types and sizes.

## Features

- **User-Configurable Slots**: Initialize parking lot with "n" slots specified by the user
- **Slot Size Classification**: Three types of parking slots:
  - **Small**: For small and compact cars
  - **Large**: For full-size cars  
  - **Oversize**: For SUVs and trucks
- **Vehicle Management**: Park, unpark, and find vehicles
- **Duplicate Prevention**: No two vehicles can have the same license plate
- **Real-time Status**: Display current availability of all slot types
- **Input Validation**: Comprehensive validation for all user inputs
- **Error Handling**: Robust error handling with user-friendly messages

parkinglot/
│
├── parking_lot_interactive.py   # Main CLI application (entry point)
├── parking_lot.py               # ParkingLot singleton and logic
├── parking_spot.py              # ParkingSpot class
├── vehicle.py                   # Abstract base class for vehicles
├── car.py                       # SmallCar, LargeCar, SUV, Truck classes
├── vehicle_type.py              # Enums: VehicleType, SlotSize
├── README.md                    # Project documentation (this file)
└── info.txt                     # Project requirements/spec
