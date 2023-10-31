# ***************************************************************
# Name : coupon_calculations.py
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

# Constants for shipping rates and tax rate
SHIPPING_RATES = {
    0: 5.95,
    10: 5.95,
    30: 7.95,
    50: 11.95
}
TAX_RATE = 0.06

# Prompt the user for input
price = float(input("Enter the item price: $"))
cash_coupon = float(input("Enter the cash coupon amount ($5 or $10): $"))
percent_coupon = float(input("Enter the percent coupon (10%, 15%, or 20%): "))

# Apply cash coupon
if cash_coupon == 5 or cash_coupon == 10:
    cash_off_subtotal = price - cash_coupon
else:
    print("Invalid cash coupon amount. No cash coupon applied.")
    cash_off_subtotal = price  # Set to the original price if no valid cash coupon

# Calculate the discount based on percent coupon
if percent_coupon == 10:
    percent_discount = cash_off_subtotal * 0.10
elif percent_coupon == 15:
    percent_discount = cash_off_subtotal * 0.15
elif percent_coupon == 20:
    percent_discount = cash_off_subtotal * 0.20
elif percent_coupon == 30:
    percent_discount = cash_off_subtotal * 0.30
else:
    percent_discount = 0

# Calculate the subtotal after applying percent discount
subtotal_after_percent = cash_off_subtotal - percent_discount

# Calculate shipping cost
shipping_cost = 0

# Check if the subtotal after percent discount is greater than $10 to apply shipping cost
if subtotal_after_percent > 0:
    for threshold, rate in SHIPPING_RATES.items():
        if subtotal_after_percent <= threshold:
            shipping_cost = rate
            break

# Calculate tax amount
tax_amount = subtotal_after_percent * TAX_RATE

# Calculate the total order amount
total_amount = subtotal_after_percent + tax_amount + shipping_cost

# Display the result
print(f"Subtotal after cash coupon: ${cash_off_subtotal:.2f}")
print(f"Subtotal after percent discount: ${subtotal_after_percent:.2f}")
print(f"Shipping cost: ${shipping_cost:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total order amount: ${total_amount:.2f}")