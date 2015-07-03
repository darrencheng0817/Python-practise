#Write a method to count the number of 2s between 0 and n.

def counter(n):
	sum3 = 0
	while n != 0:
		#print n
		if n %10 == 2:
			sum3 += 1
		n = n/10
	return sum3


def main():
	n = 102
	i = 0
	sum2 = 0
	while i <= n:
		sum2 += counter(i)
		i+=1
	print sum2
if __name__ == "__main__":
	main()
