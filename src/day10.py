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



'''

import time

work_string = "3113322113"

#Timing: Start
start = time.perf_counter()

def elves_look(look):

    groups = []
    buffer = ''

    for c in look:
        if buffer == '':
            buffer += c
        else:
            if c == buffer[0]:
                buffer += c
            else:
                groups.append(buffer)
                buffer = c
    
    groups.append(buffer)
    return groups

def elves_say(say):

    said = ''
    for what in say:
        said += str(len(what))
        said += what[0]
    return said

#Part 1 -- forty rounds
for i in range(1,41):
    elves_see = elves_look(work_string)
    work_string = elves_say(elves_see)

print(len(work_string))

#Part 2 -- another ten rounds
for i in range(1,11):
    elves_see = elves_look(work_string)
    work_string = elves_say(elves_see)

print(len(work_string))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
