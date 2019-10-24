n = int(input("Enter the upper limit: "))

def brute_force(n):
	a = 1
	b = 2
	c = a + b
	sum = b
	while c<n:
		if c%2==0:
			sum = sum + c
		c = a + b
		a = b
		b = c
	return sum

def even_fib(n):
	a = 2
	b = 8
	c = 34
	sum = a + b
	while c < n :
		sum = sum + c
		c = 4*b + a
		a = b
		b = c

	return sum

print(even_fib(n))