class Vehicle:

    def __init__(self, vehicle_id, brand, model, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.is_available = True


    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rent Per Day:", self.rent_per_day)
        print("Available:", self.is_available)

    
    def calculate_rent(self, days):
       return self.rent_per_day * days


    def rent_vehicle(self):
        if not self.is_available:
            print("Vehicle is already rented.")
            return

        self.is_available = False
        print("Vehicle rented successfully.")

    def return_vehicle(self):
        if self.is_available:
            print("Vehicle is already available.")
            return

        self.is_available = True
        print("Vehicle returned successfully.")


car = Vehicle(101, "Zuzuki", "Fronx", 3000)     
car.display_details()
cost = car.calculate_rent(5)
print("Rental Cost:", cost)

class Car(Vehicle):

    def calculate_rent(self, days):
        return self.rent_per_day * days + 500

A = Car(102, "Toyota", "Camry", 4000)
A.display_details()
cost = A.calculate_rent(5)
print("Car Rental Cost:", cost)

class Bike(Vehicle):

    def calculate_rent(self, days):
        return self.rent_per_day * days + 100

B = Bike(103, "Yamaha", "R1", 2000)
B.display_details()
cost = B.calculate_rent(5)
print("Bike Rental Cost:", cost)

class Truck(Vehicle):

    def calculate_rent(self, days):
        return self.rent_per_day * days + 1000

C = Truck(104, "Volvo", "FH16", 6000)
C.display_details()
cost = C.calculate_rent(5)
print("Truck Rental Cost:", cost)


A.rent_vehicle()
B.rent_vehicle()
A.return_vehicle()




class Customer:

    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def display_details(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Phone:", self.phone)



customer1 = Customer(1, "Anu", "9876543210")

customer1.display_details()



class Rental:

    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total_cost = vehicle.calculate_rent(days)

    def display_rental_details(self):
        print("\n===== Rental Details =====")
        print("Customer:", self.customer.name)
        print("Vehicle:", self.vehicle.brand, self.vehicle.model)
        print("Rental Days:", self.days)
        print("Total Rental Cost:", self.total_cost)


A = Car(105, "Toyota", "Camry", 3000)

customer1 = Customer(2, "Suk", "9446543210")

A.rent_vehicle()

rental1 = Rental(customer1, A, 5)

rental1.display_rental_details()

A.return_vehicle()        