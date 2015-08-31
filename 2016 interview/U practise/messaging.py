# 第一轮
# 给定一段英文消息，以及一个固定的长度，要求将消息分割成若干条，每条的最后加上页码如 (2/3)，然后每条总长度不超过给定的固定长度。典型的应用场景就是短信发送长消息。
# 经过询问之后得到更多详细要求及假设：
# (1）消息数量尽可能少，不必凑整句，可以在任意空格处分页；
# (2）这个固定长度可能非法，比如某个词很长导致一条消息放不下，要判断并抛出异常；
# (3) 假设空格分割，不会出现连着两个空格的情况。
    
    
#implementation step
#First -> detect the white space, store a list of string 
    #checking the max length, if length exceed the max, return error
#Second -> create an empty list, iterate the loop and add the element in the list and add the number at the end
    
def step(string):
    list1 = []
    
    length = 0
    for x in string.split(' '):
        item = x.strip()
        list1.append(item)
        length += len(item)
    
    maxlength = 16
    
    #-> length
    total = length/maxlength
    if (length%maxlength) != 0:
        total += 1
    
    
    newstring, list2 = "", []
    i = 0
    Pnum = 0
    while i < len(list1)-1:
        #corner cases
        if len(list1[i]) > maxlength-3:
            print "eee"
            return False
        newstring = ""
        #temp and j are used to store the pre step's result
        while i < len(list1):
            temp = newstring
            newstring = newstring + list1[i]
            j = i
            i += 1
            if len(newstring) > maxlength-3:
                break
    
        i = j
        Pnum+=1
    list2.append(temp + str(Pnum) + "/" + str(total))
    #used for adding the last string
    if list1[-1] not in list2[-1]:
        list2.append(list1[-1]+ str(Pnum+1) + "/" + str(total))

print list1
    print list2






def main():
    string = "ewewewewewewe rre www, wede yyyyeeeeeeee"
    step(string)

if __name__ == "__main__":
    main()

