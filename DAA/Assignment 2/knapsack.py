from tokenize import Double


items = []
capacity = float(input("Enter Bag capacity: ")) 
n = int(input("Number of Items: "))

for i in range(n):
    name = input("Enter item name: ")
    profit = float(input("Enter profit: "))
    weight = float(input("Enter weight: "))
    pwr = float(profit/weight)
    items.append([name,profit,weight,pwr])

items.sort(key=lambda a:a[3],reverse=True)

