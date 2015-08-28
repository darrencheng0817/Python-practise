#You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j).
#EXAMPLE:
#Input: N = 10000000000, M = 10101, i = 2, j = 6
#Output: N = 10001010100

#1), Convert number into a list of digits: 10000000000, 10101
#2), Start at the begnning point i, add the digit into the N list

N = 10000000000
M = 1023

N = str(N)
M = str(M)
star = 3
end = 5

list1 = []
list2 = []
for i in str(N):
    list1.extend([int(i)])
for j in str(M):
    list2.extend([int(j)])

for index in range(0, len(list1)):
    if index == star:
        #change the value of each point
        while index <= end:
            if index >= len(list2) + star:
                break;
            else:
                list1[-index-1] = list2[-(index-star)-1]
                index += 1
                
print list1
ans = 0
power = 0
for elem in range(1, len(list1)+1):
    ans += list1[len(list1)-elem] * pow(10, power)
    power += 1


print ans

