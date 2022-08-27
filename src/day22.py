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
NOTES
------------------------------------------------------------------------------

- If armor (from a spell) would reduce damage below 1, it becomes 1 instead.
  That is, the boss' attacks always deal at least 1 damage.

- On each of your turns, you MUST select one of your spells to cast.

- If you cannot afford to cast any spell, you lose. 

- You must have enough mana to cast a spell, and its cost is immediately 
  deducted when you cast it.

- You cannot cast a spell that would start an effect which is already active. 
  However, effects can be started on the same turn they end.

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 
1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount 
of mana you can spend and still win the fight?

'''

import time
from copy import deepcopy

#Timing: Start
start = time.perf_counter()

PLAYER_MANA = 500
PLAYER_HP = 50
BOSS_HP = 58
BOSS_DAM = 9
MAX_MANA = 9999999

#Spec:    cost, dam, heal, armour boost, duration, mana boost
spells = [(53,  4,   0,    0,            0,        0),    #Magic missile
          (73,  2,   2,    0,            0,        0),    #Drain
          (113, 0,   0,    7,            6,        0),    #Shield
          (173, 3,   0,    0,            6,        0),    #Poison
          (229, 0,   0,    0,            5,      101)]    #Recharge

def play(boss_hp, player_hp, player_mana, active_spells, player_turn, mana_used, part):

    #In Part 2,  it costs 1hp to play each round    
    if (part == 2) and player_turn:
        player_hp -= 1
        if player_hp < 1: return False
            
    player_armour = 0
    new_spells = []
    for spell in active_spells:
        if spell[4] >= 0: # spell effect applies now
            boss_hp -= spell[1]
            player_hp += spell[2]
            player_armour += spell[3]
            player_mana += spell[5]

        new_duration = spell[4] - 1
        if new_duration > 0:
            new = (spell[0], spell[1], spell[2], spell[3], new_duration, spell[5])
            new_spells.append(new)
    
    if boss_hp <= 0:
        global least_mana
        least_mana = min(least_mana, mana_used)
        return True

    #Don't follow paths that already cost too much!
    if mana_used >= least_mana:
        return False

    if player_turn:
        for spell in spells:
            spell_already_active = False
            for comp_spell in new_spells:
                if comp_spell[0] == spell[0]:
                    spell_already_active = True
                    break

            if not spell_already_active:
                spell_cost = spell[0]
                if spell_cost <= player_mana:
                    spell_stack = deepcopy(new_spells)
                    spell_stack.append(spell)
                    play(boss_hp, player_hp, player_mana - spell_cost, 
                         spell_stack, False, mana_used + spell_cost, part)
    else:
        net_damage = BOSS_DAM - player_armour
        net_damage = max(1, net_damage)
        player_hp -= net_damage
        if player_hp > 0:
            play(boss_hp, player_hp, player_mana, new_spells, True, mana_used, part)

least_mana = MAX_MANA
play(BOSS_HP, PLAYER_HP, PLAYER_MANA, [], True, 0, 1)
print(least_mana)

least_mana = MAX_MANA
play(BOSS_HP, PLAYER_HP, PLAYER_MANA, [], True, 0, 2)
print(least_mana)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
