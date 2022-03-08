player_data = {
        'name' : "",
        'hp' : 0,
        'atk' : 5,
        'def' : 5,
        'lives' : 1,                # potions of revival
        'weapon' : {},              # the weapon it has
        'armor' : {},               # the armor it has
        'items' : [],               # list of owned items (list of dicts)
        'killed_monsters' : {},     # killed monsters { monster : count, }
        'score' : 0,                # keeps score of the player
        'flag_guarantee' : False,   # when True, next monster will be one you don't have
}



monster = {
        'id' : "goblin",
        'name' : "Goblin",
        'encounter' : "You encounter a slimy green goblin",
        'warn' : "The goblin sneaks over to you and steals one of your rusty coins! The fiend, not my coins!",
        'winning' : "you slice the goblin in half and reclaim your lost item",
        'losing' : "the goblin laughs as he steals all your items, and knocks you unconscious",
        'hp' : 10,
        'atk' : 3,
        'def' : 3,
        'chance' : 3,
        'score' : 1,
        'drops' : [],
}



# rolls a dice and returns a value between 1 and faces (defaults to 6)
def dice_roll(faces = 6):
        from random import randint
        new_dice = randint(1,faces)
        return new_dice
# need to have return to store value of new_dice in new_dice
# pass value/result from a function to a variable?

# get player atk base + player weapon + dice
# get monster def base + dice
# compare player_atk > mon_def
# monster hp = ( player_atk - monster dif )

def player_attack(monster):
        
        dice = dice_roll(faces = 6)
        player_atk = player_data['atk'] + dice 
        if player_data['weapon'] and 'modifier' in player_data['weapon']: 
                player_atk + player_data['weapon']['modifier']
        
        dice = dice_roll(faces = 6)
        monster_def = monster['def'] + dice

        monster_hit = player_atk - monster_def
        
        if monster_hit > 0: monster['hp'] -= monster_hit
        if monster['hp'] < 0: monster['hp'] = 0


        # what should we return?
        return monster_hit()
        # so the weapon adds to base atk
        


# def monster_attack():
#         dice_roll(),
#         monster_atk = monster['atk'],
#         player_def = player_data['def'],
#         monster_atk = monster_atk - player_def,
#         return monster_atk(),
# # player defense changes (dice roll) when monster rolls for his attack

player_attack()

print(monster_attack)
        








# print( "key=value"[:2] )

#print( int('') )

# def load_monster_file(file):
#     print(file)
#     with open(file,'r') as file:
#         print( file.readline() )



# # print('\n'*3)

# # from os import listdir, getcwd
# # from os.path import isfile, join

# # file_stem = 'ascii_monster_'
# # curent_dir = getcwd()
# # #print( listdir(curent_dir) )
# # onlyfiles = [f for f in listdir(curent_dir) if isfile(join(curent_dir, f)) and f[:len(file_stem)].lower()==file_stem]
# # #print(onlyfiles)
# # for file in onlyfiles:
# #     # print(file)
# #     load_monster_file(file)
    


# def called(x):
#     print(f'i called : {x}')

# def calling(xx, my_called):
#     print(f'will call {called} with  {xx}')
#     my_called( xx )

# calling('miu',called)


# my_dict = {}

# key = 'name'
# value = 'Eduard'

# my_dict.update( {key: value} )

# key = 'new_name'
# value = 'Matthew'

# my_dict.update( {key: value} )

# print( my_dict )

# # game over condition
# #This is a list of itenms that can be picked up
# #This is a list of itenms that can be picked up

# def game_over():
#         if ['health'] == 0: #needs defining/tidying
#             print('game over')
#             retry = input('retry?')
#             if retry == 'yes':
#                 game()



# # print('mario')
# # from time import sleep
# # sleep(2)
# # print('luigi')

# my_dict = {}
# if False and my_dict['id']: print('yay') 
# else: print('nay')

# # delay can be changed, can have 3 x delay on space, can have random (1 in 5) 3 x delay while writing the text
# # unsing inkey, i could implement a printall with space/esc (after space clear buffer)
# def typewriter( text="miw miw", delay=0.01, newline=True, space_breaks=True, random_breaks=True, rush_on_enter_or_space=True ):
    
#     print(f'text is of type {type(text)} and it is: "{text}"', flush=True)
#     from time import sleep
#     #from random import randint
#     #should_break = False
#     #rush_through = False
#     for char in text:
#         print(char, end='', flush=True)
#         # if rush_on_enter_or_space and inkey() in [32,13]: 
#         #     rush_through = True
#         # if not rush_through:
#         sleep(delay)
#             # if random_breaks:
#             #     should_break = randint(1,5)==3
#             # if (char==' ' and space_breaks) or should_break: 
#             #     for _ in range(4): sleep(delay)
#     # if newline: print(flush=True)


#pewriter('', 0.01)

# typewriter()

        #   8_ball =  ["As I see it, yes.",
        #              "Ask again later.", 
        #              "Better not tell youcounter now.", 
        #              "Cannot predict now.", 
        #              "Concentrate and ask again.",
        #              "Don’t count on it.", 
        #              "It is certain.", 
        #              "It is decidedly so.", 
        #              "Most likely.", 
        #              "My reply is no.", 
        #              "My sources say no.", 
        #              "Outlook not so good.", 
        #              "Outlook good.", 
        #              "Reply hazy", 
        #              "try again.", 
        #              "Signs point to yes.", 
        #              "Very doubtful.", 
        #              "Without a doubt.",
        #              "Yes", 
        #              "Yes definitely.", 
        #              "You may rely on it."]

#typewriter( 5 , 0.01)


# dict_1 = {'A':1, 'B':2, 'C':3} # Values from dictionary 1
# dict_2 = {'B':4, 'C':5, 'D':6} # Values from dictionary 2
# a_counter = Counter(dict_1) # Dictionary 1 
# b_counter = Counter(dict_2) 
# add_dict = a_counter + b_counter
# dict_3 = dict(add_dict)
# print(dict_3)

