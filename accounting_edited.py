

def determine_customer_payment(file_path, melon_cost = 1):
    """ Calculate who has underpaid or overpaid on their order of melons"""

# open file 
    the_file = open(file_path)
# iterate through file lines 
    for line in the_file:
# remove "|" to get a string 
        order = line.split('|')
# get the customers full name, located in index position one 
        customer_full_name = order[1]
# get the quantity of the customer's order, located index position 2. Convert quantity from string to float 
        quantity = float(order[2])
# get the actual price of the customer paid, located index position 3. Convert quantity from string to float 
        price_paid = float(order[3])
# calculate how much the customer should have paid 
        customer_expected = quantity * melon_cost
# if customer has over paid, print "overpaid", their payment, and how much was expected  
        if customer_expected < price_paid:
            print(f"Overpaid: {customer_full_name} paid {price_paid:.2f},",
            f"expected ${customer_expected:.2f}"
            )
# if customer underpaid, print "underpaid", their payment, and how much was expected 
        if customer_expected > price_paid:
            print(f"Underpaid: {customer_full_name} paid {price_paid:.2f},",
            f"expected ${customer_expected:.2f}"
            )
#close the file 
    the_file.close()

#call the function 
determine_customer_payment("customer-orders.txt")