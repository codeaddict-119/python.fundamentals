from random import randint

class Bus:
    def __init__(self, busNo):
        self.busno = busNo

    def book(self, fro, to):
        print(f"Ticket is booked in bus number: {self.busno} from {fro} to {to}")

    def getstatus(self):
        print(f"Bus no: {self.busno} is functional")

    def getfare(self, fro, to):
        fare = randint(100, 2500)  # just for practice
        print(f"Ticket fare for bus {self.busno} from {fro} to {to} is {fare}")

# object creation
b = Bus(1023001)

# method calls
b.book("Delhi", "Noida")
b.getstatus()
b.getfare("Delhi", "Noida")

