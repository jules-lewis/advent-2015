'''
------------------------------------------------------------------------------
ADVENT OF CODE 2015 - DAY 22: Wizard Simulator 20XX
------------------------------------------------------------------------------

Little Henry Case decides that defeating bosses with swords and stuff is 
boring. Now he's playing the game with a wizard. Of course, he gets stuck on 
another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking 
alternating turns. The player still goes first. Now, however, you don't get 
any equipment; instead, you must choose one of your spells to cast. The 
first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack 
normally. However, since you do magic damage, your opponent's armor is 
ignored, and so the boss effectively has zero armor as well. As before, 
if armor (from a spell, in this case) would reduce damage below 1, it 
becomes 1 instead - that is, the boss' attacks always deal at least 1 
damage.

On each of your turns, you must select one of your spells to cast. 
If you cannot afford to cast any spell, you lose. Spells cost mana; 
you start with 500 mana, but have no maximum limit. You must have enough 
mana to cast a spell, and its cost is immediately deducted when you cast 
it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile :  53 mana : Instantly does 4 damage.
Drain         :  73 mana : Instantly does 2 damage and heals you for 
                           2 hit points.
Shield        : 113 mana : Starts an effect that lasts for 6 turns. 
                           While it is active, your armor is increased 
                           by 7.
Poison        : 173 mana : Starts an effect that lasts for 6 turns. 
                           At the start of each turn while it is active, 
                           it deals the boss 3 damage.
Recharge      : 229 mana : Starts an effect that lasts for 5 turns. 
                           At the start of each turn while it is active, 
                           it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the 
player's turns and the boss' turns. Effects are created with a timer 
(the number of turns they last); at the start of each turn, after they 
apply any effect they have, their timer is decreased by one. If this 
decreases the timer to zero, the effect ends. You cannot cast a spell 
that would start an effect which is already active. However, effects 
can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and 
that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

Now, suppose the same initial conditions, except that the 
boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.

You start with 50 hit points and 500 mana points. The boss's actual stats 
are in your puzzle input. What is the least amount of mana you can spend 
and still win the fight? (Do not include mana recharge effects as "spending" 
negative mana.)

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------


'''

import time

#Timing: Start
start = time.perf_counter()

START_MANA = 500
PLAYER_HP = 50
BOSS_HP = 58
BOSS_DAM = 9

#Spec:      cost, damage, heal, armour boost, duration, mana boost
spells = [ (53,   4,      0,    0,            0,        0), #Magic missile
           (73,   2,      2,    0,            0,        0), #Drain
           (113,  0,      0,    7,            6,        0), #Shield
           (173,  3,      0,    0,            6,        0), #Poison
           (229,  0,      0,    0,            5,      101)]  #Recharge

print(spells)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
