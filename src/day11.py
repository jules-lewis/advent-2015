'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 11: Corporate Policy
------------------------------------------------------------------------------

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has 
devised a method of coming up with a password based on the previous one. 
Corporate policy dictates that passwords must be exactly eight lowercase 
letters (for security reasons), so he finds his new password by incrementing 
his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so 
on. Increase the rightmost letter one step; if it was z, it wraps around to 
a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has 
imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, 
like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd 
doesn't count.

Passwords may not contain the letters i, o, or l, as these letters can be 
mistaken for other characters and are therefore confusing.

Passwords must contain at least two different, non-overlapping pairs of 
letters, like aa, bb, or zz.

For example:

hijklmmn meets the first requirement (because it contains the straight hij) 
but fails the second requirement requirement (because it contains i and l).

abbceffg meets the third requirement (because it repeats bb and ff) but 
fails the first requirement.

abbcegjk fails the third requirement, because it only has one double 
letter (bb).

The next password after abcdefgh is abcdffaa.

The next password after ghijklmn is ghjaabcc, because you eventually skip 
all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next 
password be?

Your puzzle input is hxbxwxba

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Santa's password expired again. What's the next one?

'''

import time
import re

work_string = "hxbxwxba"

#Timing: Start
start = time.perf_counter()

def incr_string(s):
    if len(s):
        l, r = s[:-1], s[-1]
        if r == 'z':
            return incr_string(l) + 'a'
        else:
            return l + chr(ord(r) + 1)
    else:
        return ''

def is_password_ok(s):

    #Test 3 - let's eliminate i, o, l first
    if sum(map(s.count, 'iol')) == 0:
        #Test 1 - triples that don't have i, o, l
        if sum(map(s.count, ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz'])):
            #Test 2 - two different sets of doubled letters
            if len(set(re.findall(r'(.)\1', s))) > 1:
                return True
    return False

def get_new_password(s):
    s = incr_string(s)
    while not is_password_ok(s):
        s = incr_string(s)
    return s

#Part 1
work_string = get_new_password(work_string)
print(work_string)

#Part 2
print(get_new_password(work_string))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
