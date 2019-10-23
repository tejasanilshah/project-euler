n = int(input("Enter the upper limit: ")) - 1

def brute_force(n):
	sum = 0
	for i in range(1,n):
		if(i%3==0 or i%5==0):
			sum = sum + i
	return sum

def sum_of_multiples(i):
	l = n//i
	return i*l*(l+1)/2

print(sum_of_multiples(3)+sum_of_multiples(5)-sum_of_multiples(15))