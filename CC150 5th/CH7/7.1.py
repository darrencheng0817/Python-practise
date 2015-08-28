#You have a basketball hoop and someone says that you can play 1 of 2 games.
#Game #1: You get one shot to make the hoop.
#Game #2: You get three shots and you have to make 2 of 3 shots.
#If p is the probability of making a particular shot, for which values of p should you pick one game or the other?


#since the we have two options
# 1), s(1,1) => p
# 2), s(2,3) + s(3,3) => p^3 + 3 (1-p) * p^2

#compare the size
# p > 3p^2 - 2p^3 => (2p-1)(p-1) > 0
# because the p value is less than 1, so result is undeterminted.
