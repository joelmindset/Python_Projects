
class car:
        def __init__(self, carType, make, year, milage):
                self.carType = carType
                self.make = make
                self.year = year
                self.milage = milage
        def carinfo(self):
                print ("Type: " + self.carType, "\nMake: " + self.make, "\nYear: ", self.year, "\nMilage: " , self.milage)
class motor(car):
        def __init__(self, motorType, fuel,  motorMilage, driveType):
                self.motorType = motorType
                self.fuel = fuel
                self.motorMilage = motorMilage
                self.driveType = driveType
        def motorinfo(self):
                print ("Type: ", self.motorType, "\nFuel: ", self.fuel, "\nMilage: " , self.motorMilage, "\nDrive Type: ", self.driveType )
class details(car):
        def __init__(self, color, doorNumber):
                self.color = color
                self.doorNumber = doorNumber
        def detailsinfo(self):
                print("Color: ", self.color, "\nNumber of doors: ", self.doorNumber)

carpart = car("Toyota", "Tacoma", 2020, 5000)
carmot = motor("v8", "Reg", 5000, "4x4")
cardet =  details("blue", 2)

carpart.carinfo()
carmot.motorinfo()
cardet.detailsinfo()

                

