'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 9: All in a Single Night ---
------------------------------------------------------------------------------

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have 
provided him the distances between every pair of locations. He can start and 
end at any two (different) locations he wants, but he must visit each 
location exactly once. What is the shortest distance he can travel to achieve 
this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer 
is 605 in this example.

What is the distance of the shortest route?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

The next year, just to show off, Santa decides to take the route with the 
longest distance instead.

He can still start and end at any two (different) locations he wants, and he 
still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 
via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?


'''

import time
from itertools import permutations

#Timing: Start
start = time.perf_counter()

distances = {}
towns = []

# Load the puzzle data
with open('src/day09.txt') as f:
    for line in f:
        t1, _, t2, _, dist = line.split()
        distances[(t1, t2)] = int(dist)
        distances[(t2, t1)] = int(dist)
        towns.extend([t1, t2])

towns = list(set(towns))
perms = list(permutations(towns))
route_lengths = []
for perm in perms:
    route_length = 0
    for town in range(len(perm)-1):
        route_length += distances[(perm[town], perm[town+1])]
    route_lengths.append(route_length)

#Part 1
print(min(route_lengths))

#Part 2
print(max(route_lengths))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
