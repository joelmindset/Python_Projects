

class accessCode:
    def __init__(self):
        self._codeProtected = 0

obj = accessCode()
obj._codeProtected = 3756
print(obj._codeProtected)

class Number:
    def __init__(self):
        self.__privateNum = 15
    
    def getNums(self):
        print(self.__privateNum)
    
    def setNums(self, nums):
        self.__privateNum = nums

num = Number()
num.getNums()
num.setNums(2)
num.getNums()



#super
class Worker:

    #constructor private and protected
    def __init__(self, name, age, department):
        self._name = name
        self.__age = age
        self.__department = department

    #private 
    def _displayWorker(self):
        #access private data 
        print("Age: ", self.__age)
        print("Department: ", self.__department)
#derived
class Person(Worker):
    #constructor
    def __init__(self, name, age, department):
        Worker.__init__(self, name, age, department)

    #public function
    def displayDetails(self):

        # accessing protected data members of super class
        print("Name: ",self._name)

        # accessing protected member functions of super
        self._displayWorker()

#objects of class
dude = Person("Bob", 35, "Shipping")

#call public member functions of the class
dude.displayDetails()