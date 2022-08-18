'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 1: NOT QUITE LISP
------------------------------------------------------------------------------

Santa was hoping for a white Christmas, but his weather machine's "snow" 
function is powered by stars, and he's fresh out! To save Christmas, he needs 
you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made 
available on each day in the Advent calendar; the second puzzle is unlocked 
when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he 
can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one 
character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing 
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will 
never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Now, given the same instructions, find the position of the first character 
that causes him to enter the basement (floor -1). The first character in the 
instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the 
basement?

'''

import time

#Timing: Start
start = time.perf_counter()

#Load the puzzle data
with open('src/day01.txt') as f:
    data = f.read()

#Part 1: Seems the simplest way to calculate the floors
floor = data.count('(') - data.count(')')
print(str(floor))

#Part 2: Feels like we need to step through the data
floor = 0
pos = 0
for char in data:
    pos += 1
    if char == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break
print(str(pos))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
