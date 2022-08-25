'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 6: Probably a Fire Hazard ---
------------------------------------------------------------------------------

Because your neighbors keep defeating you in the holiday house decorating 
contest year after year, you've decided to deploy one million lights in a 
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has 
mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the 
lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions 
include whether to turn on, turn off, or toggle various inclusive ranges 
given as coordinate pairs. Each coordinate pair represents opposite corners 
of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore 
refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights 
by doing the instructions Santa sent you in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.

- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, 
    turning off the ones that were on, and turning on the ones that were off.

- turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

You just finish implementing your winning light pattern when you realize you 
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each 
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of 
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of 
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of 
those lights by 2.

What is the total brightness of all lights combined after following Santa's 
instructions?

For example:

- turn on 0,0 through 0,0 would increase the total brightness by 1.

- toggle 0,0 through 999,999 would increase the total brightness by 2000000.

'''

import time

#Timing: Start
start = time.perf_counter()

#Parse an instruction from the input file
def parse_instruction(s):
    words = s.replace('turn ', '').replace(',', ' ').split()
    instruction, x1, y1, _, x2, y2 = words
    return instruction, int(x1), int(x2), int(y1), int(y2)

#Load the puzzle data
with open('txt/day06.txt') as f:
    data = [line.rstrip() for line in f]

#PART 1
lights = {}
for line in data:
    instruction, x1, x2, y1, y2 = parse_instruction(line)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2+1):
            key = (x, y)
            if instruction == 'off':
                lights[key] = 0
            elif instruction == 'on':
                lights[key] = 1
            else: #toggle
                if key in lights:
                    if lights[key] == 0:
                        lights[key] = 1
                    else:
                        lights[key] = 0
                else:
                    lights[key] = 1
print(sum(lights.values()))

#PART 2
lights = {}
for line in data:
    instruction, x1, x2, y1, y2 = parse_instruction(line)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2+1):
            key = (x, y)
            if instruction == 'off':
                if key in lights:
                    if lights[key] > 0:
                        lights[key] -= 1
            else:
                if instruction == 'on':
                    incr = 1
                else: #toggle
                    incr = 2
                if key in lights:
                    lights[key] += incr
                else:
                    lights[key] = incr

print(sum(lights.values()))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
