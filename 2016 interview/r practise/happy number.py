#round 1
#Happy number, sum of the power of 2 for each digit == 1 at the end

#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1

def happynum(num):
    #prevent an infinite loop
    numset = set()
    while num != 1 and num not in numset:
        numset.add(num)
        sum = 0
        #sum the new value
        while num > 0:
            digit = pow((num % 10), 2)
            sum += digit
            num = num/10
            
        #iterate the new number
        num = sum
    print numset
    return num == 1
        
print happynum(18)