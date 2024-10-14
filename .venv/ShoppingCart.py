#Create a Class named ItemToPurchase with the following
#Attributes  item_name (string)  item_price (float)  item_quantity (int)
#Default constructor Initializes item's name = "none", item's price = 0, item's quantity = 0
class ItemToPurchase:
    def __init__(self, item_name = "none", item_description = "none", item_price = 0.0, item_quantity = 0,
                 item_total = 0.0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_total = item_total

#Method print_item_cost()
    def print_item_cost(self):
        print(self.item_name + " " + '{:d}'.format(self.item_quantity) + " @ $" +
              '{:.2f}'.format(self.item_price) + " = $" + '{:.2f}'.format(self.item_total))

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
    def __init__(self, customer_name = "none", current_date = "January 1, 2020", cart_items = [], cart_qty = 0,
                 cart_total = 0.0):
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
        itemFound = False

        for i in self.cart_items:
            if ItemToPurchase.item_name == i.item_name:
                itemFound = True
                updateIndex = self.cart_items.index(i)
                if ItemToPurchase.item_description != "none":
                    self.cart_items[updateIndex].item_description = ItemToPurchase.item_description
                    didChange = True

                if ItemToPurchase.item_price != 0.0:
                    self.cart_items[updateIndex].item_price = ItemToPurchase.item_price
                    didChange = True

                if ItemToPurchase.item_quantity != 0:
                    self.cart_items[updateIndex].item_quantity = ItemToPurchase.item_quantity
                    didChange = True

        if itemFound == False:
            print('Item not found in cart. Nothing modified.')

        if itemFound == True and didChange == False:
            print('Item found in cart, but no changes made.')

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

#Method print_total()
    def print_total(self):
        if len(self.cart_items) > 0:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            self.get_num_items_in_cart()
            print('Number of Items:', self.cart_qty)
            for i in self.cart_items:
                i.find_item_total()
                i.print_item_cost()
            self.get_cost_of_cart()
            print('Total: $' + '{:.2f}'.format(self.cart_total))
        else:
            print('SHOPPING CART IS EMPTY')

#Method print_descriptions()  Outputs each item's description.
    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print("Item Descriptions")
            for i in self.cart_items:
                print(i.item_name + ": "+ i.item_description)
        else:
            print('SHOPPING CART IS EMPTY')

#Function print_menu()  has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart.
#Each option is representedi
#by a single character. Build and output the menu within the function.
def print_menu(ShoppingCart):
    menuInput = ""
    while menuInput != "q":
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option:")
        menuInput = input()

        if menuInput == "a":
            itemEntry = ItemToPurchase()
            input_item(itemEntry)
            ShoppingCart.add_item(itemEntry)

        elif menuInput == "r":
            itemAddRemove = input('Enter Item to Remove: ')
            ShoppingCart.remove_item(itemAddRemove)
            print()

        elif menuInput == "c":
            itemEntry = ItemToPurchase()
            change_item(itemEntry)
            ShoppingCart.modify_item(itemEntry)

        elif menuInput == "i":
            ShoppingCart.print_descriptions()
            print()

        elif menuInput == "o":
            ShoppingCart.print_total()
            print()

        elif menuInput == "q":
            break

        else:
            print("Invalid entry, please try again")
            print()

#Function input_item  Enter the Item Name, Description, Price, and Quantity for the item.
#Calculate the total item cost
def input_item(ItemToPurchase):
    tempString = ""
    print("Enter the item name:")
    ItemToPurchase.item_name = input()
    print("Enter the item description:")
    ItemToPurchase.item_description = input()
    print("Enter the item price:")
    tempString = input()
    if tempString != "":
        ItemToPurchase.item_price = float(tempString)
    print("Enter the item quantity:")
    tempString = input()
    if tempString != "":
        ItemToPurchase.item_quantity = int(tempString)
    ItemToPurchase.find_item_total()

#Function input_item  Enter the Item Name, Description, Price, and Quantity for the item.
#Calculate the total item cost
def change_item(ItemToPurchase):
    tempString = ""
    print("Enter the name of the item to change:")
    ItemToPurchase.item_name = input()
    print("Enter the new item description, or press enter to leave unchanged:")
    tempString = input()
    if tempString == "":
        ItemToPurchase.item_description = "none"
    else:
        ItemToPurchase.item_description = tempString
    print("Enter the new item price, or press enter to leave unchanged:")
    tempString = input()
    if tempString != "":
        ItemToPurchase.item_price = float(tempString)
    print("Enter the new item quantity, or press enter to leave unchanged:")
    tempString = input()
    if tempString != "":
        ItemToPurchase.item_quantity = int(tempString)
    ItemToPurchase.find_item_total()

#Define objects of the class ShoppingCart()
cart01 = ShoppingCart()

#Add name and date
cart01.customer_name = "John Doe"
cart01.current_date = "February 1, 2020"

#Run the method print_menu(cart01)
print_menu(cart01)
