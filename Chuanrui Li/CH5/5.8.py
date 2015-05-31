#1, screen is stored as a single array of bytes.
#2, width of screen can be divided by 8 pixels or 1 byte
#3, eight consecutive pixels to store in one byte
#4, height of the screen can be derived from 
#---------the width of screen 
#---------the length of a single array  
#---------height = the length of a single array  /  the width of screen
#   --------  -------- --SSSSSS SSSSSSSS SSSSSSSS SSS----- => this is 6 bytes, 8 pixel in each byte
# start byte is 3rd, end byte is 5th
# this is only one line representation 6 bytes (width), totally bytes on the screen = 6 bytes (width) * height 


list1 = [0] * 18

def printline():
    global list1 
    breaker = 0
    for i in list1:
        if breaker == 6:
            print "\n"
            breaker = 0
        print i,
        breaker += 1
        

def drawline():
    global list1
    width = 6 
    x1 = 2*8 + 2
    x2 = 2*8 + 3
    y = 2
    #starting point of x1
    start_offset = x1 % 8 
    start_full_byte = x1 / 8
    if start_offset != 0:
        #set the starting point
        list1 [width * y + start_full_byte] = 1
        start_full_byte += 1
    
    #ending point of x2
    end_offset = x2 % 8
    end_full_byte = x2 / 8
    if end_offset != 7:
        #set the starting point
        list1 [width * y + end_full_byte] = 1        
        end_full_byte -= 1 
    print start_full_byte, end_full_byte
    
    
    #set byte for that one line
    cor_x = start_full_byte
    while cor_x <= end_full_byte:
        list1 [width * y + cor_x] = 1
        cor_x += 1
    
       
    printline()
    
    
    
drawline()