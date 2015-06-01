#Write a method to implement *, - , / operations. You should use only the + operator.

#general tricks for * and /
    # 1), first calculate the value
    # 2), second calculate the sign of the value

def check_sign(num1, num2):
    #this is for checking the input sign
    sign = True
    sign1 = 0
    sign2 = 0
    if num1 < 0:
        num1 = abs(num1)
        sign1 = 1
    if num2 < 0:
        num2 = abs(num2)
        sign2 = 1 
    if sign1 != sign2:
        sign = False
    return sign, num1, num2

#we need to checkout the * operations
def multiple():
    num1 = 5
    num2 = -4
    sum_result = 0
    sign, num1, num2 = check_sign(num1, num2)
    while num2 > 0:
        sum_result += num1
        num2 -= 1
    if sign == False:
        print 0 - sum_result
    else:
        print sum_result

#next we do the / operations
def divide():
    num1 = -24
    num2 = -4
    counter = 0
    sign, num1, num2 = check_sign(num1, num2)
    while num1 > 0:
        num1 = num1 + (-num2)
        counter += 1
    if sign == False:
        print 0 - counter
    else:
        print counter


divide()
