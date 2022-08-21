'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 14: Reindeer Olympics
------------------------------------------------------------------------------

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must 
rest occasionally to recover their energy. Santa would like to know which of 
his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting 
(not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After 
ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the 
eleventh second, Comet begins resting (staying at 140 km), and Dancer 
continues on for a total distance of 176 km. On the 12th second, both 
reindeer are resting. They continue to rest until the 138th second, when 
Comet flies for another ten seconds. On the 174th second, Dancer flies 
for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and 
Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by 
that point). So, in this situation, Comet would win (if the race ended 
at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after 
exactly 2503 seconds, what distance has the winning reindeer traveled?


------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Seeing how reindeer move in bursts, Santa decides he's not pleased with the 
old scoring system.

Instead, at the end of each second, he awards one point to the reindeer 
currently in the lead. (If there are multiple reindeer tied for the lead, 
they each get one point.) He keeps the traditional 2503 second time limit, 
of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is 
in the lead and gets one point. He stays in the lead until several seconds 
into Comet's second burst: after the 140th second, Comet pulls into the 
lead and gets his first point. Of course, since Dancer had been in the 
lead for the 139 seconds before that, he has accumulated 139 points by 
the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor 
Comet, our old champion, only has 312. So, with the new scoring system, 
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), 
after exactly 2503 seconds, how many points does the winning reindeer 
have?
'''

import time

#Timing: Start
start = time.perf_counter()

duration = 2503
reindeer = {}

# Load the puzzle data
with open('src/day14.txt') as f:
    # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
    for line in f:
        words = line.split()  
        reindeer[words[0]] = [int(words[3]), int(words[6]), int(words[-2])]

def get_reindeer_in_lead(seconds_elapsed):

    max_distance = 0
    max_reindeer = []

    for r in reindeer:

        #Get the basic values
        speed, fly_time, rest = reindeer[r]
        
        #The length of each cycle of flight and rest
        cycle_length = fly_time + rest
        
        #How many cycles the reindeer has completed during seconds_elapsed
        cycles = seconds_elapsed // cycle_length
        remainder = seconds_elapsed % cycle_length

        #Distance is in two parts, completed cycles, and partial
        distance = (cycles * fly_time * speed)

        #The partial cycle. If the reindeer hasn't completed its flight,
        #just work out how much it has done
        if remainder < fly_time:
            distance += (remainder * speed)
        else:
            #Reindeer has completed its flight
            distance += (fly_time * speed)

        #Keep track of leading reindeer. In Part 2, we have to account
        #for the fact that more than one reindeer can have covered the
        #same distance
        if distance > max_distance:
            max_distance = distance
            max_reindeer = [[r, max_distance]]
        #Remember to account for DRAWS!
        elif distance == max_distance:
            max_reindeer.append([r, max_distance])

    return max_reindeer

#Part 1
print(get_reindeer_in_lead(2503)[0][1])

#Part 2
scoreboard = {}
for i in range(1, duration+1):
    lst = get_reindeer_in_lead(i)
    #There could be more than one reindeer in joint lead!
    for r in lst:
        r_name = r[0]
        if r_name in scoreboard:
            scoreboard[r_name] += 1
        else:
            scoreboard[r_name] = 1
print(max(scoreboard.values()))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
