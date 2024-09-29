#Create a Class named ItemToPurchase with the following
#Attributes  item_name (string)  item_price (float)  item_quantity (int)
#Default constructor Initializes item's name = "none", item's price = 0, item's quantity = 0
class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_total = 0.0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_total = item_total

#Method print_item_cost()
    def print_item_cost(self):
        print(self.item_name + " " + '{:d}'.format(self.item_quantity) + " @ $" +
              '{:.2f}'.format(self.item_price) + " = $" + '{:.2f}'.format(self.item_total) + "\n")

#Method find_item_total()
    def find_item_total(self):
        self.item_total = self.item_quantity * self.item_price

#Define objects of the class ItemToPurchase()
item01 = ItemToPurchase()
item02 = ItemToPurchase()

#input item01 attributes
print("Item 1\n")
print("Enter the item name:\n")
item01.item_name = input()
print()
print("Enter the item price:\n")
item01.item_price = float(input())
print()
print("Enter the item quantity:\n")
item01.item_quantity = int(input())
print()

#input item01 attributes
print("Item 2\n")
print("Enter the item name:\n")
item02.item_name = input()
print()
print("Enter the item price:\n")
item02.item_price = float(input())
print()
print("Enter the item quantity:\n")
item02.item_quantity = int(input())
print()

#find total cost and print results
print("TOTAL COST\n")
item01.find_item_total()
item01.print_item_cost()
item02.find_item_total()
item02.print_item_cost()
print("Total: $" + '{:.2f}'.format(item01.item_total + item02.item_total))