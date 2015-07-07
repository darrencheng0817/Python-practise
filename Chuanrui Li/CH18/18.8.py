Given a string s and an array of smaller strings T, 
design a method to search s for each small string in T.

def main():
String testString = “mississippi”
String[] stringList = {"is", "sip", "hi", "sis", "mis"}

#APPROACH 
1, hashmap store all the small strings
2, brute force testString and cheak the hashmap for every single step
3, using a new list to receice right step. 
4, the loop can break if number is not found

if __name__ == "__main__":
main()
