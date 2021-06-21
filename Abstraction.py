

from abc import ABC, abstractmethod

#inventory and pass in an argument unknown data
class inventory(ABC):
    def disInventory(self, amount):
        print("Total Inventory: ", amount)
    @abstractmethod
    def total(self, amount):
        pass

#class total inventory and how much it should be with parent class
class totalInventory(inventory):
    def total(self,amount):
        print('You have {} your total amount should be 30'.format(amount))

obj = totalInventory()
obj.disInventory(25)
obj.total('25')