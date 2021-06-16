# car self type
class car:
        def __init__(self, carType, make, year, milage):
                self.carType = carType
                self.make = make
                self.year = year
                self.milage = milage
        #print all from car
        def carinfo(self):
                print ("Type: " + self.carType, "\nMake: " + self.make, "\nYear: ", self.year, "\nMilage: " , self.milage)
#motor class with parent car
class motor(car):
        def __init__(self, motorType, fuel,  motorMilage, driveType):
                self.motorType = motorType
                self.fuel = fuel
                self.motorMilage = motorMilage
                self.driveType = driveType
        #print all from motor
        def motorinfo(self):
                print ("Type: ", self.motorType, "\nFuel: ", self.fuel, "\nMilage: " , self.motorMilage, "\nDrive Type: ", self.driveType )
#details class with parent car
class details(car):
        def __init__(self, color, doorNumber):
                self.color = color
                self.doorNumber = doorNumber
        #print all from details
        def detailsinfo(self):
                print("Color: ", self.color, "\nNumber of doors: ", self.doorNumber)
#constructors 
carpart = car("Toyota", "Tacoma", 2020, 5000)
carmot = motor("v8", "Reg", 5000, "4x4")
cardet =  details("blue", 2)

carpart.carinfo()
carmot.motorinfo()
cardet.detailsinfo()

                

