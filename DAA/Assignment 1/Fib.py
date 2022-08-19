import time

def rec_fib(n):
	if n<=1:
		return n
	return (rec_fib(n-1) + rec_fib(n-2))

def ite_fib(n):
	a = 0
	b = 1
	for i in range(n):
		a,b = b,a+b
	return a

n = int(input("Enter n: "))

start = time.time()
print(rec_fib(n))
end = time.time()
time_n = end - start

print("Recursive Time complexity: ",time_n)

start = time.time()
print(ite_fib(n))
end = time.time()
time_n = end - start

print("Iterative Time complexity: ",time_n)
print("Iterative Space complexity: ",4*5,"bytes")
