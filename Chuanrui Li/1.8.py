# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

# input: s1 “waterbottle”     s2 “erbottlewat”
# output: true or false
    
# 1), if the length of s1 and s2 are not equal, then s1 and s2 are not a rotate substring, else go to 2)
# 2), if s3 = s1+s1
# 3), check if s2 is substring of s3 , if yes, true, if no, false
def rotate_string():
    s1 = "waterbottle"
    s2 = "erbottlewat"

    if(len(s1) != len(s2)):
        print "false"
    else:
        s3 = s1 + s1
        if s2 in s3:
            print "true"
        else:
            print "false"
#fast way to check the substring
def check():
    s3 = "waterbottlewaterbottle"
    s1 = "erbottlewat"
    for i in s3:
            print 
            
        
check()
    