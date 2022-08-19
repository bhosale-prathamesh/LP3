n = int(input("Enter number of characters: "))
l = []
while (n):
    char,freq = input("Enter Character and Frequncy: ").split(" ")
    l.append([char,int(freq)])
    n -= 1
l.sort(key=lambda x: x[1])
print(l)