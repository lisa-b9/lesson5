class Person:

    def __init__(self, name="Person"):
        self.name = name
class Car:
    def __init__(self, model):
        self.model = model
        self.Passengers = []
    def add_passenger(self, *args):
        for passenger in args:
            self.Passengers.append(passenger)
    def print_passengers_names(self):
        if self.Passengers != []:
            print(f"Names of {self.model} passengers: ")
            for passenger in self.Passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.model}")
Lisa = Person("Lisa")
Alana = Person("Alana")
Lauren = Person ("Lauren")
Aime = Person("Aime")
car = Car("Porsche")
car.add_passenger(Lisa, Alana, Lauren, Aime)
car.print_passengers_names()