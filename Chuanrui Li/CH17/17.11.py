# Write a method to generate a random number between 1 and 7, 
# given a method that generates a random number between 1 and 5 
# (i.e., implement rand7() using rand5()).

5 * rand5() => 0, 5, 10, 15, 20
rand5() => 0, 1, 2, 3, 4

@ 0 - 4
@ 5 - 9
@ 10 - 14
....

def rand7():
    while (true):
        num = 5 * rand5()+ rand5()
        if (num < 21):
            return num % 7


def main():


if __name__ == "__main__":
	main()

