

# The Warrior King of Tristram is very old & close to death. He has instructed all warriors to prove their strength by bringing back the head of each monster including that of the largest Dragon in the Tristram Kingdom, if you complete this task you will become the new King of Tristram.
# "Your name" has defeated all of the monsters in the land of Tristram!
# The First King of Tristram celebrates your victory in front of the Tristram Castle in a special Coronation Ceremony! You are now the new King!

# template for the monster entity
# monster = {
#     'name' : 'Ogre',
#     'description' : 'ogre description',
#     'text_encounter' : 'you see a huge looking mean monster',
#     'text_warn' : 'the ogre turns around and sees you. he rushes to eat you', 
#     'hp' : 10,
#     'atk' : 3,
#     'def' : 4,
#     'chance_to_spwn' : 6,
#     'drop_list' : [],
#     }


## some ascii art links
## https://textart.io/art/tag/house/1
## https://www.asciiart.eu/buildings-and-places/houses
## https://textart.io/#



from distutils.dep_util import newer_group
from lib2to3.pytree import type_repr
from multiprocessing.connection import answer_challenge


def the_game():

    # some config data
    ascii_file_stem_monster  = 'ascii_monster_'        # how all the moster files start
    ascii_file_stem_event    = 'ascii_event_'          # how all the events files start

    ascii_file_items         = 'ascii_loot_items.txt'  # holds all the items
    ascii_file_strings       = 'ascii_strings.txt'     # holds the strings for encounters
    
    ascii_file_game_start    = 'ascii_game_start.txt'
    ascii_file_game_win      = 'ascii_game_win.txt'
    ascii_file_game_loose    = 'ascii_game_loose.txt'

    chance_encounter_monster = 7        # 7 out of 10 to fight a monster
    chance_encounter_event   = 5        # 5 out of 10 to have an event
    #chance_encounter_none = 2          # 2 out of 2 to have nothing special in the encounter

    monster_fight_warn_time  = 5        # time to answer untill waring
    monster_fight_total_time = 10       # time to answer untill failed


    # the player record - hods everything about the player
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

    monsters    = []     # list of dictionaries (dicts)
    events      = []     # list of events (dicts)
    loot_items  = []     # list of items (dics)
    encounters  = []     # list of encounters strings 

    highscore   = []     # list of highscore (dicts) { name, value, date }

    
    # useful in debug, tells the name of the calling function
    def whoami( lvl=0 ):
        import sys
        return sys._getframe(1+lvl).f_code.co_name


    # prints an problem  message in red and includes the function where the error hapened
    def print_err( message ):
        text_to_print = f'\033[1;31merr=>{whoami(1)}: '+message+'\033[0m'
        print(text_to_print)


    # clears the terminal screen (not the history tho)
    def clear_screen():
        import os
        clear = lambda: os.system('cls')
        clear()


    # reads a keypress from the buffer if theres one there, otherwise returns 0
    def inkey():
        import msvcrt
        if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
        key = msvcrt.getch()
        if ord(key) == 0: key = msvcrt.getch()  # special chars
        if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
        return ord(key)


    # play a beeping sound, if list is provided must be a list of tuples/list of (tone,duration)
    # they will be played in succession
    def beep( duration = 100, frequency = 2500):
        # Set Frequency To 2500 Hertz
        # Set Duration To 1000 ms == 1 second
        import winsound
        winsound.Beep(frequency, duration)


    # will play the list of bees provided, can be stoped with space/enter, like the typewritter
    # list_of_beeps must be a list of (tone,duraction)
    def beep_from_list( list_of_beeps = [], stop_on_enter_space = True ):
        # will use beep to play 
        for beep_pair in list_of_beeps:
            tone     = beep_pair[0]
            duration = beep_pair[1]
            beep( duration, tone )
            if stop_on_enter_space and inkey() in [32,13]: break


    # delay can be changed, can have 3 x delay on space, can have random (1 in 5) 3 x delay while writing the text
    # unsing inkey, i could implement a printall with space/esc (after space clear buffer)
    def typewriter( text:str, delay=0.02, newline=True, space_breaks=False, random_breaks=True, rush_on_enter_or_space=True ):
        from time import sleep
        from random import randint
        should_break = False
        rush_through = False
        for char in text:
            print(char, end='', flush=True)
            if rush_on_enter_or_space and inkey() in [32,13]: 
                rush_through = True
            if not rush_through:
                sleep(delay)
                if random_breaks:
                    should_break = ( randint(1,3)==2 )
                if (char==' ' and space_breaks) or should_break: 
                    for _ in range(5): sleep(delay)
        if newline: print(flush=True)

    
    # rolls a dice and returns a value between 1 and faces (defaults to 6)
    def dice_roll(faces = 6):
        from random import randint
        return randint(1,faces)


    # answer must be from answer_list, will return 'failed' if no answer was given
    def get_answer(answer_list, answer_time=0, warn_time=0, warn_text='', print_the_answer = True):
        tick = 0.1
        tick_answer = answer_time/tick
        tick_warn = warn_time/tick
        tick_count = 0
        from time import sleep 
        while answer_time==0 or tick_count<tick_answer:
            sleep(0.1)
            tick_count += 1
            answer = inkey()    
            #if o got allowed answer the return char
            if chr(answer) in answer_list:
                if print_the_answer: 
                    print( chr(answer), end='' )
                return chr(answer)
            elif warn_time and warn_text and tick_count == tick_warn:
                typewriter(warn_text,)      # delay=0.01
            elif answer_time and tick_count == tick_answer:
                return 'failed'


    # will scan all the files that start with a specified string, like "ascii_monster_"
    # then it will pass them to a parsing function received in callable_func 
    # which will parse the file into a dictionary that will be aded to a list
    def load_files(file_stem,calable_func,dest_list):
        from os import listdir, getcwd
        from os.path import isfile, join

        #file_stem = ascii_file_stem_monster
        curent_dir = getcwd()
        #print( listdir(curent_dir) )
        onlyfiles = [f for f in listdir(curent_dir) if isfile(join(curent_dir, f)) and f[:len(file_stem)].lower()==file_stem]
        #print(onlyfiles)
        for file in onlyfiles:
            # print(file)
            calable_func(file, dest_list)  # load_monster_ascii or load_event_ascii


    # validates the monster read from file, that has all the necesary fields
    # todo: create the validation method
    def validate_monster_event_item( monster_event_dict, display_message = True ):
        #print('todo: validate_monster_item()')
        #if monster_dict['name']
        # if its empty, you'll not add it
        if not monster_event_dict: return False

        return True 


    # validates if the item to be added has the required properties to work with the game
    # todo: validates the loot item before adding it to the list
    def validate_loot_item( items_dict, display_message = True ):
        #print('todo: validate_monster_item()')
        if not items_dict: return False

        return True


    # goes through the lines of an ascii file (ascii_monster_<>.txt or ascii_event_<>.txt) and
    # creates a dictionary with everything inside (ascii, list of drops, key/value pairs)
    # and that dictionary is validated and added tot the list passed as parameter (monsters or events)
    def process_ascii(file_name, dest_list):
        print(f"dbg: {whoami()} ~ file_name = '{file_name}'")
        with open(file_name,'r') as file:
            item_read = {}     # =dict()
            ascii_img = ""
            for line in file.readlines():
                #line = line.strip()        # removes \n -- i do it lower where i read the key/value pair

                if not line.strip(): 
                    continue

                elif line[:1] == '#':       # the line is a comment, ignore it
                    continue

                elif line[:2] == '##':        # collects the lines for the ascii image
                    ascii_img += line

                elif line.find('=') > 0:            # if the line is a key = value pair
                    line = line.strip()
                    dict_key = line[:line.find('=')].strip().lower()
                    
                    if dict_key == 'drops':     # if it's the 'drops' line, builds a list of lists'
                        s = line[line.find('=')+1:].strip()
                        dict_value = [ l.split(':') for l in s.split(',') if l ]
                    
                    else:                       # just the normal value for it
                        dict_value = line[line.find('=')+1:].strip().replace('\\n','\n')

                        if dict_key in ('hp','atk','def','score_point','modifier','cooldown'):
                            if dict_value.strip():
                                dict_value = int( dict_value.strip() )
                            else:
                                dict_value = 0
                    
                    # if not dict_key:
                    #     print(f'hey, dict_key is empty {line}')

                    #if not dict_key: breakpoint
                    #print(f'dict key : value = {dict_key} : {dict_value}')   # debug
                    item_read[dict_key] = dict_value                        # adds the new key/value to dictionary
                # elif not line: continue
                else:
                    if line: print(f'err=> {whoami()}: shouldnt run, line is "{line}" ')
                
            # todo: remove this when everything works fine
            # for debug purposes, adds a dbg_filename property to the dictionary, in case theres an issue to find the source
            item_read['dbg_filename'] = file_name

            # validate the required fields are in there
            if validate_monster_event_item(item_read):
                dest_list.append(item_read)


    # reads the ascii_loot_items.txt and build a list of dictionaries for every item, with its properties
    def process_ascii_loot(file_name,dest_list):
        with open(file_name,'r') as file:
            # will go line by line, when it encounters 'id' (its a new object) it will add the 'item_read' dict to the 'dest_list' 
            # if item_read['id'] its not empty, then creates a new 'item_read' and adds the 'id' property to it
            item_read = {}     # =dict()
            for line in file.readlines():
                line = line.strip()        # removes \n

                if line[:1] == '#': continue        # skip over comments
                if line.find('=') <= 0: continue    # skip if not  key / value pair

                # get the key / value pair
                dict_key    = line[:line.find('=')].strip().lower()
                dict_value  = line[line.find('=')+1:].strip().replace('\\n','\n')

                # if dict_key is 'id' and previous 'item_read[id]' has value, 
                # it means 'item_read' is complete, so adds it to the list
                if dict_key == 'id' and 'id' in item_read and item_read['id']:   # if 1st or 2nd are False it won't eval the 3rd
                    # validates that all required fields are there
                    if validate_loot_item(item_read): 
                        dest_list.append(item_read)
                    item_read = {}

                if not dict_value: continue         # skipt the rest if value is empty

                # some values (with strings) needs to be turned into lists
                if '|' in dict_value:
                    dict_value = [l.strip() for l in dict_value.split('|') if l]

                # needs numbers for these
                if dict_key in ('modifier','action_chance','cooldown'):
                    if dict_value.strip():
                        dict_value = int( dict_value.strip() )
                    else:
                        dict_value = 0

                item_read[ dict_key ] = dict_value


    # will lload all the strings from ascii_strings.txt into encounters
    def process_ascii_strings( file_name ):
        print(f"dbg: {whoami()}")
        # open the file
        with open(file_name,'r') as file:
            # read from the file line by line in a for loop
            for line in file.readlines():
                # if starts with '#' you don't need it, its a comment
                if line[:1] == '#':       # the line is a comment, ignore it
                    continue
                elif not line:  # line==''
                    continue
                # encounter = a test that you want
                elif line.find('=') > 0:
                    # you're gonna strip the line - so you get rid of all end of flies and spaces from it
                    line.strip()
                    # break it into a key and value
                    #dict_key = line[:line.find('=')].strip().lower()
                    dict_value = line[line.find('=')+1:].strip().lower()
                    # test you actualy have a string and is not empty
                    if dict_value:
                        # you're gonna add 'a text that you want' to th encounters[] list
                        encounters.append( dict_value )


    
    # prints ascii text given as a parameter - might use a typewriter or not // or maybe something even cooler
    def print_ascii( text ):
        #typewriter( text, )
        print( text )


    # prints the story text given as a parameter - used for all stories, most likely with a typewritter
    def print_story( text ): 
        typewriter( text, delay=0.01 )

    
    # it will scan a file for an ascii art and a "story = ", extract them 
    # and then it will print the ascii art and the story
    def print_ascii_and_story_from_file( file_name ):
        #file_name = 'ascii_game_start.txt'
        flag_record_story = False   # once True, all next lines will be added to the story, provided they are not comments
        ascii_text = ''
        story = ''
        with open(file_name,'r') as file:
            for line in file.readlines():
                line.strip()
                if line[:2] == '##':        # collects the lines for the ascii image
                    ascii_text += line 
                elif line[:1] == '#':       # the line is a comment, ignore it
                    continue
                # if it was flagged to record the story it will just add every new line to the story, including empty lines
                elif flag_record_story:
                    story += line   #.rstrip()  # .replace("\\n",'\n')
                # when it finds the 'story = ', then it will start recording the story from that point
                elif line.find('=') > 0 and line[ :line.find('='):].lower().strip() == 'story' :
                    flag_record_story = True                # flag to say that from here all lines read that are nit comments will be added to the story
                    story = line[ line.find('=')+1:]        # everything after the '='
                    story = story.strip()                   # strip leading and trailing spaces and new lines
                    story = story.replace("\\n",'\n')       # unescapes new lines in the story string
                elif not line.strip(): None         # ignore empty lines bfore the 'story= ' fragment
                else:
                    if line: print(f'err=> {whoami()}: shouldnt run, line is "{line}"')

        # print the ascii image
        print_ascii( ascii_text )
        
        # print the story - typewritter
        print_story( story )



    # will print the game start ascii and the story
    def game_print_start():
        print(f"dbg: {whoami()}")
        # read from text file
        # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of  notmal print
        print_ascii_and_story_from_file( 'ascii_game_start.txt' ) 


    # will print the game end ascii and the story // difere
    def game_print_end( player_won = False ):
        print(f"dbg: {whoami()}")
        # read from text file -- depending on player_won variable you check read differemt files
        # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of notmal print
        if player_won: 
            print_ascii_and_story_from_file( 'ascii_game_win.txt' ) 
        else: 
            print_ascii_and_story_from_file( 'ascii_game_loose.txt' ) 


    # prints the text for the encounter, the first things after enters a new map tile
    def print_game_encounter():
        print(f"dbg: {whoami()}")
        # clear screen to start from the top
        clear_screen()
        # draw a chance string from encounters and print it using 'print_story()' instead of print()
        from random import choice
        text = choice( encounters )
        print_story(text)


    ## loads everything from files
    def game_setup():
        
        # sanity check - make sure all the files exist 
        from os.path import exists as file_exists
        if not file_exists(ascii_file_items) \
            or not file_exists(ascii_file_strings) \
            or not file_exists(ascii_file_game_start) \
            or not file_exists(ascii_file_game_win) \
            or not file_exists(ascii_file_game_loose):
                print("Unfortunately you're missing some data files (ascii text files) required by the game. \nPlease consult the developers of the application")
                exit()
        # check theres at least a monster and an event file
        from os import listdir, getcwd
        from os.path import isfile, join
        curent_dir = getcwd()
        if not [f for f in listdir(curent_dir) if f[:len(ascii_file_stem_monster)].lower()==ascii_file_stem_monster] \
            or not [f for f in listdir(curent_dir) if f[:len(ascii_file_stem_event)].lower()==ascii_file_stem_event]:
                print("Unfortunately you're missing some data files (ascii text files) required by the game. \nPlease consult the developers of the application")
                exit()

        # load items in list -- validate_monster will check the items are in the list
        process_ascii_loot(ascii_file_items, loot_items)

        # load monsters from files
        load_files(ascii_file_stem_monster, process_ascii, monsters)

        # load events from files
        load_files(ascii_file_stem_event, process_ascii, events)

        # load flavor strings (foud youself into a clearing, departing the lcerang, etc)
        process_ascii_strings( ascii_file_strings )
        
        # for debug
        from pprint import pprint
        print(f'\n\n\nItems: '+'='*70)
        pprint(loot_items)
        print(f'\n\n\nMonsters: '+'='*70)
        pprint(monsters)
        print(f'\n\n\nEvents: '+'='*70)
        pprint(events)



    ## the game starts, initializes the player
    ## on restart it won't ask for name anymore     //# todo: the restart game feature
    def game_player_reset( player_name = 'Player' ):
        # reset player data
        player_data = {
            'name'   : player_name,
            'hp'     : 30,
            'atk'    : 5,
            'def'    : 5,
            'lives'  : 1,             # potions of revival
            'weapon' : {},
            'armor'  : {},
            'items'  : [],            # list of owned items - list of dictionaries
            'killed_monsters' : [],   # list of killed monsters (just their names)
            'score'  : 0,             # keeps score of the player
        }


    # displays a list of choices for the user to pick from
    # will build a list of player choices from the encounter (monster/event), items, etc
    # but will display only those appropriate for the stage
    # situation: none, monster, situation
    # moster_event: is the actual mosnter or event teh player has to deal with (dict)
    # stage: before, after // the 'before' with monster will develop into a warning, then a fight
    def game_player_show_choices( situation, monster_event, stage ):
        # dbg: sanity check
        if situation in ['monster','event'] and not monster_event:
            print_err(f'situation={situation}, stage={stage}, monster_event={monster_event}')
            #print(f'err=> {whoami()}: situation={situation}, stage={stage}, monster_event={monster_event}')
            #exit()

        player_choices = []
        no_ord = 0
        # add the situation choices - fight
        if situation == 'monster' and stage == 'before':
            no_ord=+1
            option = {}
            option['prompt']    = f'{no_ord}. Fight'
            option['key']       = f'{no_ord}'
            option['call']      = 'game_action_fight'
            option['param']     = monster_event
            player_choices.append(option)
        # add the event choices
        if situation == 'event' and monster_event.action:
            no_ord=+1
            option = {}
            option['prompt']    = f'{no_ord}. '+monster_event.action
            option['key']       = f'{no_ord}'
            option['call']      = 'game_action_event'
            option['param']     = monster_event
            player_choices.append(option)
        # add the item choices - teleport, petrify, sleep, 8-ball
        for item in player_data.items: 
            # checks if the item has action_prompt, has the same stage (before/after fight) and is  not on cooldown
            if 'action_prompt'      in item \
            and (not 'action_stage' in item or item('action_stage') == stage) \
            and (not 'cooldown'     in item or item['cooldown']==0):
                no_ord=+1
                option = {}
                option['prompt']    = f'{no_ord}. '+item['action_prompt']
                option['key']       = f'{no_ord}'
                option['call']      = 'game_action_item'
                option['param']     = item
                player_choices.append(option)
        # add the leave map tile choices
        no_ord=+1
        option = {}
        option['prompt']    = f'{no_ord}. Go back into the forest and continue your exploration'
        option['key']       = f'{no_ord}'
        option['call']      = 'game_new_tile'
        option['param']     = {}
        player_choices.append(option)
        
        # dbg: sanity check - if no_ord >= 10 then its gonna have problems, 10 is basically 2 symbols 1 and 0, if needed you might use letters, like [F]ight
        if no_ord >= 10: print_err( f'no_ord is more tha 9. this will create problems. {nr_ord}' )

        # display the choices for the user to select
        allowed_answers = ''
        for option in player_choices:
            #print( '\t'+option['prompt'] )
            typewriter( '\t'+option['prompt'] )
            allowed_answers += option['prompt']
        

        if situation == 'monster' and stage == 'before': 
            answer_time = monster_fight_total_time
            warn_time   = monster_fight_warn_time
            if 'warn' in monster_event and monster_event['warn']:
                warn_text   = monster_event['warn']
            else:
                warn_text   = "The creature noticed you and is hurrying towards you. \nYou should really do something, or you're toast"
        else:
            answer_time, warn_time, warn_text = 0, 0, ''

        # ask for an answer, then get answer
        typewriter( '\n\033[1;35mWhat do you choose? :\033[0m ' )
        answer = get_answer( allowed_answers, answer_time, warn_time, warn_text )

        # if the player didn't aswer in time and it got shreded
        # update its hp with 0 and will be handled later on
        if answer == 'failed': 
            if situation == 'monster' \
            and 'losing' in monster_event \
            and monster_event['losing']:
                typewriter( monster_event['losing'] )

            # display you got killed message if any
            player_data['hp'] = 0





    # the player encounters a monster
    def game_encounter_monster( monster_attack_first = False ):
        print(f"dbg: {whoami()}")
        # todo: build the function


    # player encounters encounters a new event
    def game_encounter_event():
        print(f"dbg: {whoami()}")
        # todo: build the function


    # if theres no event or monster to encounter on this tile
    def game_encounter_none():
        print(f"dbg: {whoami()}")
        # todo: build the function
        # nothng to do, empty clearing, show choices to user
        game_player_show_choices( situation = 'none' )


    # will loopt through the items in players inventory and decrement their cooldown value
    def player_decrement_items_cooldown():
        for item in player_data.items:
            if 'cooldown' in item and item['cooldown'] > 0: 
                item['cooldown'] -= 1


    # player travel to a new tile (or teleported to a new tile)
    def game_new_tile( monster_or_event = True ):
        print(f"dbg: {whoami()}")
        # todo: everything happens here
        # print ascii? and story (random?) for scenery
        print_game_encounter()
        # all items in inventory are checked and their cooldown are decremented
        player_decrement_items_cooldown()
        # if monster_or_event roll for a monster or for event, 
        if chance_encounter_monster >= dice_roll(10):
            game_encounter_monster()
        elif chance_encounter_event >= dice_roll(10): 
            game_encounter_event()    
        else: 
            game_encounter_none()
        # then roll for which monster or which event to use
        # action teh event or the monster
        # afer that, if player HP > 0 then check options after the fight
        # action option after the fight if any 
        # exit function after the player cjose which way to go 
        # (it goes back to the loop where it will run another game_start_tile)


    # checks if player can jump to a new tile // make sure he's still alive for one
    def player_can_do_new_tile():
        player_still_alive = \
                player_data['hp']    > 0   \
            and player_data['lives'] > 0
        return player_still_alive


    # starts the game, prints the story and get on with the next tile in a loop
    def game_start():
        print(f'dbg: {whoami()}')

        # todo: get player name
        player_name = ''

        # reste player data - the plaer record with items, stats and score
        game_player_reset( player_name )

        # print game start ascii and story
        game_print_start()
        
        # throw tiles at the player in a loop
        while player_can_do_new_tile():
            game_new_tile()
            # debug: kill player
            player_data['hp'] = 0
        
        # print game over ascii and story
        game_print_end()

        # todo asks the user if he'd like to start again ?
        # it should be in a loop only for this purpose


    ######################################################################
    ##  here, the application starts
    ######################################################################

    # loads all the data from the ascii files // if missing required files it should kill the app
    game_setup()
    # starts the game
    game_start()





# entry point into the app
warrior_king_of_tristram = the_game()
