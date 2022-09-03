'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 12: JSAbacusFramework.io
------------------------------------------------------------------------------

Santa's Accounting-Elves need help balancing the books after a recent order. 
Unfortunately, their accounting software uses a peculiar storage format. 
That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), 
objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply 
find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Uh oh - the Accounting-Elves have realized that they double-counted 
everything red.

Ignore any object (and all of its children) which has any property with the 
value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.


'''

import time
import re
import json

#Timing: Start
start = time.perf_counter()

with open('txt/day12.txt') as f:
    data = json.loads(f.read())

#Part 1
print(sum(int(i) for i in re.findall(r'-?\d+', str(data))))

#Part 2
def sum_numbers(node):

    if type(node) is int:
        return node
    
    if type(node) is list:
        return sum(map(sum_numbers, node))
    
    if type(node) is dict:
        vals = node.values()
        
        if "red" in vals:
            return 0
        
        return sum(map(sum_numbers, vals))
    
    else:

        return 0

print(sum_numbers(data))


#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
