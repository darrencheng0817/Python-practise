#1, screen is stored as a single array of bytes.
#2, width of screen can be divided by 8 pixels or 1 byte
#3, eight consecutive pixels to store in one byte
#4, height of the screen can be derived from 
#---------the width of screen 
#---------the length of a single array  
#---------height = the length of a single array  /  the width of screen
#   --------  -------- --SSSSSS SSSSSSSS SSSSSSSS SSS----- => this is 6 bytes, 8 pixel in each byte
# start byte is 3rd, end byte is 5th
def drawline():
    list1 = []
    width = 6*8 
    x1 = 2*8 + 2
    x2 = 5*8 + 3
    #
    start_offset = x1 % 8 
    start_full_byte = x1 / 8
    if start_offset != 0:
        start_full_byte += 1
    
    end_offset = x2 % 8
    end_full_byte = x2 / 8
    if end_offset != 7:
        end_full_byte -= 1 
    print start_offset, start_full_byte
    
    
    
    
    
drawline()