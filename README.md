# 🏗️ Building Types – OOP Inheritance Project

👥 Team Members
- [ESTRADA, AUBREY NICOLE P.]
- [MALINAO, CHRISTOPHER III B.]
- [ALBO, LEX RANDAL B.]
- [ESPLANA, JOHN REI]

## 📌 Overview

This project is a demonstration of **Object-Oriented Programming (OOP)** in Python using an **abstract base class** and multiple **subclasses**. It models different types of buildings—each with specific behaviors and properties—showing how inheritance and abstraction can be used to design scalable systems.

## 🎯 Objectives

- Use Python’s `abc` module to define an abstract base class.
- Implement inheritance through subclasses.
- Ensure each subclass overrides at least one abstract method.
- Demonstrate real-world behavior using objects of the classes.
- Create a class diagram showing relationships and structure.

---

## 🧱 Class Structure

### 🔹 `Building` (Abstract Base Class)
- **Properties**: `location`, `size`, `floors`, `doors_open`
- **Methods**:
  - `open_doors()`
  - `close_doors()`
  - `get_location()`, `get_size()`, `get_floors()`
  - `operate()` – Abstract Method

### 🔹 `ResidentialHouse`
- **Properties**: `bedrooms`, `has_garden`
- **Methods**:
  - `ring_doorbell()`
  - `plant_garden()`
  - `hold_party()`
  - `operate()` – Overrides abstract method

### 🔹 `Hospital`
- **Properties**: `departments`, `emergency_cases`
- **Methods**:
  - `emergency_alert()`
  - `admit_patient(emergency)`
  - `conduct_rounds()`
  - `operate()` – Overrides abstract method

### 🔹 `School`
- **Properties**: `students`, `extracurriculars`
- **Methods**:
  - `start_classes()`
  - `add_extracurricular(activity)`
  - `hold_assembly()`
  - `operate()` – Overrides abstract method

### 🔹 `ConvenienceStore`
- **Properties**: `open_24_7`, `inventory`
- **Methods**:
  - `make_sale()`
  - `add_inventory(item, quantity)`
  - `check_stock(item)`
  - `operate()` – Overrides abstract method

---

## 📈 Class Diagram

The class diagram includes:

- One abstract base class: `Building`
- Four subclasses: `ResidentialHouse`, `Hospital`, `School`, `ConvenienceStore`
- All subclasses inherit from `Building` and override the abstract `operate()` method.

*(See `ClassDiagram.png` or your PlantUML code for reference.)*

---

▶️ How to Run the Program

1. Make sure you have **Python 3** installed on your computer.
2. Save the code into a `.py` file (e.g., `building_system.py`).
3. Open a terminal or command prompt.
4. Run the script using:
   ```bash
   python building_system.py
The program will display outputs simulating the actions of each building type.

## 🙏 Acknowledgement

We would like to express our sincere gratitude to our instructor, Ms. Fatima Marie agdon, for guiding us throughout the development of this project and helping us deepen our understanding of object-oriented programming concepts.

We also extend our thanks to our classmates and peers who shared insights and encouragement during brainstorming and debugging sessions.

This project strengthened our skills in Python, problem-solving, and teamwork—and gave us a better appreciation for how real-world systems can be modeled in code.

Lastly, we acknowledge each team member's effort and dedication in contributing to the success of this project.
