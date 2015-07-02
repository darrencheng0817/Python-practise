#Write a method which finds the maximum of two numbers. You should not use if- else or any other comparison operator.
#EXAMPLE
#Input: 5, 10
#Output: 10


# reference: https://en.wikipedia.org/wiki/Signed_number_representations

def find_max(a, b):
	c = a - b
	sign = (c >> 31)&(0x1) # last bit is a sign bit, if bit == 1, this is a negtive number, if bit == 0, this is a positive number
	flip = 1^sign
	print sign * b + flip * a


def main():
	a = 40
	b = 1
	find_max(a, b)

if __name__ == "__main__":
	main()
