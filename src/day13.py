'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 13: Knights of the Dinner Table
------------------------------------------------------------------------------

In years past, the holiday feast with your family hasn't gone so well. Not 
everyone gets along! This year, you resolve, will be different. You're going 
to find the optimal seating arrangement and avoid all those awkward 
conversations.

You start by writing up a list of everyone invited and the amount their 
happiness would increase or decrease if they were to find themselves 
sitting next to each other person. You have a circular table that will 
be just big enough to fit everyone comfortably, and so each person will 
have exactly two neighbors.

For example, suppose you have only four attendees planned, and you 
calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness 
units (because David talks so much), but David would gain 46 happiness 
units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to 
Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits 
next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, 
David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, 
you find that this one is the most optimal, with a total change in happiness 
of 330.

What is the total change in happiness for the optimal seating arrangement 
of the actual guest list?


------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

In all the commotion, you realize that you forgot to seat yourself. At this 
point, you're pretty apathetic toward the whole thing, and your happiness 
wouldn't really go up or down regardless of who you sit next to. You assume 
everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that 
involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement 
that actually includes yourself?


'''

import time
from itertools import permutations

#Timing: Start
start = time.perf_counter()

happiness = {}
people = []

# Load the puzzle data
with open('txt/day13.txt') as f:
    # "Mallory would lose 99 happiness units by sitting next to George."
    for line in f:
        line = line.replace('lose ', '-').replace('gain ', '')[:-2]
        words = line.split()        
        p1 = words[0]
        p2 = words[-1]
        h = words[2]
        happiness[(p1, p2)] = int(h)
        people.append(p1)

people = list(set(people))
perms = list(permutations(people))

def get_max_happiness(perms):

    max_happiness = 0
    for perm in perms:
        this_happiness = 0
        for person in range(len(perm)-1):
            this_happiness += happiness[(perm[person], perm[person + 1])]
            this_happiness += happiness[(perm[person + 1], perm[person])]
        this_happiness += happiness[(perm[-1], perm[0])]
        this_happiness += happiness[(perm[0], perm[-1])]

        max_happiness = max( max_happiness, this_happiness)
    return max_happiness

#Part 1
print(get_max_happiness(perms))

#Part 2
for person in people:
    happiness[(person, 'me')] = 0
    happiness[('me', person)] = 0
people.append('me')
perms = list(permutations(people))
print(get_max_happiness(perms))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
