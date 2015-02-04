n = 600851475143
i = 2

for i in range (2,775147) :
	if n % i == 0:
		n = n / i
		j = i

print (j)
