# Parking Lot Management System

A command-line application for managing a parking lot.
Users can specify the total number of slots and manage entry, exit, and status of vehicles of various sizes.
*All data is stored in memory—no database required!*

---

## Features

* **User-defined Slots:** Initialize the parking lot with any number of slots.
* **Slot Size Classification:** Three slot types — Small, Large, Oversize.
* **Vehicle Management:** Park, unpark, and locate vehicles by license plate.
* **Duplicate Prevention:** License plates must be unique within the lot.
* **Real-time Status:** View slot availability for each slot size.
* **Input Validation & Error Handling:** Handles invalid/duplicate entries.

---

## Approach & Design

### Object-Oriented Structure

* **Classes:**

  * `ParkingLot`: Singleton class managing all slots and operations.
  * `ParkingSpot`: Represents a single slot, tracks its type and occupancy.
  * `Vehicle` (abstract) and its subclasses: `SmallCar`, `LargeCar`, `SUV`, `Truck`.
  * Enums for vehicle/slot types for type-safety and clarity.

---

## File Structure

```
parkinglot/
│
├── parking_lot_interactive.py   # Main CLI application (entry point)
├── parking_lot.py               # ParkingLot core logic
├── parking_spot.py              # ParkingSpot class
├── vehicle.py                   # Abstract Vehicle base class
├── car.py                       # SmallCar, LargeCar, SUV, Truck classes
├── vehicle_type.py              # Enums: VehicleType, SlotSize
├── README.md                    # Project documentation
└── info.txt                     # Project requirements/specs
```

---

## How to Run

### Requirements

* Python 3.7 or higher

### Steps

1. **Clone the repo:**

   ```sh
   git clone <your-github-repo-url>
   cd parkinglot
   ```

2. **Run the application:**

   ```sh
   python parking_lot_interactive.py
   ```

3. **Follow on-screen prompts to park/unpark vehicles or view status.**

---

## Example Usage

```
Welcome to Parking Lot Management System!
Enter the total number of parking slots (n): 8

Parking lot initialized with 8 slots:
  Small slots: 4
  Large slots: 2
  Oversize slots: 2

=== PARKING LOT MANAGEMENT SYSTEM ===
1. Park a vehicle
2. Unpark a vehicle
3. Display availability
4. Exit
=====================================
Enter your choice (1-4): 1

Select vehicle type:
1. Small Car
2. Large Car
3. SUV
4. Truck
Enter your choice (1-4): 3
Enter license plate: ABC123

Vehicle ABC123 parked successfully in spot 6
```

---

## Test Data & Expected Results

You can manually test the application interactively. Here is an example test sequence and the expected outcome:

### Test Scenario

1. Initialize with **8 slots**.
2. Park the following vehicles in order:

   * Small Car, License Plate: `S1`
   * Small Car, License Plate: `S2`
   * Large Car, License Plate: `L1`
   * Large Car, License Plate: `L2`
   * SUV, License Plate: `O1`
   * Truck, License Plate: `O2`
3. Try to park another Small Car with plate `S1` (duplicate) — should be rejected.
4. Try to park another SUV (should fail if all oversize slots are filled).
5. Unpark vehicle with license plate `L1`.
6. Park a new Large Car, License Plate: `L3` (should succeed, since a large slot became available).
7. Display availability/status at each step for validation.

### Expected Results

* After step 2, all slot types should be either full or partially full depending on distribution.
* Duplicate parking (`S1`) is not allowed (error message).
* Trying to park an SUV when oversize slots are full should show a "no slots available" message.
* After unparking `L1` and parking `L3`, all large slots should be full again.

#### Example Output Snippet

```
Parking lot initialized with 8 slots:
  Small slots: 4
  Large slots: 2
  Oversize slots: 2

Vehicle S1 parked successfully in spot 0
Vehicle S2 parked successfully in spot 1
Vehicle L1 parked successfully in spot 4
Vehicle L2 parked successfully in spot 5
Vehicle O1 parked successfully in spot 6
Vehicle O2 parked successfully in spot 7

Vehicle with license plate S1 is already parked
No oversize slots available!
Vehicle L1 unparked successfully
Vehicle L3 parked successfully in spot 4

=== PARKING LOT STATUS ===
Small slots: 2/4 available
Large slots: 0/2 available
Oversize slots: 0/2 available
Total vehicles parked: 6
========================
```

---
