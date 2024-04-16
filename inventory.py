import sys  # Importing the sys module for system-specific parameters and functions.

class Inventory:
    def __init__(self,
                 category=None,  # Initializing category as None (default value).
                 c_technology=None,  # Initializing c_technology as None (default value).
                 c_home=None,  # Initializing c_home as None (default value).
                 c_health=None,  # Initializing c_health as None (default value).
                 incoming_shipping=None,  # Initializing incoming_shipping as None (default value).
                 pending_sales=None,  # Initializing pending_sales as None (default value).
                 chosen_category=None,  # Initializing chosen_category as None (default value).
                 item=None,  # Initializing item as None (default value).
                 ask=None,  # Initializing ask as None (default value).
                 sell_list=None,  # Initializing sell_list as None (default value).
                 restock_list=None  # Initializing restock_list as None (default value).
                 ):
        self.sell_list = sell_list  # Assigning the sell_list parameter to the instance variable sell_list.
        self.restock_list = restock_list  # Assigning the restock_list parameter to the instance variable restock_list.
        self.ask = ask  # Assigning the ask parameter to the instance variable ask.
        self.category = category  # Assigning the category parameter to the instance variable category.
        self.c_technology = c_technology  # Assigning the c_technology parameter to the instance variable c_technology.
        self.c_home = c_home  # Assigning the c_home parameter to the instance variable c_home.
        self.c_health = c_health  # Assigning the c_health parameter to the instance variable c_health.
        self.incoming_shipping = incoming_shipping  # Assigning the incoming_shipping parameter to the instance variable incoming_shipping.
        self.pending_sales = pending_sales  # Assigning the pending_sales parameter to the instance variable pending_sales.
        self.chosen_categoty = chosen_category  # Assigning the chosen_category parameter to the instance variable chosen_categoty.
        self.item = item  # Assigning the item parameter to the instance variable item.
        self.sell_list = []  # Initializing sell_list as an empty list.
        self.restock_list = []  # Initializing restock_list as an empty list.
        
        self.category = ["Technology Items", "Home Items", "Health Items"]  # Assigning a list of categories to the category variable.
        self.c_technology = [# Initializing c_technology with a list of dictionaries containing technology items.
    {
        "Product": "Smart Speaker",
        "Description": "A voice-activated assistant for your home, offering music playback, smart home control, and information access.",
        "Price": 99,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Wireless Earbuds",
        "Description": "True wireless earbuds with noise-canceling technology and long battery life.",
        "Price": 149,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Gaming Console",
        "Description": "High-performance gaming console with 4K graphics, HDR support, and a vast library of games.",
        "Price": 399,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Fitness Tracker",
        "Description": "Wearable fitness tracker with heart rate monitoring, activity tracking, and sleep analysis.",
        "Price": 79,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Robot Vacuum",
        "Description": "Smart robotic vacuum cleaner with mapping technology and app control for efficient cleaning.",
        "Price": 249,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Action Camera",
        "Description": "Compact action camera with 4K video recording, waterproof design, and image stabilization.",
        "Price": 199,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Smartwatch",
        "Description": "Multi-functional smartwatch with fitness tracking, notifications, GPS, and customizable watch faces.",
        "Price": 249,
        "Quantity": 20  # Set the default Quantity to 20
    }
]

        
        self.c_home = [# Initializing c_home with a list of dictionaries containing home items.
    {
        "Product": "Garden Kit",
        "Description": "Beginner-friendly indoor garden kit with herbs, seeds, and automated watering system.",
        "Price": 79,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "LED Lights",
        "Description": "Smart LED lights with customizable colors, schedules, and energy-saving features.",
        "Price": 29,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Smart Lock",
        "Description": "Keyless smart lock system with app control, guest access, and activity logs.",
        "Price": 149,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Home Gym",
        "Description": "Compact home gym equipment set with resistance bands, dumbbells, and exercise guides.",
        "Price": 199,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Cleaning Kit",
        "Description": "Eco-friendly cleaning kit with natural cleaning solutions, reusable cloths, and bamboo scrubbers.",
        "Price": 29,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Wall Art",
        "Description": "Modern wall art prints on canvas with abstract designs and vibrant colors.",
        "Price": 69,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Art Frame",
        "Description": "Digital art frame with high-resolution display, Wi-Fi connectivity, and curated art collections.",
        "Price": 299,
        "Quantity": 20  # Set the default Quantity to 20
    }
]

        self.c_health = [# Initializing c_health with a list of dictionaries containing health items.
    {
        "Product": "Yoga Mat",
        "Description": "High-quality yoga mat with non-slip surface and eco-friendly materials.",
        "Price": 49,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Meditation App",
        "Description": "Guided meditation app with calming sessions and mindfulness exercises.",
        "Price": 4,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Fitness App",
        "Description": "Personalized fitness app with workout routines, progress tracking, and nutrition plans.",
        "Price": 4,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Massage Chair",
        "Description": "Luxurious massage chair with Shiatsu massage, heat therapy, and zero-gravity recline.",
        "Price": 1499,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Sleep Tracker",
        "Description": "Advanced sleep tracker wearable with sleep stages analysis, sleep score, and personalized insights.",
        "Price": 129,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Meal Planner",
        "Description": "AI-powered meal planner app with recipe suggestions, grocery lists, and nutritional information.",
        "Price": 5,
        "Quantity": 20  # Set the default Quantity to 20
    },
    {
        "Product": "Wellness Tea",
        "Description": "Organic wellness tea blend with immune-boosting herbs and antioxidants.",
        "Price": 12,
        "Quantity": 20  # Set the default Quantity to 20
    }
]

    def menu(self):  # Defining a method named menu.
        while True:  # Starting an infinite loop.
           print()  # Printing a blank line.
           print("Product Inventory Manager")  # Printing a message.
           print("Choose Functionality:")  # Printing a message.
           print("1.View Items")  # Printing a message.
           print("2.Sell Item")  # Printing a message.
           print("3.Restock Item")  # Printing a message.
           print("4.View Incoming Shipments")  # Printing a message.
           print("5.Exit Program")  # Printing a message.
           choice = input("Enter your choice:1-5:")  # Taking user input for choice.
           if choice == '1':  # Checking if the choice is '1'.
               self.view_items()  # Calling the view_items method.
           elif choice == '2':  # Checking if the choice is '2'.
               self.sell_item()  # Calling the sell_item method.
           elif choice == '3':  # Checking if the choice is '3'.
               self.order_item()  # Calling the order_item method.
           elif choice == '4':  # Checking if the choice is '4'.
               self.view_shipments()  # Calling the view_shipments method.
           elif choice =='5':  # Checking if the choice is '5'.
               sys.exit()  # Exiting the program.
           else:  # Executing if none of the above conditions are met.
               print("Invalid Choice: Try again.")  # Printing a message.
            
    def view_items(self):  # Defining a method named view_items.
        print("Item Categories:")  # Printing a message.
        print("1.Technology Items")  # Printing a message.
        print("2.Home Items")  # Printing a message.
        print("3.Health Items")  # Printing a message.
        self.chosen_categoty = input("Choose Category:1-3:")  # Taking user input for chosen category.
        print()  # Printing a blank line.
        print()  # Printing a blank line.
        if self.chosen_categoty == '1':  # Checking if the chosen category is '1'.
            print(self.category[0])  # Printing the first category.
            for item in self.c_technology:  # Looping through technology items.
              print("-" * 20)  # Printing a line of dashes.
              print(f"Product: {item['Product']}")  # Printing product information.
              print(f"Description: {item['Description']}")  # Printing description information.
              print(f"Price: {item['Price']}")  # Printing price information.
              print(f"Quantity: {item['Quantity']}")  # Printing quantity information.
              print("-" * 20)  # Printing a line of dashes.
        elif self.chosen_categoty == '2':
            print(self.category[1])
            for item in self.c_home:
              print("-" * 20)
              print(f"Product: {item['Product']}")
              print(f"Description: {item['Description']}")
              print(f"Price: {item['Price']}")
              print(f"Quantity: {item['Quantity']}")
              print("-" * 20)  # Separate items with a line of dashes\
        elif self.chosen_categoty == '3':
            print(self.category[2])
            for item in self.c_health:
              print("-" * 20)
              print(f"Product: {item['Product']}")
              print(f"Description: {item['Description']}")
              print(f"Price: {item['Price']}")
              print(f"Quantity: {item['Quantity']}")
              print("-" * 20)  # Separate items with a line of dashes\
                  
    def print_item(self):  # Defining a method named print_item.
        print("-" * 20)  # Printing a line of dashes.
        print(f"Product: {self.item['Product']}")  # Printing product information.
        print(f"Description: {self.item['Description']}")  # Printing description information.
        print(f"Price: {self.item['Price']}")  # Printing price information.
        print(f"Quantity: {self.item['Quantity']}")  # Printing quantity information.
        print("-" * 20)  # Printing a line of dashes.
        
    def sell_item(self):  # Defining a method named sell_item.
       print()  # Printing a blank line.
       print("Selling Function")  # Printing a message.
       self.view_items()  # Calling the view_items method.
       cat = int(input("Choose Product:1-7:"))  # Taking user input for product choice.
       print("Selected Item:")  # Printing a message.
       if self.chosen_categoty == '1':  # Checking if the chosen category is '1'.
           self.item = self.c_technology[cat - 1]  # Assigning the selected item to self.item.
           self.quantity_checker()  # Calling the quantity_checker method.
           self.print_item()  # Calling the print_item method.
           self.ask = int(input(f"How many {self.item['Product']} do you want to sell?:"))  # Taking user input for quantity.
           self.item['Quantity'] -= self.ask  # Updating item quantity.
           self.c_technology[cat - 1] = self.item  # Updating item in the technology list.
           print("Item was added to the shipment!")  # Printing a message.
           self.add_shipment("Sell",self.item['Product'],self.ask)  # Calling the add_shipment method.
       elif self.chosen_categoty == '2':
           self.item = self.c_home[cat - 1]
           self.print_item()
           self.ask = int(input(f"How many {self.item['Product']} do you want to sell?:"))
           self.item['Quantity'] -= self.ask
           self.c_home[cat - 1] = self.item
           print("Item was added to the shipment!")
           self.add_shipment("Sell",self.item['Product'],self.ask)
       elif self.chosen_categoty == '3':
           self.item = self.c_health[cat - 1]
           self.print_item()
           self.ask = int(input(f"How many {self.item['Product']} do you want to sell?:"))
           self.item['Quantity'] -= self.ask
           self.c_home[cat - 1] = self.item
           print("Item was added to the shipment!")
           self.add_shipment("Sell",self.item['Product'],self.ask)
       self.check_stock()
       
    def order_item(self):  # Method to order or restock items.
        print()
        print("Order Stocks Function")  # Print a message indicating the start of the order process.
        self.view_items()  # Display available items.
        cat = int(input("Choose Product:1-7:"))  # Get user input for the chosen product.
        print("Selected Item:")  # Print a message indicating the selected item.
        if self.chosen_categoty == '1':  # Check if the chosen category is '1' (Technology Items).
           self.item = self.c_technology[cat - 1]  # Assign the selected item from the technology category.
           self.print_item()  # Print details of the selected item.
           self.ask = int(input(f"How many {self.item['Product']} do you want to Order?"))  # Get user input for the quantity to order.
           self.item['Quantity'] += self.ask  # Update the quantity of the item in inventory.
           self.c_technology[cat - 1] = self.item  # Update the item in the technology category list.
           print("Item was added to the shipment!")  # Print a confirmation message.
           self.add_shipment("Restock", self.item['Product'], self.ask)  # Add the item to the restock list.
           
        elif self.chosen_categoty == '2':
           self.item = self.c_home[cat - 1]
           self.print_item()
           self.ask = int(input(f"How many {self.item['Product']} do you want to Order?"))
           self.item['Quantity'] += self.ask
           self.c_home[cat - 1] = self.item
           print("Item was added to the shipment!")
           self.add_shipment("Restock",self.item['Product'],self.ask)
           
        elif self.chosen_categoty == '3':
           self.item = self.c_health[cat - 1]
           self.print_item()
           self.ask = int(input(f"How many {self.item['Product']} do you want to Order?"))
           self.item['Quantity'] += self.ask
           self.c_home[cat - 1] = self.item
           print("Item was added to the shipment!")
           self.add_shipment("Restock",self.item['Product'],self.ask)
        
    def view_shipments(self):  # Method to view shipments (sold items or restocked items).
        print()
        print("Shipments Viewer")  # Print a message indicating the start of the shipments view.
        print("Category")
        print("1. Selling Shipment")  # Print option to view sold items.
        print("2. Ordering/Restocking Shipment")  # Print option to view restocked items.
        ask = input("Choose Category:(1-2):")  # Get user input for the chosen category.
        if ask == '1':
            num = 1
            for item in self.sell_list:
                print()
                print(f"Sold Item # {num}")
                print(f"Product Name:{item['Product']}")
                print(f"Quantity:{item['Quantity']}")
                num += 1
        if ask == '2':
            num = 1
            for item in self.restock_list:
                
                print()
                print(f"Ordered/Restocked Item # {num}")
                print(f"Product Name:{item['Product']}")
                print(f"Quantity:{item['Quantity']}")
                num += 1
                
                
    def add_shipment(self,category,item_name,quantity):# Method to add an item to the shipment list.
        if category == "Sell": # Check if the category is for selling items.
            item = {# Create a dictionary representing the item.
                "Product":item_name,
                "Quantity":quantity
            }
            self.sell_list.append(item) # Add the item to the sell list.
            
        elif category == "Restock":# Check if the category is for restocking items.
            item = {  # Create a dictionary representing the item.
                "Product":item_name,
                "Quantity":quantity
            }
            self.restock_list.append(item)# Add the item to the restock list.
            
    def check_stock(self):# Method to check if the stock level of an item is low.
        if self.item['Quantity'] <= 5: # Check if the quantity of the item is less than or equal to 5.
            print(f"{self.item['Product']} stocks is low! Please Restock!")  # Print a message indicating low stock.
   
            
    def quantity_checker(self): # Method to check if the quantity of an item is zero.
        if self.item['Quantity'] == 0: # Check if the quantity of the item is zero.
            print("Restock Item First!")# Print a message indicating that the item needs restocking.
            self.menu()# Go back to the main menu
    
            
start = Inventory() #instantiate Inventory
start.menu() #call menu method to start the prorgam

