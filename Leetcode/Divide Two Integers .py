"""
    #Detail explanation:
    #example: 4, 8, 16, 32
    First iteration:
    temp(divisor): 4 -> 8 -> 16 -> 32
    dividend:      44->36 -> 20 -> stop
    
    Second iteration:
    temp(divisor): 4 -> 8 -> 16
    dividend:      16-> 8 -> stop
    
    Third iteration:
    temp(divisor): 4 -> 8
    dividend:      8-> stop
    
    Forth iteration:
    temp(divisor): 4
    dividend:      stop
    """


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while divisor <= dividend:
            #temp storing one turn incrementing data
            #counter storing one turn num of divisor in the dividend
            
            temp, counter = divisor, 1
            while divisor <= dividend:
                dividend -= temp
                #not quite sure
                result += counter
                #1 -> 2 -> 4 -> 8 ...
                counter << 1
                #if temp = 4, 4->8->16->32
                temp << 1
        #check the sign
        if positive == False:
            result = 0 - result
        
        #check the overflow
        return min(max(-2147483648, result), 2147483647)




print Solution().divide(13, 2)