'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 17: No Such Thing as Too Much
------------------------------------------------------------------------------

The elves bought too much eggnog again - 150 liters this time. To fit it all 
into your refrigerator, you'll need to move it into smaller containers. You 
take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 
If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely, how many different combinations of 
containers can exactly fit all 150 liters of eggnog?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

While playing with all the containers in the kitchen, another load of eggnog 
arrives! The shipping and receiving department is requesting as many 
containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of 
eggnog. How many different ways can you fill that number of containers and 
still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were 
three ways to use that many containers, and so the answer there would be 3.



'''

import time
import itertools

#Timing: Start
start = time.perf_counter()

# Load the puzzle data
with open('src/day17.txt') as f:
    containers = [int(line) for line in f]

target = 150

#Part 1
combi_count = 0
for l in range(1, len(containers)+1):
    for c in itertools.combinations(containers, l):
        if sum(c) == target:
            combi_count += 1
print(combi_count)

#Part 2
combi_count = 0
right_length_found = False
for l in range(1, len(containers)+1):
    for c in itertools.combinations(containers, l):
        if sum(c) == target:
            right_length_found = True
            combi_count += 1
    if right_length_found:
        print(combi_count)
        break

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
