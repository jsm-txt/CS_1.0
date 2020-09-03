#Beginning of code, asks user for burger information
contents = input("What do you want on your burger? ")

#Prints user information to comfirm
print("This is what you want on your burger " + contents)

#Asks user for number of burgers and converts it into an int
numb_burgers = input("How many burgers do you want? ")
numb_burgers = int(numb_burgers) 

#Caluclates burger cost
def calculate(numb_burgers):
    cost = 5
    tax = 1.05
    total = 0
    total_tax = 0
    total = numb_burgers * cost
    total_tax = total * tax
    return(total_tax)

#Calls for burger cost and displays it
total = calculate(numb_burgers)
print(f'Your total is: " {total}')

#Asks user for change and converts it integer
cash = input("How much money do you have? ")
cash = int(cash)

#Calculates change
def change(cash, total):
    change = cash - total
    return (change)

#Calls and prints change
customer_change = change(cash, total)
print(f'"Your change is: " {customer_change}')