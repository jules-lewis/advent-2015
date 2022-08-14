'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 4: The Ideal Stocking Stuffer
------------------------------------------------------------------------------

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as 
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at 
least five zeroes. The input to the MD5 hash is some secret key (your puzzle 
input, given below) followed by a number in decimal. To mine AdventCoins, you 
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) 
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of 
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest 
such number to do so.

If your secret key is pqrstuv, the lowest number it combines with to make 
an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash 
of pqrstuv1048970 looks like 000006136ef....

Your puzzle input is yzbqklnj.

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Now find one that starts with six zeroes.

'''

import time
import hashlib

#Timing: Start
start = time.perf_counter()

def solve(key, zeroes):

    n = 1
    prefix = zeroes * '0'

    while True:
        s = key + str(n)
        h = hashlib.md5(s.encode()).hexdigest()[:zeroes]
        if h == prefix:
            return n
        n += 1

#Part 1
print(solve('yzbqklnj', 5))

#Part 2
#print(solve('yzbqklnj', 6))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
