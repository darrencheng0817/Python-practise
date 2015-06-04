#Write a method to generate the nth Fibonacci number.

def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)



def fab1(n, mem):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mem[n] != 0: #this is used for cache
        return mem[n]
    else:
        mem[n] = fab1(n-1, mem) + fab1(n-2, mem)
        return mem[n]
        
def main():
    n = 7
    mem = [0]*(n+1)
    print fab1(n, mem)
    

if __name__ == "__main__":
    main()






