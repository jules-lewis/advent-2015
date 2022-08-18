'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 3: Perfectly Spherical Houses in a Vacuum
------------------------------------------------------------------------------

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and 
then an elf at the North Pole calls him via radio and tells him where to move 
next. Moves are always exactly one house to the north (^), south (v), east (>), 
or west (<). After each move, he delivers another present to the house at his 
new location.

However, the elf back at the north pole has had a little too much eggnog, and 
so his directions are a little off, and Santa ends up visiting some houses 
more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to 
the east.

^>v< delivers presents to 4 houses in a square, including twice to the house 
at his starting/ending location.

^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 
2 houses.


------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

The next year, to speed up the process, Santa creates a robot version of 
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents 
to the same starting house), then take turns moving based on instructions 
from the elf, who is eggnoggedly reading from the same script as the previous 
year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa 
goes south.

^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where 
they started.

^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and 
Robo-Santa going the other.




'''

import time

#Timing: Start
start = time.perf_counter()

#Load the puzzle data
with open('src/day03.txt') as f:
    data = f.read().rstrip()

#We're going to use a dictionary, keyed on Santa's X and Y co-ords
def increment_house(x, y, houses):
    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

#Generalised, so we can move more that one character in Part 2
def calc_move(x, y, move):
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '>':
        x += 1
    else:
        x -= 1
    return x, y

#Part 1
santaX = 0
santaY = 0
houses = {}
increment_house(santaX, santaY, houses)
for char in data:
    santaX, santaY = calc_move(santaX, santaY, char)
    increment_house(santaX, santaY, houses)
print(len(houses))

#Part 2
santaX = 0
santaY = 0
robX = 0
robY = 0
houses = {}
increment_house(santaX, santaY, houses)
increment_house(robX, robY, houses)
moveSanta = True
for char in data:
    if moveSanta:
        santaX, santaY = calc_move(santaX, santaY, char)
        increment_house(santaX, santaY, houses)
        moveSanta = False
    else:
        robX, robY = calc_move(robX, robY, char)
        increment_house(robX, robY, houses)
        moveSanta = True
print(len(houses))


#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
