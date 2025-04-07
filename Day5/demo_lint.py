from abc import ABC, abstractmethod
#Abstract Base class
class chai:
    def __init__(self, name, base_price,  quantity_in_stock):
        self.name = name
        self.base_price = base_price
        self.quantity_in_stock = quantity_in_stock
        
    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def display_info(self):
        pass
        
#Sub Classes
class MasalaChai(chai):
    def calculate_price(self):
        return self.base_price + 10 

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: {self.calculate_price()} | Stock: {self.quantity_in_stock}")
    
class GingerChai(chai):
    def calculate_price(self):
        return self.base_price + 8

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: {self.calculate_price()} | Stock: {self.quantity_in_stock}")

class ElaichiChai(chai):
    def calculate_price(self):
        return self.base_price + 12

    def display_info(self):
        print(f"Name: {self.name} | Price per cup: {self.calculate_price()} | Stock: {self.quantity_in_stock}")

#Main class
class ChaiInventory:
    def __init__(self):
        self.chai_list = []
    
    def Add_Chai(self, obj):
        self.chai_list.append(obj)

    def show_inventory(self):
        for chai in self.chai_list:
            chai.display_info()

    def total_inventory_value(self):
        Total = sum(chai.calculate_price() * chai.quantity_in_stock for chai in self.chai_list)
        return Total

Inventory = ChaiInventory()

chai1 = MasalaChai("Masala Chai", 20,  30)
chai2 = GingerChai("Ginger Chai", 15, 20)
chai3 = ElaichiChai("Elaichi Chai", 30, 25)
        
Inventory.Add_Chai(chai1)
Inventory.Add_Chai(chai2)
Inventory.Add_Chai(chai3)

Inventory.show_inventory()
print("Total Inventory Value: ₹", Inventory.total_inventory_value())

#Your code has been rated at 4.22/10