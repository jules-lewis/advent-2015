'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 20: Infinite Elves and Infinite Houses
------------------------------------------------------------------------------

To keep the Elves busy, Santa has them deliver some presents by hand, 
door-to-door. He sends them down a street with infinite houses numbered 
sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on 
that number:

Elf 1 delivers presents to every house: 1, 2, 3, 4, 5, ....
Elf 2 delivers presents to every second house: 2, 4, 6, 8, 10, ....
Elf 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers 
presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, which 
delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, 
because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 
40 = 70 presents.

What is the lowest house number of the house to get at least as many 
presents as the number in your puzzle input?

Your puzzle input is 29000000.

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

The Elves decide they don't want to visit an infinite number of houses. 
Instead, each Elf will stop after delivering presents to 50 houses. To make 
up for it, they decide to deliver presents equal to eleven times their number 
at each house.

With these changes, what is the new lowest house number of the house to get 
at least as many presents as the number in your puzzle input?

Your puzzle input is still 29000000.

'''

import time
from math import sqrt
from collections import defaultdict

#Timing: Start
start = time.perf_counter()

PUZZLE_INPUT = 29000000

def solve(target, increment, cap):

    houses = defaultdict(int)
    
    for elf in range(1, PUZZLE_INPUT+1):

        if cap: 
            end = min((elf*50)+1, target)
        else:
            end = target

        for house in range (elf, end, elf):
            houses[house] += elf * increment

        if houses[elf] >= PUZZLE_INPUT:
            return elf

#Part 1
print(solve(1000000, 10, False))
#Part 2
print(solve(1000000, 11, True))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
