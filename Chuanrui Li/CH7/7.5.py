# Given two squares on a two dimensional plane, find a line that would cut these two squares in half.

#cases that we have
# there are two cases: 
#first,the middle point of both square are not the same, so we can calculate the slope and find the intersection of 
# the y axis
#second, the middle point of the both squares are the same, we can pick the smaller square and find horizontal line to cut the square

def case1(mid_x):
	print "y = " + str(mid_x)

def case2(slope, x, y):
	b = slope * x - y
	print "y = " + str(slope) + "x + " + str(b)

	
def cases_square():
	#define the square and find the middle point, break into cases
	list1 = [(1,1), (1, 2), (2, 2), (2, 1)] # follow colorwise (x,y)
	#list2 = [(1,1), (1, 2), (2, 2), (2, 1)]
	list2 = [(2,2), (2, 3), (3, 3), (3, 2)]
	#list1 value
	mid_x = (list1[0][0] + list1[2][0]) / 2.0
	mid_y = (list1[0][1]+ list1[1][1]) / 2.0
	print mid_x, mid_y
	#list2 value
	mid_x1 = (list2[0][0] + list2[2][0]) / 2.0
	mid_y1 = (list2[0][1]+ list2[1][1]) / 2.0
	print mid_x1, mid_y1
	if(mid_x == mid_x1 and mid_y == mid_y1):
		case1(mid_x)
	else:
		slope = (mid_y - mid_y1) / (mid_x - mid_x1)
		print slope
		case2(slope, mid_x, mid_y)
cases_square()