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

#Build the ShoppingCart class with the following data attributes and related methods.
#Parameterized constructor, which takes the customer name and date as parameters:
#    Attributes:
#        customer_name (string) - Initialized in default constructor to "none"
#        current_date (string) - Initialized in default constructor to "January 1, 2020"
#        cart_items (list)
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020", cart_items = [], cart_qty = 0, cart_total = 0.0):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        self.cart_qty = cart_qty
        self.cart_total = cart_total

#Method add_item()  Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

#Method remove_item() Removes item from cart_items list. Has a string (an item's name) parameter.
#Does not return anything.  If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, itemRemove):
        didChange = False
        for i in self.cart_items:
            if i.item_name == itemRemove:
                self.cart_items.remove(i)
                didChange = True

        if didChange == False:
            print('Nothing removed.')

#Method modify_item()
#Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
#If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
#If not, modify item in cart.
#If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, ItemToPurchase):
        didChange = False
        makeChange = True
        if ItemToPurchase.item_name == "none" and ItemToPurchase.item_price == 0.0 or ItemToPurchase.item_quantity == 0:
            makeChange = False
            didChange = True
            print('Default values passed, nothing updated')

        if makeChange == True:
            for i in self.cart_items:
                if ItemToPurchase.item_name == i.item_name:
                    updateIndex = self.cart_items.index(i)
                    self.cart_items[updateIndex].item_price = ItemToPurchase.item_price
                    self.cart_items[updateIndex].item_quantity = ItemToPurchase.item_quantity
                    didChange = True

        if didChange == False:
            print('Item not found in cart. Nothing modified.')

#Method get_num_items_in_cart() Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        self.cart_qty = 0
        for i in self.cart_items:
            self.cart_qty += i.item_quantity

#Method get_cost_of_cart()  Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
         self.cart_total = 0.0
         for i in self.cart_items:
             self.cart_total += i.item_price * i.item_quantity


                #Define objects of the class ItemToPurchase()
item01 = ItemToPurchase()
item02 = ItemToPurchase()
cart01 = ShoppingCart()
itemAddRemove = 'none'

#print(cart01.cart_items)

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

cart01.add_item(item01)
print(cart01.cart_items[0].item_name)
print(cart01.cart_items[0].item_price)
print(cart01.cart_items[0].item_quantity)

itemAddRemove = input('Enter Item to Remove: ')
cart01.remove_item(itemAddRemove)
cart01.get_num_items_in_cart()
print('Items in cart: ', cart01.cart_qty)
cart01.get_cost_of_cart()
print('Cost of cart: ', cart01.cart_total)



#input item02 attributes
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

cart01.modify_item(item02)

print(cart01.cart_items[0].item_name)
print(cart01.cart_items[0].item_price)
print(cart01.cart_items[0].item_quantity)



#find total cost and print results
#print("TOTAL COST\n")
#item01.find_item_total()
#item01.print_item_cost()
#item02.find_item_total()
#item02.print_item_cost()
#print("Total: $" + '{:.2f}'.format(item01.item_total + item02.item_total))