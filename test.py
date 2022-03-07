

print( dict() )

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
# value = 'Mathew'

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


# typewriter('', 0.01)

# typewriter()

          8_ball =  ["As I see it, yes.",
                     "Ask again later.", 
                     "Better not tell you now.", 
                     "Cannot predict now.", 
                     "Concentrate and ask again.",
                     "Don’t count on it.", 
                     "It is certain.", 
                     "It is decidedly so.", 
                     "Most likely.", 
                     "My reply is no.", 
                     "My sources say no.", 
                     "Outlook not so good.", 
                     "Outlook good.", 
                     "Reply hazy", 
                     "try again.", 
                     "Signs point to yes.", 
                     "Very doubtful.", 
                     "Without a doubt.",
                     "Yes", 
                     "Yes definitely.", 
                     "You may rely on it."]

#typewriter( 5 , 0.01)