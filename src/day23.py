'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 23: Opening the Turing Lock
------------------------------------------------------------------------------

Little Jane Marie just got her very first computer for Christmas from some 
unknown benefactor. It comes with instructions and an example program, but 
the computer itself seems to be malfunctioning. She's curious what the program 
does, and would like you to help her run it.

The manual explains that the computer supports two registers and six 
instructions (truly, it goes on to remind the reader, a state-of-the-art 
technology). The registers are named a and b, can hold any non-negative 
integer, and begin with a value of 0. The instructions are as follows:

- hlf r         : halves register r, then continues
- tpl r         : triples register r, then continues
- inc r         : increments register r by 1, then continues
- jmp offset    : a jump; continues at instruction offset away 
                  relative to itself.
- jie r, offset : is like jmp, but only jumps if register r is even
- jio r, offset : is like jmp, but only jumps if register r is 1

All three jump instructions work with an offset relative to that 
instruction. The offset is always written with a prefix + or - to 
indicate the direction of the jump (forward or backward, respectively). 
For example, jmp +1 would simply continue with the next instruction, 
while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the 
ones defined.

For example, this program sets a to 2, because the jio instruction 
causes it to skip the tpl instruction:

    inc a
    jio a, +2
    tpl a
    inc a

What is the value in register b when the program in your puzzle 
input is finished executing?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

The unknown benefactor is very thankful for releasi-- er, helping little Jane 
Marie with her computer. Definitely not to distract you, what is the value 
in register b after the program is finished executing if register a starts as 
1 instead?


'''

import time

#Timing: Start
start = time.perf_counter()

with open("txt/day23.txt") as f:
    program = [line.strip().replace(',', '').split() for line in f.readlines()]

reg_a = 1
reg_b = 0
index = 0
cont = True
top_bound = len(program)

while cont:
    loc = program[index]
    instruction = loc[0]
    jump = 1
    if instruction == 'inc':
        if loc[1] == 'a':
            reg_a += 1
        else:
            reg_b += 1
    elif instruction == 'tpl':
        if loc[1] == 'a':
            reg_a *= 3
        else:
            reg_b *= 3
    elif instruction == 'hlf':
        if loc[1] == 'a':
            reg_a = reg_a // 2
        else:
            reg_b = reg_b // 2
    elif instruction == 'jmp':
        if loc[1][0] == '+':
            jump = int(loc[1][1:])
        else:
            jump = -int(loc[1][1:])
    elif instruction == 'jio':
        cond_met = False
        if loc[1] == 'a':
            if reg_a == 1:
                cond_met = True
        else:
            if reg_b == 1:
                cond_met = True
        if cond_met:
            if loc[2][0] == '+':
                jump = int(loc[2][1:])
            else:
                jump = -int(loc[2][1:])
    elif instruction == 'jie':
        cond_met = False
        if loc[1] == 'a':
            if (reg_a % 2) == 0:
                cond_met = True
        else:
            if (reg_b % 2) == 0:
                cond_met = True
        if cond_met:
            if loc[2][0] == '+':
                jump = int(loc[2][1:])
            else:
                jump = -int(loc[2][1:])

    index += jump
    if index < 0 or index >= top_bound:
        cont = False

print(reg_b)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
