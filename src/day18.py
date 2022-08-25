'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 18: Like a GIF For Your Yard
------------------------------------------------------------------------------

After the million lights incident, the fire code has gotten stricter: now, 
at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal 
lighting configuration. With so few lights, he says, you'll have to resort 
to animation.

Start by setting your lights to the included initial configuration (your 
puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next 
configuration based on the current one. Each light's next state (either 
on or off) depends on its current state and the current states of the 
eight lights adjacent to it (including diagonals). Lights on the edge 
of the grid might have fewer than eight neighbors; the missing ones always 
count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors 
numbered 1 through 8, and the light marked B, which is on an edge, only 
has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or 
off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off 
otherwise.

A light which is off turns on if exactly 3 neighbors are on, and stays 
off otherwise.

All of the lights update simultaneously; they all consider the same 
current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:

.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:

..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:

..###.
......
..###.
......
.#....
.#....

After 3 steps:

...#..
......
...#..
..##..
......
......

After 4 steps:

......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how 
many lights are on after 100 steps?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

You flip the instructions over; Santa goes on to point out that this is all 
just an implementation of Conway's Game of Life. At least, it was, until you 
notice that something's wrong with the grid of lights you bought: four lights, 
one in each corner, are stuck on and can't be turned off. The example above 
will actually run like this:

Initial state:

##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:

#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:

#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:

#...##
####.#
..##.#
......
##....
####.#

After 4 steps:

#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:

##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, 
but with the four corners always in the on state, how many lights 
are on after 100 steps?

'''

import time
from copy import deepcopy

#Timing: Start
start = time.perf_counter()

LIGHT_ON = '#'
LIGHT_OFF = '.'
PART_2 = True

def turn_on_corners(l_grid):
    l_grid[0+1][0+1] = LIGHT_ON
    l_grid[0+1][99+1] = LIGHT_ON
    l_grid[99+1][0+1] = LIGHT_ON
    l_grid[99+1][99+1] = LIGHT_ON

def animate(grid):
    '''
    Here are the rules:
    
    - A light which is on stays on when 2 or 3 neighbors 
      are on, and turns off otherwise.

    - A light which is off turns on if exactly 3 neighbors 
      are on, and stays off otherwise.
    '''
    #All lights are off in the new grid
    new_grid = deepcopy(empty_grid)
    for x in range(100):
        for y in range(100):

            #Remember, we look up the OLD grid, but plot the NEW
            count = 0
            for dx in range (-1, 2):
                for dy in range (-1, 2):
                    if not ((dx == 0) and (dy == 0)):
                        #Remember there is a border
                        if grid[y+dy+1][x+dx+1] == LIGHT_ON:
                            count += 1
            if grid[y+1][x+1] == LIGHT_ON:
                if count in [2, 3]:
                    new_grid[y+1][x+1] = LIGHT_ON
            else:
                if count == 3:
                    new_grid[y+1][x+1] = LIGHT_ON
    
    if PART_2: turn_on_corners(new_grid)

    return new_grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

#Create an empty grid
cols = [LIGHT_OFF] * 102
row = [LIGHT_OFF] * 102
grid = []
for x in range(102):
    grid.append(deepcopy(row))

#We'll need an empty grid
empty_grid = deepcopy(grid)

# Load the puzzle data
with open('txt/day18.txt') as f:
    row = 0
    for line in f:
        col = 0
        for char in line.strip():
            if char == LIGHT_ON:
                grid[row+1][col+1] = char
            col += 1
        row += 1

if PART_2: turn_on_corners(grid)

for i in range(100):
    grid = animate(grid)
print(sum(row.count(LIGHT_ON) for row in grid))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
