from abc import ABC, abstractmethod

# Base class
class Building(ABC):
    def __init__(self, location, size, floors):
        self.location = location
        self.size = size
        self.floors = floors
        self.doors_open = False

    def open_doors(self):
        if not self.doors_open:
            self.doors_open = True
            print(f"The doors at {self.location} are now open.")
        else:
            print(f"The doors at {self.location} are already open.")

    def close_doors(self):
        if self.doors_open:
            self.doors_open = False
            print(f"The doors at {self.location} have been closed.")
        else:
            print(f"The doors at {self.location} are already closed.")

    def get_location(self):
        return self.location

    def get_size(self):
        return self.size

    def get_floors(self):
        return self.floors

    @abstractmethod
    def operate(self):
        pass

# Subclass - Residential House
class ResidentialHouse(Building):
    def __init__(self, location, size, floors, bedrooms):
        super().__init__(location, size, floors)
        self.bedrooms = bedrooms
        self.has_garden = False

    def operate(self):
        print(f"This {self.size} sqr meter {self.floors}-storey house at {self.location} is a residential house.")

    def ring_doorbell(self):
        print("Ding-dong! Someone is at the door." if not self.doors_open else "Ding-dong! Someone is at the open door.")

    def plant_garden(self):
        self.has_garden = True
        print(f"A garden has been planted at the back of the {self.floors}-storey house at {self.location}.")

    def hold_party(self):
        self.open_doors()
        print(f"Party at {self.location}! All {self.bedrooms} rooms at the {self.floors}-storey house are ready for guests.")

# Subclass - Hospital
class Hospital(Building):
    def __init__(self, location, size, floors, departments):
        super().__init__(location, size, floors)
        self.departments = departments
        self.emergency_cases = 0

    def operate(self):
        print(f"{self.location} running with {len(self.departments)} departments.")

    def emergency_alert(self):
        print(f"Emergency! Staff at {self.location} report to emergency stations.")
        self.open_doors()

    def admit_patient(self, emergency=False):
        if emergency:
            self.emergency_cases += 1
            print(f"Emergency patient admitted! Total emergencies today: {self.emergency_cases}")
        else:
            print("Regular patient admitted.")

    def conduct_rounds(self):
        print(f"Doctors are making rounds in {len(self.departments)} departments.")
        self.close_doors()

# Subclass - School
class School(Building):
    def __init__(self, location, size, floors, students):
        super().__init__(location, size, floors)
        self.students = students
        self.extracurriculars = []

    def operate(self):
        print(f"{self.location} is open with {self.students} students.")

    def start_classes(self):
        print(f"Classes started for {self.students} students.")
        self.close_doors()

    def add_extracurricular(self, activity):
        self.extracurriculars.append(activity)
        print(f"Added {activity} as an extracurricular activity.")

    def hold_assembly(self):
        self.open_doors()
        print(f"Assembly in progress at {self.location}.")
        if self.extracurriculars:
            print(f"Today's highlight: {self.extracurriculars[-1]}")

# Subclass - Convenience Store
class ConvenienceStore(Building):
    def __init__(self, location, size, floors, open_24_7):
        super().__init__(location, size, floors)
        self.open_24_7 = open_24_7
        self.inventory = {}

    def operate(self):
        status = "open 24/7" if self.open_24_7 else "following regular hours"
        print(f"{self.location} is {status}.")

    def make_sale(self):
        print("Sale processed." if self.doors_open else "Store closed. Sale not allowed.")

    def add_inventory(self, item, quantity):
        self.inventory[item] = self.inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item}(s) to inventory.")

    def check_stock(self, item):
        if item in self.inventory:
            print(f"{item} stock: {self.inventory[item]}")
        else:
            print(f"{item} is not available.")

# === Demonstration ===

print("\n" + "="*20 + " RESIDENTIAL HOUSE " + "="*20)
house = ResidentialHouse("Estrada Residence", 150, 2, 3)
house.close_doors()
house.ring_doorbell()
house.operate()
house.plant_garden()
house.hold_party()

print("\n" + "="*20 + " HOSPITAL " + "="*20)
hospital = Hospital("Saint Lex Hospital", 5000, 8, ["Emergency", "Pediatrics", "Surgery"])
hospital.operate()
hospital.emergency_alert()
hospital.admit_patient(emergency=True)
hospital.conduct_rounds()

print("\n" + "="*20 + " SCHOOL " + "="*20)
school = School("Batangas State University", 3000, 3, 500)
school.open_doors()
school.start_classes()
school.operate()
school.add_extracurricular("LAMB INTRAMURALS")
school.hold_assembly()

print("\n" + "="*20 + " CONVENIENCE STORE " + "="*20)
store = ConvenienceStore("ACP MART", 100, 1, True)
store.open_doors()
store.make_sale()
store.operate()
store.add_inventory("Chips", 50)
store.check_stock("Chips")
store.close_doors()
