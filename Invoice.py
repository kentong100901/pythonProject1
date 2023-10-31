# ***************************************************************
# Name : ProgramNameTong
# Author: Than Tong
# Created : * Course: CIS189
# Version: 1.0
# OS: Windows 11
# IDE: Python
# Copyright : This is my own original work
# based onspecifications issued by our instructor
# Description :
#           Input: ADD HERE XXX
#           Ouput: ADD HERE XXX
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.
class Invoice:
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price=None):
        # Constructor to initialize Invoice object
        self.invoice_id = invoice_id  # Invoice ID (required)
        self.customer_id = customer_id  # Customer ID (required)
        self.address = address  # Address (required)
        self.last_name = last_name  # Last Name (required)
        self.first_name = first_name  # First Name (required)
        self.phone_number = phone_number  # Phone Number (required)
        # Dictionary to hold items with their prices (optional, defaults to an empty dictionary)
        self.items_with_price = items_with_price if items_with_price is not None else {}

    def __str__(self):
        # String representation of the Invoice object
        return f"Invoice ID: {self.invoice_id}, Customer ID: {self.customer_id}, Name: {self.first_name} {self.last_name}"

    def __repr__(self):
        # Representation of the Invoice object
        return f"Invoice({self.invoice_id}, {self.customer_id}, {self.address}, {self.last_name}, {self.first_name}, {self.phone_number}, {self.items_with_price})"

    def add_item(self, item):
        # Method to add items and their prices to the invoice
        self.items_with_price.update(item)  # Update the dictionary with the provided items

    def create_invoice(self):
        # Method to generate the invoice with items, total, and tax
        total = sum(self.items_with_price.values())  # Calculate total price of items
        tax = total * 0.135  # Calculate tax assuming a rate of 13.5%

        # Display each item and its price
        for item, price in self.items_with_price.items():
            print(f"{item}.....${price:.2f}")

        # Display tax and total amount including tax
        print(f"Tax......... ${tax:.2f}")
        print(f"Total.......${total + tax:.2f}")

# Driver code to test the Invoice class
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

