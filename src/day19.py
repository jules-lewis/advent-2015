'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 19: Medicine for Rudolph
------------------------------------------------------------------------------

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, 
and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph 
is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer 
chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission 
plant, capable of constructing any Red-Nosed Reindeer molecule you need. It 
works by starting with some input molecule and then doing a series of 
replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration 
involves determining the number of molecules that can be generated in one 
step from a given starting point.

For example, imagine a simpler machine that supports only the following 
replacements:

H => HO
H => OH
O => HH

Given the replacements above and starting with HOH, the following 
molecules could be generated:

HOOH (via H => HO on the first H).
HOHO (via H => HO on the second H).
OHOH (via H => OH on the first H).
HOOH (via H => OH on the second H).
HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, 
because HOOH appears twice) after one replacement from HOH. Santa's 
favorite molecule, HOHOHO, can become 7 distinct molecules (over 
nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. 
For example, given the string H2O, the transition H => OO would 
result in OO2O.

Your puzzle input describes all of the possible replacements 
and, at the bottom, the medicine molecule for which you need to 
calibrate the machine. How many distinct molecules can be created 
after all the different ways you can do one replacement on the 
medicine molecule?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Now that the machine is calibrated, you're ready to begin molecule 
fabrication.

Molecule fabrication always begins with just a single electron, e, and 
applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

e => H
e => O
H => HO
H => OH
O => HH

If you'd like to make HOH, you start with e, and then make the following 
replacements:

e => O to get O
O => HH to get HH
H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, 
can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements 
and the medicine molecule in your puzzle input, what is the fewest number of 
steps to go from e to the medicine molecule?

'''

import time

#Timing: Start
start = time.perf_counter()

replacements = []
medicine = None

for line in open("txt/day19.txt"):
    parts = line.strip().split(" => ")
    if len(parts) == 1:
        if not line.strip():
            continue
        medicine = line.strip()
        continue
    replacements.append((parts[0], parts[1]))

def part1():
    molecules = set()
    for src, repl in replacements:
        idx = 0
        while src in medicine:
            idx = medicine.find(src, idx+1)
            if idx == -1:
                break
            molecules.add(medicine[:idx] + repl + medicine[idx + len(src):])
    return len(molecules)

def part2():
    count = 0
    m = medicine
    while m != 'e':
        for src, repl in replacements:
            if repl in m:
                m = m.replace(repl, src, 1)
                count += 1
    return count

#Part 1
print(part1())

#Part 2
replacements.sort(key=lambda y: len(y[1]), reverse=True)
print(part2())

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
