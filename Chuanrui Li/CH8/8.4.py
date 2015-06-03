#Design a parking lot using object oriented principles

#we assume there are two types of cars, s_car and b_car
#The there empty space for them, s space and b space

s_space = 10
b_space = 15

class l_car:
    def __init__(self, ID):
        self.ID = ID

    def l_car_in(self):
        global s_space
        if s_space > 0:
            s_space -= 1
        else:
            print "no more space"

    def l_car_out(self):
        global s_space
        s_space += 1

class s_car():
    def __init__(self, ID):
        self.ID = ID

    def l_car_in(self):
        global b_space
        if b_space > 0:
            b_space -= 1
        else:
            print "no more space"

    def l_car_out(self):
        global b_space
        b_space += 1

s1 = l_car(1)
s2 = l_car(2)

s1.l_car_in()
s1.l_car_in()
s1.l_car_out()
print s_space



