
# string = "lee@matew.tim"
# list_names = string.split('@')

# for i in range(0,len(list_names)):
#     list_names[i] = list_names[i].split('.')

# list_names[1][0]

# print(list_names)

# exit()


player_data = {
    'name'      : "",
    'hp'        : 30,
    'atk'       : 5,
    'def'       : 5,
    'lives'     : 1,            # potions of revival
    'weapon'    : {},           # the weapon it has - has the 'modifier' key
    'armor'     : {},           # the armor it has - has the 'modifier' key
    'items'     : [],           # list of owned items (list of dicts)
    'killed_monsters' : {},     # killed monsters { monster : count, }
    'score'     : 0,            # keeps score of the player
    'flag_guarantee'  : False,  # when True, next monster will be one you don't have
}

monster = {
    'name' : 'Ogre',
    'description' : 'ogre description',
    'text_encounter' : 'you see a huge looking mean monster',
    'text_warn' : 'the ogre turns around and sees you. he rushes to eat you', 
    'hp' : 10,
    'atk' : 3,
    'def' : 4,
    'chance_to_spwn' : 6,
    'drop_list' : [],
    }




def dice_roll(faces = 6):
    from random import randint
    return randint(1,faces)


def player_attack(monster):

    dice = dice_roll()                                                      # Adds dice roll value to variable dice
    player_dice = dice
    player_atk = player_data['atk'] + dice                                  # Player's attack is calculated by looking at key ['atk'] and adding it to the previous dice value
    if player_data['weapon'] and 'modifier' in player_data['weapon']:       # If the player has a weapon in his hands with a damage modifier;
        player_atk += player_data['weapon']['modifier']
        weap = player_data['weapon']['modifier']
    else:
        weap = 0

    dice = dice_roll()  
    monster_dice = dice
    
    monster_def = monster['def'] + dice                                     # The monster's defence is his ['def'] key and the dice roll added together.

    monster_hit = player_atk - monster_def                                  # The monsters damage is calculated by taking the monsters defence from the players attack.

    if monster_hit > 0: 
        monster['hp'] = monster['hp'] - monster_hit                        # If the monster is hit for damage totalling an amount higher than 0 then take full damamge.
    if monster['hp'] < 0: 
        monster['hp'] = 0                                 # If monster's health goes lower than 0 hp, instead it's just 0.

    print( f"player attacks! (atk + wep = {player_data['atk']} + {weap}): dice roll = {player_dice} for a total ATK of: {player_atk}" )
    print( f"   monster defends! (def = {monster['def']}): dice roll = {monster_dice} for a total DEF of: {monster_def}" )
    print( f"   monster takes a hit of { monster_hit }. Monster HP = {monster['hp']}")
    print()

    # what should we return?
    # return monster_hit()
    # so the weapon adds to base atk



def monster_attack():
    dice = dice_roll()                                                      # Adds dice roll value to variable dice
    monster_dice = dice    
    monster_atk = monster['atk'] + dice                                     # Monster attack is calculated by adding the monster's ['atk'] key to the dice we just rolled
    
    dice = dice_roll()    
    player_dice = dice
                                                 # Adds dice roll value to variable dice
    player_def = player_data['def'] + dice                                  # The player's defence is his ['def'] key and the dice roll added together.
    if player_data['armor'] and 'modifier' in player_data['armor']:         # if the player is wearing armor that modifies their defence;
        player_def = player_def + player_data['armor']['modifier']          # - In that case add the player's armor to their defence
        arm = player_data['armor']['modifier']
    else:
        arm = 0
    
    player_hit = monster_atk - player_def                                   # The player's damage is calculated by taking the player's defence from the monster's attack.
                                                    
    if player_hit > 0: player_data['hp'] -= player_hit                      # If the player is hit for damage totalling an amount higher than 0 then take full damage.
    if player_data['hp'] < 0: player_data['hp'] = 0                         # If the player's health goes lower than 0 hp, instead it's just 0.
    
    print( f"monster attacks! (atk = {monster['atk']}): dice roll = {monster_dice} for a total ATK of: {monster_atk}" )
    print( f"   player defends! (def + armor = {player_data['def']} + {arm}): dice roll = {player_dice} for a total DEF of: {player_def}" )
    print( f"   player takes a hit of { player_hit }. Player HP = {player_data['hp']}")
    print()


    #return player_hit()

# player defense changes (dice roll) when monster rolls for his attack


print()
print()
print()

player_attack(monster) # Runs player attack
monster_attack()

player_attack(monster) # Runs player attack
monster_attack()

player_attack(monster) # Runs player attack
monster_attack()
