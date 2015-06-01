There are three ants on different vertices of a triangle. 
What is the probability of collision (between any two or all of them) 
if they start walking on the sides of the triangle?
Similarly find the probability of collision with ‘n’ ants on an ‘n’ vertex polygon.


since we have two directions and only three ants
p(clockwise) = (1/2)^3
p(counterclockwise) = (1/2)^3

one direction walk without collision:
p = p(clockwise) + p(counterclockwise) = (1/2)^3 + (1/2)^3 = 1/4
p(collision) = 1 - p(same direction) = 1- (1/4) = 3/4

=> if we have ‘n’ vertex polygon:
p(clockwise) = (1/2)^n
p(counterclockwise) = (1/2)^n

p(collision) = 1 - p(same direction) = 1- (1/2)^(n-1) 




