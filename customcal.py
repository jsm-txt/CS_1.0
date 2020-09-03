contents = input("What do you want on your burger? ")

print("This is what you want on your burger " + contents)

numb_burgers = input("How many burgers do you want? ")

numb_burgers = int(numb_burgers) 

def calculate(numb_burgers):
    cost = 5
    tax = 1.05
    total = 0
    total_tax = 0
    total = numb_burgers * cost
    total_tax = total * tax
    return(total_tax)

total = calculate(numb_burgers)

print(f'Your total is: " {total}')

cash = input("How much money do you have? ")
cash = int(cash)

def change(cash, total):
    change = cash - total
    return (change)

customer_change = change(cash, total)

print(f'"Your change is: " {customer_change}')