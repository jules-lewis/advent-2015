'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 5: Doesn't He Have Intern-Elves For This? 
------------------------------------------------------------------------------

Santa needs help figuring out which strings in his text file are naughty or 
nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or 
  aeiouaeiouaeiou.

It contains at least one letter that appears twice in a row, like xx, 
  abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

It does not contain the strings ab, cd, pq, or xy, even if they are 
  part of one of the other requirements.

For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), 
  a double letter (...dd...), and none of the disallowed substrings.

aaa is nice because it has at least three vowels and a double letter, even 
  though the letters used by different rules overlap.

jchzalrnumimnmhp is naughty because it has no double letter.

haegwjzuvuyypxyu is naughty because it contains the string xy.

dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?


------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Realizing the error of his ways, Santa has switched to a better model of 
determining whether a string is naughty or nice. None of the old rules apply, 
as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the 
string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like 
aaa (aa, but it overlaps).

It contains at least one letter which repeats with exactly one letter between 
them, like xyx, abcdefeghi (efe), or even aaa.

For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a 
letter that repeats with exactly one letter between them (zxz).

xxyxx is nice because it has a pair that appears twice and a letter that 
repeats with one between, even though the letters used by each rule overlap.

uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a 
single letter between them.

ieodomkazucvgmuy is naughty because it has a repeating letter with one 
between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

'''

import time

#Timing: Start
start = time.perf_counter()

#Load the puzzle data
with open('day05.txt') as f:
    data = [line.rstrip() for line in f]

def count_vowels(s):
    return sum(map(s.count, "aeiou"))

def check_forbidden(s):
    return sum(map(s.count, ['ab', 'cd', 'pq', 'xy'])) == 0

def check_double(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def check_triples(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def check_duplicates(s):
    for i in range(len(s)-1):
        check = s[i:i+2]
        if check in s[i+2:]:
            return True
    return False

#Part 1
nice_strings = 0
for s in data:
    if count_vowels(s) > 2:
        if check_forbidden(s):
            if check_double(s):
                nice_strings += 1
print(str(nice_strings))

#Part 2
nice_strings = 0
for s in data:
    if check_triples(s):
        if check_duplicates(s):
            nice_strings += 1
print(str(nice_strings))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
