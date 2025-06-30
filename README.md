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

## File Structure
parkinglot/
├── parking_lot_interactive.py # Main interactive application
├── parking_lot.py # Core parking lot management class
├── parking_spot.py # Individual parking spot class
├── vehicle.py # Abstract vehicle base class
├── vehicle_type.py # Vehicle and slot size enums
├── car.py # Car vehicle classes (SmallCar, LargeCar, SUV, Truck)
├── parking_lot_demo.py # Demo/example usage
├── README.md # This file
└── info.txt # Project requirements