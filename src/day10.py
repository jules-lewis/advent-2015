'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 10: Elves Look, Elves Say
------------------------------------------------------------------------------

Today, the Elves are playing a game called look-and-say. They take turns 
making sequences by reading aloud the previous sequence and using that 
reading as the next sequence. For example, 211 is read as "one two, two 
ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value 
as input for the next step. For each step, take the previous value, and 
replace each run of digits (like 111) with the number of digits (3) followed 
by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. 
What is the length of the result?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Neat, right? You might also enjoy hearing John Conway talking about this 
sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 
50 times. What is the length of the new result?

'''

import time
import re


#Timing: Start
start = time.perf_counter()

work_string = "3113322113"

#This will group all similar digits in a string
#See this explained at https://regexr.com/6sdqb
regex = re.compile(r'((\d)\2*)')

def translate(work_string):
    groups = [i[0] for i in regex.findall(work_string)]
    new_string = ''
    for group in groups:
        new_string += str(len(group)) + group[0]
    return new_string

#Part 1 -- forty rounds
for i in range(1,41):
    work_string = translate(work_string)
print(len(work_string))

#Part 2 -- another ten rounds
for i in range(1,11):
    work_string = translate(work_string)
print(len(work_string))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
