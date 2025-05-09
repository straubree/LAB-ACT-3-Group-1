# 🏗️ Building Types – OOP Inheritance Project

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

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Run the script with:
   ```bash
   python your_script_name.py
