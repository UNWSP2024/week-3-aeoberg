# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

hotDog = 3.5
chiliDog = 4.5
cheese = 0.5
peppers = 0.75
grilledOnions = 1

meal = float(input('Enter the meal number (1 - hotdog, 2 - chilidog): '))

if meal == 1:
    subtotal = 3.5
elif meal == 2:
    subtotal = 4.5
else:
    print ("Error: Invalid selection")
    exit(1)

extras = float(input('Select the number of the item you would like to add (1 - cheese, 2 - peppers, 3 - grilled onions, 4 - none): '))

if extras == 1:
        subtotal = subtotal + cheese
elif extras == 2:
        subtotal = subtotal + peppers
elif extras == 3:
        subtotal = subtotal + grilledOnions
elif extras == 4:
        subtotal = subtotal
else:
    print ("Error: Invalid selection")
    exit(1)

salesTax = round (subtotal * 0.07, 2)
total = subtotal + salesTax

print (f'Subtotal: ${subtotal:.2f}')
print (f'Sales Tax: ${salesTax:.2f}')
print (f'Total: ${total:.2f}')
