'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 15: Science for Hungry People
------------------------------------------------------------------------------

Today, you set out on the task of perfecting your milk-dunking cookie recipe. 
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a 
list of the remaining ingredients you could use to finish the recipe (your 
puzzle input) and their properties per teaspoon:

capacity   (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor     (how tasty it makes the cookie)
texture    (how it improves the feel of the cookie)
calories   (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and 
you have to be accurate so you can reproduce your results in the future. 
The total score of a cookie can be found by adding up each of the properties 
(negative totals become 0) and then multiplying together everything except 
calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6,  texture 3,  calories 8
Cinnamon:     capacity 2,  durability 3,  flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of 
cinnamon (because the amounts of each ingredient must add up to 100) would
result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) 
results in a total score of 62842880, which happens to be the best score 
possible given these ingredients. If any properties had produced a negative 
total, it would have instead become zero, causing the whole score to multiply 
to zero.

Given the ingredients in your kitchen and their properties, what is the 
total score of the highest-scoring cookie you can make?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Your cookie recipe becomes wildly popular! Someone asks if you can make 
another recipe that has exactly 500 calories per cookie (so they can use 
it as a meal replacement). Keep the rest of your award-winning process the 
same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 
teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds 
to 100), the total calorie count would be 40*8 + 60*3 = 500. The total 
score would go down, though: only 57600000, the best you can do in such 
trying circumstances.

Given the ingredients in your kitchen and their properties, what is the 
total score of the highest-scoring cookie you can make with a calorie total 
of 500?
'''

import time

#Timing: Start
start = time.perf_counter()

'''
We just want combinations that add up to 100. There are four ingredients, so
the minimum three of them could add up to is 3 teaspoons, which means the
fourth one must be 97. In other words, it's impossible to have a recipe with
97 teaspoons of anything. Creating a list of possible recipes was a LOT
quicker using naive loops than using itertools.product()!
'''
recipes = []
for i in range(1, 98):
    for j in range(1, 98):
        if (i + j) < 100:
            for k in range(1, 98):
                if (i + j + k) < 100:
                    recipes.append((i, j, k, 100 - (i + j + k)))

# Load the puzzle data
ingredients = []
with open('src/day15.txt') as f:
    # Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
    for line in f:
        parts = line.replace(':', ',').split(',')  
        qualities = []
        for part in parts[1:]:
            qualities.append(int(part.split()[1]))
        ingredients.append(qualities)

max_score = 0
for recipe in recipes:
    score = cap = dur = fla = tex = cal = 0
    for x in range(4):
        ingredient = ingredients[x]
        tsp = recipe[x]
        cap += tsp * ingredient[0]
        dur += tsp * ingredient[1]
        fla += tsp * ingredient[2]
        tex += tsp * ingredient[3]
        cal += tsp * ingredient[4]
    if cap > 0:
        if dur > 0:
            if fla > 0:
                if tex > 0:
                    if cal == 500:
                        score = cap * dur * fla * tex
                        max_score = max(score, max_score)
print(max_score)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
