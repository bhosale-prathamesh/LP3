items = []
value = 0
capacity = float(input("Enter Bag capacity: ")) 
n = int(input("Number of Items: "))

for i in range(n):
    name, profit, weight = input("Enter item name, profit and weight: ").split(" ")

    profit = float(profit)
    weight = float(weight)
    pwr = float(profit/weight)
    items.append([name,profit,weight,pwr])

items.sort(key=lambda a:a[3],reverse=True)

for i in items:
    if i[2] <= capacity:
        capacity -= i[2]
        value += i[1]
    else:
        value += capacity*i[3]
        break
print("Total Profit: ",value)
