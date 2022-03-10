

# The Warrior King of Tristram is very old & close to death. He has instructed all warriors to prove their strength by bringing back the head of each monster including that of the largest Dragon in the Tristram Kingdom, if you complete this task you will become the new King of Tristram.
# "Your name" has defeated all of the monsters in the land of Tristram!
# The First King of Tristram celebrates your victory in front of the Tristram Castle in a special Coronation Ceremony! You are now the new King!

####  monster ############
# id        = batman                                         # used in code, one word (could use snake_case)
# name      = The Batman                                     # the name, used in code - monster name
# ascii_img =                                                # the ascii image to be printed for the monster
#
# encounter = You notice a strange person blah blah blah     # the encounter description 
# warn      = Luckily he tripped,                            # the warning text you get if you don't take action soon
# winning   = You defeated the beast                         # text display when you killed the monster 
# losing    = The beast killed you                           # text displaied when you were killed
#
# hp        = 10                       # base hp for the monster
# atk       = 3                        # base attack for the monster
# def       = 4                        # base defence fro the monster
#
# chance    = 5                        # chance of encountering the monster (out of 10)
# score     = 3                        # the score you get for defeting him
# drops     = bedroll:2, shuriken:8    # list of loot items [['',2], ['',]] it drops with what chance for each to drop (out of 10) - ex: 2 of 10 for shuriken to drop
#
# petrified = False                    # while in game, it will be set to True when petrified, which will add it to the list of kills, but no loot



#### events ##############
# id                  = fountain
# name                = Exquisite Fountain
# ascii_img           = the ascii image - will be printed
#
# story               = You have arrived on the land of a rich family, there is an attractive water fountain with suspiciously glinting objects
# action              = Investigate the suspicious objects
# chance_event        = 3 
#
# chance_effect       = 8
# affected_stat       = HP
# modifier            = 10
# action_func         = apply_<func>
#
# drops               = 8ball:2, rusty coin:8
# drop_text_success   = You opened the small shining box and received: @@.
# drop_text_fail      = You open the small shiny box and discover is empty.


#### loot_item ###########
# id =                # an id name, used in code, ex: magic_flute
# name =              # nice name to be displayed at times, like: Magical Flute
# description =       # description that will be shown, ex: An extremly intricate flute that plays tunes out of this world 
# type =              # special, used in code, one of these: weapon, armor, potion, loot, junk
#
# stat_effect =       # the stat that it will affect, if it affects a stat: HP, ATK, DEF
# modifier =          # the amount it will increase/decrease the stat with: 10, +3, -1
#
# action_stage  =     # the stage when the item can be used in relation with the fight/event: before, after
# action_func =       # used in code, the special action function that will be called with the item: sleep, teleport
# action_chance =     # what chance out of 10 will the effect have to go through: 3
#
# action_prompt =     # the text that the user will see and choose to execute the objects effect: Take a moment and play the flute
# action_success =    # text to be displaied when the effect is succesfull: The birds have heard your song and gather around you
# action_failed =     # a list of funny text to be chosen from when the item fails to do its action - for the 8ball, separate texts by "|"
#
# cooldown =          # how often can it be used? once every how many clearings? ex: 3 - can be used again after the third clearing




## some ascii art links
## https://textart.io/art/tag/house/1
## https://www.asciiart.eu/buildings-and-places/houses
## https://textart.io/#


# prints a dctionary nice, in columns
#   "\n".join("{}\t{}".format(k, v) for k, v in dictionary.items())
# same but for sorted
#   "\n".join("{}\t{}".format(k, v) for k, v in sorted(dictionary.items(), key=lambda t: str(t[0])))


# todo: a function game_random_text('encounter/leaving/defa_warn') -- couold be used in game_player_show_choices()
# todo: a pretier display of the ascii art panels, like droping (shredder) or blowing up, fade from another, etc
# todo: trength modifiers for mosters, makes thema a bit more challenging
# todo: the ascii_strings.txt could hold strings for everythingreally, like teh default text, the leave texts, 
# todo:     i could ahve a dict of lists the function to retrieve a random list item for a certain dict  branch








def the_game():

    # some config data
    ascii_file_stem_monster  = 'ascii_monster_'        # how all the moster files start
    ascii_file_stem_event    = 'ascii_event_'          # how all the events files start

    ascii_file_items         = 'ascii_loot_items.txt'  # holds all the items
    ascii_file_strings       = 'ascii_strings.txt'     # holds the strings for encounters
    
    ascii_file_game_start    = 'ascii_game_start.txt'
    ascii_file_game_win      = 'ascii_game_win.txt'
    ascii_file_game_lose     = 'ascii_game_lose.txt'

    chance_encounter_monster = 5        # 7 out of 10 to fight a monster
    chance_encounter_event   = 4        # 5 out of 10 to have an event
    #chance_encounter_none = 2          # 2 out of 2 to have nothing special in the encounter

    player_max_hp            = 30       # set hp value for player - used in resets and poption
    player_inventory_limit   = 0        # no limit for now

    monster_fight_warn_time  = 5        # time to answer untill waring
    monster_fight_total_time = 10       # time to answer untill failed
    
    use_typewritter_effect   = True
    print_debug_messages     = True
    dont_use_msvcrt          = True
    color_for_debug_messages = 35       # 30-black, 31-red, 32-green, 33-yellow, 34-blue, 35-purple, 36-cyan, 37-white

    # the player record - hods everything about the player
    player_data = {
        'name'              : "",
        
        'hp'                : player_max_hp,
        'atk'               : 5,
        'def'               : 5,
        
        'lives'             : 1,      # potions of revival
        'weapon'            : {},     # the weapon it has - has the 'modifier' key
        'armor'             : {},     # the armor it has - has the 'modifier' key
        'items'             : [],     # list of owned items (list of dicts)
        
        'killed_monsters'   : {},     # killed monsters { monster : count, }
        'score'             : 0,      # keeps score of the player

        'flag_guarantee'    : False,  # when True, next monster will be one you don't have
        'flag_teleporting'  : False,  # if set to True it will teleport away from the 
        'flag_leaving'      : False,  # will be set to True to leave the loof of choices
    }

    monsters        = []     # list of dictionaries (dicts)
    events          = []     # list of events (dicts)
    loot_items      = []     # list of items (dics)
    encounters      = []     # list of encounters strings 

    highscore       = []     # list of highscore (dicts) { name, value, date }

    
    


    # action_functions is down because it has to be after the functions


    # useful in debug, tells the name of the calling function
    def whoami( lvl=0 ):
        import sys
        return sys._getframe(1+lvl).f_code.co_name


    # prints a problem message in red and includes the function where the error hapened
    def print_err( message ):
        text_to_print = f'\033[1;31merr=>{whoami(1)}: '+message+'\033[0m'
        print(text_to_print)


    # print a debug message in grey to denugging purposes
    def print_dbg( message='' ):
        if print_debug_messages:
            text_to_print = ': '+message if message else ''
            text_to_print = f'\033[1;{color_for_debug_messages}mdbg=>{whoami(1)}' + text_to_print +'\033[0m'
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

    # returns a key but waits the user to press it -- not to be used in loops
    def input_key():
        result = input()

    # play a beeping sound, if list is provided must be a list of tuples/list of (tone,duration)
    # they will be played in succession
    # def beep( duration = 100, frequency = 2500):
    #     # Set Frequency To 2500 Hertz
    #     # Set Duration To 1000 ms == 1 second
    #     import winsound
    #     winsound.Beep(frequency, duration)


    # will play the list of bees provided, can be stoped with space/enter, like the typewritter
    # list_of_beeps must be a list of (tone,duraction)
    # def beep_from_list( list_of_beeps = [], stop_on_enter_space = True ):
    #     # will use beep to play 
    #     for beep_pair in list_of_beeps:
    #         tone     = beep_pair[0]
    #         duration = beep_pair[1]
    #         beep( duration, tone )
    #         if stop_on_enter_space and inkey() in [32,13]: break


    # delay can be changed, can have 3 x delay on space, can have random (1 in 5) 3 x delay while writing the text
    # unsing inkey, i could implement a printall with space/esc (after space clear buffer)
    def typewriter( text:str, delay=0.01, newline=True, space_breaks=False, random_breaks=True, rush_on_enter_or_space=True ):
        from time import sleep
        from random import randint
        should_break = False
        rush_through = False
        if not use_typewritter_effect: rush_through = True      # apply global game setting
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


    # the function tests the chance agains a dice roll of 10, test teh chance for x out of 10 
    def chance_it( chance_to_test ):
        # chance of 2 out of 10, roll for a number higher than 8
        result = dice_roll(10) >= (10-chance_to_test)
        return result


    # answer must be from answer_list, will return 'failed' if no answer was given
    def get_answer(answer_list, answer_time=0, warn_time=0, warn_text='', print_the_answer = True, prompt_text=''):
        print_dbg(f" ~ answer_list='{answer_list}', answer_time={answer_time}, warn_time={warn_time}")
        tick = 0.1
        tick_answer = answer_time/tick
        tick_warn = warn_time/tick
        tick_count = 0
        typewriter( prompt_text, newline = False)   
        from time import sleep 
        while answer_time==0 or (answer_time!=0 and tick_count<tick_answer):
            sleep(0.1)
            tick_count += 1
            answer = inkey()    
            #if o got allowed answer the return char
            if chr(answer) in answer_list:
                if print_the_answer: 
                    print( chr(answer) )    # needs to jump
                return chr(answer)
            elif warn_time and warn_text and tick_count == tick_warn:
                print("\r"+" "*50)      # delay=0.01
                typewriter(warn_text)
                typewriter( prompt_text, newline = False)   # display promp again
            elif answer == 27:      # escape was pressed
                print( '<ESC>', end='' )
                return 'failed'
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
        print_dbg(f" ~ file_name = '{file_name}'")
        with open(file_name,'r') as file:
            item_read = {}     # =dict()
            ascii_img = ""
            for line in file.readlines():
                #line = line.strip()        # removes \n -- i do it lower where i read the key/value pair

                if not line.strip(): 
                    continue

                elif line[:2] == '##':        # collects the lines for the ascii image
                    ascii_img += line

                elif line[:1] == '#':       # the line is a comment, ignore it
                    continue

                elif line.find('=') > 0:            # if the line is a key = value pair
                    line = line.strip()
                    dict_key = line[:line.find('=')].strip().lower()
                    
                    if dict_key == 'drops':     # if it's the 'drops' line, builds a list of lists'
                        s = line[line.find('=')+1:].strip()
                        dict_value = [ l.split(':') for l in s.split(',') if l ]
                        for t in dict_value: 
                            t[0] = t[0].strip()
                            if len(t)==2: t[1] = int(t[1])
                    
                    else:                       # just the normal value for it
                        dict_value = line[line.find('=')+1:].strip().replace('\\n','\n')

                        if dict_key in ('hp','atk','def','modifier','cooldown','chance','score','chance_effect','chance_event'):
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


            item_read['ascii_img'] = ascii_img 

            # for debug purposes, adds a dbg_filename property to the dictionary, in case theres an issue to find the source
            item_read['dbg_filename'] = file_name

            # validate the required fields are in there
            if validate_monster_event_item(item_read):
                dest_list.append(item_read)



    # reads the ascii_loot_items.txt and build a list of dictionaries for every item, with its properties
    def process_ascii_loot(file_name,dest_list):
        print_dbg()
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
        print_dbg()
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
                    dict_value = line[line.find('=')+1:].strip()
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
        print_dbg()
        # read from text file
        # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of  notmal print
        print_ascii_and_story_from_file( ascii_file_game_start ) 


    # will print the game end ascii and the story // difere
    def game_print_end( ):
        print_dbg()
        
        # player won if killed all monsters and is still alive
        player_still_alive = player_data['hp'] > 0 or player_data['lives'] > 0
        player_killed_all = ( len(monsters) == len(player_data['killed_monsters']) )
        player_won = player_still_alive and player_killed_all

        if player_won: 
            print_ascii_and_story_from_file( ascii_file_game_win ) 
        else: 
            print_ascii_and_story_from_file( ascii_file_game_lose ) 


    # prints the text for the encounter, the first things after enters a new map tile
    def game_print_encounter():
        print_dbg()
        # clear screen to start from the top
        #clear_screen()
        # draw a chance string from encounters and print it using 'print_story()' instead of print()
        from random import choice
        text = choice( encounters )
        print_story(text)


    ## loads everything from files
    def game_setup():
        print_dbg()

        # sanity check - make sure all the files exist 
        from os.path import exists as file_exists
        if not file_exists(ascii_file_items) \
            or not file_exists(ascii_file_strings) \
            or not file_exists(ascii_file_game_start) \
            or not file_exists(ascii_file_game_win) \
            or not file_exists(ascii_file_game_lose):
                print("Unfortunately you're missing some data files (ascii text files) required by the game. \nPlease consult the developers of the application")
                exit()
        # check theres at least a monster and an event file
        from os import listdir, getcwd
        #from os.path import isfile, join
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
        # from pprint import pprint
        # print(f'\n\n\nItems: '+'='*70)
        # pprint(encounters)
        # print(f'\n\n\nItems: '+'='*70)
        # pprint(loot_items)
        # print(f'\n\n\nMonsters: '+'='*70)
        # pprint(monsters)
        # print(f'\n\n\nEvents: '+'='*70)
        # pprint(events)



    ## the game starts, initializes the player
    ## on restart it won't ask for name anymore     //# todo: the restart game feature
    def game_player_reset( player_name = 'Player' ):
        print_dbg()

        # reset player data
        player_data = {
            'name'              : player_name,
            
            'hp'                : player_max_hp,
            'atk'               : 5,
            'def'               : 5,
            
            'lives'             : 1,            # potions of revival
            'weapon'            : {},           # the weapon it has - has the 'modifier' key
            'armor'             : {},           # the armor it has - has the 'modifier' key
            'items'             : [],           # list of owned items (list of dicts)
            
            'killed_monsters'   : {},     # killed monsters { monster : count, }
            'score'             : 0,            # keeps score of the player

            'flag_guarantee'    : False,    # when True, next monster will be one you don't have
            'flag_teleporting'  : False,    # if set to True it will teleport away from the 
            'flag_leaving'      : False,    # set tot True to leave the loop of choices
        }



    # will spawn a monster from the list of monsters
    def game_spawn_monster():
        print_dbg()

        new_monster = {}
        while not new_monster:
            for mon in monsters: 
                #-- if its guarantee, must be a monster that player hasn't killed before
                if player_data['flag_guarantee'] and isinstance(player_data['killed_monsters'],dict) \
                and player_data['killed_monsters'].get(mon['name'],0) : 
                    continue
                #-- get the chance of spawning
                mon_chance = mon.get('chance',5)    # if not defined, 50/50
                if chance_it( mon_chance ):
                    new_monster = mon.copy()
                    player_data['flag_guarantee'] = False
                    break
        
        if not new_monster or not isinstance(new_monster, dict): 
            print_err(f"using random.chance() on monsters[] (len={len(monsters)}) didn't get a dict={new_monster}")
        
        return new_monster


    # will spawn a new event that will be returned
    def game_spawn_event():
        print_dbg()

        #-- gets an event from the list of events base on 'chance_event'
        new_event = {}
        while not new_event:    # isinstance(new_event, dict):
            for ev in events:
                ev_chance = ev['chance_event'] if 'chance_event' in ev and ev['chance_event'] else 5
                if chance_it( ev_chance ):
                    new_event = ev.copy()   # a copy of the event
                    break

        if not new_event or not isinstance(new_event,dict): 
            print_err(f"using random.chance() on events[] (len={len(events)}) didn't get a dict={new_event}")

        # returns a copy of the dictionary
        return new_event


    # will read the list of drops from the monster/event and randomly spawn one for the player
    def game_spawn_loot_item( monster_event ):
        print_dbg(f" ~ monster_event={monster_event}") 
        #-- sanity check, param must be dict
        if not isinstance(monster_event,dict): 
            print_err(f'parameter monster_event doesnt seem to be dict = {monster_event}')

        #-- monster/event must have the 'drops' list
        if monster_event.get('drops',[]) and isinstance(monster_event['drops'], list):
            # drops is a list of lists [ ['axe',2], ['coin',8] ]
            # goes throigh the list and runs a dice on the items so see what drops
            drop_item = {}

            for item in monster_event['drops']:     # ['item_id', chance]
                #chance = monster_event['drops'][1] if isinstance(monster_event['drops'][1],int) else 10
                item_id = item[0]
                chance  = item[1] if len(item)==2 else 5

                if chance_it(chance) :
                    #item_id        = item[0]           # monster/event holds the list of the items ids
                    item_from_loot = [ it for it in loot_items if it['id'] == item_id ]  
                    # should return only one, if not, we have a problem
                    if len(item_from_loot) != 1:
                        print_err(f"searching in loot for id='{item_id}' got {len(item_from_loot)} matches: {item_from_loot} list:{loot_items}")
                    # copy the item
                    drop_item = item_from_loot[0].copy()

                    # play the success text
                    if monster_event.get('drop_text_success',''):
                        #-- in the text, replaces @@ with the name of the item
                        text_success = monster_event['drop_text_success'].replace('@@',drop_item['name'])
                        typewriter( text_success+'\n' )
                    # return the obtained item
                    return drop_item

            #-- check if nothing dropped
            if not drop_item and monster_event.get('drop_text_fail',''):
                if not drop_item.get('name',''): 
                    print_err(f"don't have a 'name' for drop_item={drop_item}, item_id={item_id}, monster['drops']={monster_event['drops']}")
                text_fail = monster_event['drop_text_fail'].replace('@@',drop_item.get('name','thing'))
                typewriter( text_fail+'\n' )

        # return an empty dict
        return {}



    # will add the item to player's inventory, this is where i check the size of the inventory    
    def game_add_item_to_player( drop_item ):
        print_dbg(f" ~ drop_item={drop_item}") 

        # theres a limit on the inventory, and the item list is up to the inventory
        if drop_item['type'] == 'loot':

            if player_inventory_limit          \
            and isinstance(player_data['items'],list)    \
            and len(player_data['items'])==player_inventory_limit:
                # player will be asked to remove something or abandon this drop
                item_list = [ str(item) for item in player_data['items'] ]                  # ['potion','coin','head']
                item_list = [ str(i+1)+'.'+item_list[i]+'\n' for i in range(len(item_list)) ]    # ['1.potion','2.coin','3.head']
                text_inv  = ''.join( item_list )

                answerlist = '0'.join( [str(i+1) for i in range(len(item_list))] )       # '0123456..'

                typewriter('Your inventory is full. Thes erase the items: ')
                typewriter(text_inv)
                typewriter('Choose which to remove, or 0 to abandon this one: ')
                
                answer = get_answer(answerlist,)
                if answer == 'failed': answer = 0     # he chose escape, default to abandon

                # he discarded an item
                if answer > 0:
                    # player data[item] is a list of dictionaries, to access the name of 3nd one: player_data['items'][2]['name']
                    typewriter(f"You chose to discard: {player_data['items'][answer-1]['name']}")
                    player_data['items'].pop( answer-1 )        # pop the item off using the order of the list (answer-1)
                else:
                    typewriter(f"You discarded: { drop_item['name'] }")

            # if the list doesn't exist, we create it
            if not isinstance(player_data['items'],list): 
                player_data['items'] = []
                #player_data['items'].append( drop_item )
            # if theres room in the inventory
            elif not player_inventory_limit or len(player_data['items'])<player_inventory_limit:
                player_data['items'].append( drop_item )    # adds the new item

        elif drop_item['type'] == 'potion':
            player_data['lives'] += 1
            typewriter(f"You stash the '{ drop_item['name'] }' potion in your pocket. Gotta have it on hand.")

        elif drop_item['type'] == 'weapon':
            if not isinstance( player_data['weapon'], dict ) \
            or not player_data['weapon'].get('modifier','') \
            or player_data['weapon']['modifier'] < drop_item['modifier']:
                player_data['weapon'] = drop_item
                typewriter(f"You pick up the '{ drop_item['name'] }' and attach it to you belt. \nIt's swinging and makes you loose your balance every now and then.")

        elif drop_item['type'] == 'armor':
            if not isinstance( player_data['armor'], dict ) \
            or not player_data['armor'].get('modifier','') \
            or player_data['armor']['modifier'] < drop_item['modifier']:
                player_data['armor'] = drop_item
                typewriter(f"You equip the '{ drop_item['name'] }'. It's heavy and makes you clumsy but you feel reasured by it's sturdiness.")

        elif drop_item['type'] == 'junk':
            typewriter(f"You pick up a '{ drop_item['name'] }'. You need to keep this, you never know when you'll need it.")

        else:  # shouldn't run
            print_err(f"this item type hasn't been handled '{drop_item['type']}', {drop_item}")

        # addc new line
        print()


    # starts the fighting loop until monster or player died
    # if player died tries to revive him
    # updates player HP
    # if monster died adds him to kill_list
    def game_action_fight( monster, player_attacks_first=True ):
        print_dbg(f" ~ monster={monster}")
    
        # compute the atack and the defence
        player_atk = player_data['atk'] + player_data['weapon'].get('modifier',0)
        #   player_data['weapon']['modifier'] if isinstance( player_data['weapon'], dict ) and  else 0            
        player_def = player_data['def'] + player_data['armor'].get('modifier',0)
        #   player_data['weapon']['modifier'] if isinstance( player_data['armor'], dict ) else 0
        monster_atk = monster['atk']
        monster_def = monster['def']

        # text before the battle starts:
        text_battle = f"\nYou (Hp: {player_data['hp']} / Atk: {player_atk} / Def: {player_def}) face the monster (Hp: {monster['hp']} / Atk: {monster_atk} / Def: {monster_def} ) in combat.\n"
        typewriter( text_battle )
        
        # while player and moster are still alive
        while monster['hp'] > 0 and player_data['hp']>0:
            #player turn
            roll_player     = dice_roll()
            atk_player      = player_atk + roll_player
            roll_monster    = dice_roll()
            def_monster     = monster_def + roll_monster
            hp_hit          = atk_player - def_monster if atk_player > def_monster else 0
            text_battle     = f"You roll {roll_player}. \t\t\tYou attack monster with {atk_player}\n"
            text_battle    += f"Monster rolls {roll_monster}. \t\tHe defends with {def_monster}\n"
            monster['hp']   = monster['hp'] - hp_hit if monster['hp'] >= hp_hit else 0
            text_battle    += f"Monster takes a hit of {hp_hit}. \tMonster's HP is {monster['hp']} \n"
            typewriter(text_battle)
            # if monster dies, exit loop
            if monster['hp'] == 0: break
            # monster attacks
            roll_monster    = dice_roll()
            atk_monster     = monster_atk + roll_monster
            roll_player     = dice_roll()
            def_player      = player_def + roll_player
            hp_hit          = atk_monster - def_player if atk_monster > def_player else 0
            text_battle     = f"Monster rolls {roll_monster}. \t\tHe attacks you with {atk_monster}\n"
            text_battle    += f"You roll {roll_player}. \t\t\tYou defend with {def_player}\n"
            player_data['hp'] = player_data['hp'] - hp_hit if player_data['hp'] >= hp_hit else 0
            text_battle    += f"You take a hit of {hp_hit}. \t\tYour HP is {player_data['hp']} \n"
            typewriter(text_battle)

        # print message for you losing or winning
        # if you died, try to revive - get the choices of moving on, or game over
        if player_data['hp'] == 0:
            typewriter( 'You lost the fight!' )
            # can you revive? 
            if player_data['lives'] > 0:
                player_data['lives'] -= 1
                typewriter( 'Luckly, you managet to sip a potion of restoration before you died.' )
                player_data['hp'] = player_max_hp

            else:   # you're really dead
                # losing message form monster
                typewriter( monster['losing'] )     # as in message for loosing against the monster

        # you're alive, monster is dead, print message, get loot
        else: 
            typewriter( 'You won the fight' )
            typewriter( monster['winning'] )    # message for winning against the monstter
            #-- add monster to kill_list
            player_add_monster_to_kill_list( monster )
            #-- drop item 
            drop = game_spawn_loot_item( monster )
            #-- if the monster dropped something i display the item name // for the fight
            typewriter(f"You search your oponents remains and discover { drop['name'] if drop else 'Nothing.' }")
            # if you have a drop and you have an inventory limit you ask to remove something
            if drop: game_add_item_to_player( drop )  # will add the drp to plater inventory - this is where i handle inventory size
            # thats it, move on



    # actions the option from the event
    def game_action_event( param_event ):
        print_dbg(f" ~ event={param_event}")

        #-- if it's an effect, applies the effect 
        if param_event.get('affected_stat','') :    # if affected stat is not empty
            ev_stat     = param_event.get('affected_stat',0)     # if event['affected_stat'] else 0
            ev_chance   = param_event.get('chance_effect',0)    # if event['chance_effect'] else 0
            ev_modifier = param_event.get('modifier',0)         # if event['modifier'] else 0

            # lets hope nothing breaks here, don't have any more time for teste now
            if chance_it(ev_chance):
                player_data[ ev_stat ] = player_data[ ev_stat ] + ev_modifier
                typewriter( f"Your {ev_stat} has changed to {player_data[ ev_stat ]}" )

        #-- if it's an item drop, spawn an item drop
        if  param_event.get('drops',[]):
            # try and get a drop
            item_drop = game_spawn_loot_item( param_event )
            # if drop succesfull the print message and add item to player
            if item_drop: 
                # if param_event.get('drop_text_success','') : 
                #     typewriter( param_event['drop_text_success'] )
                
                game_add_item_to_player( item_drop )  # will add the drp to plater inventory - this is where i handle inventory size
            else:
                if param_event.get('drop_text_fail','') : 
                    typewriter( param_event['drop_text_fail'] )
        
        # set a flag that the event is done so its action won't be presented as a choice to the user
        param_event['flag_event_is_done'] = True


    # adds the monster received a a parameter to the kill_list, also adds its score to player score
    def player_add_monster_to_kill_list( monster ):
        print_dbg()
        if  not isinstance(player_data['killed_monsters'],dict):
            player_data['killed_monsters'] = {}
        monster_id = monster.get('id')
        player_data['killed_monsters'][ monster_id ] = player_data['killed_monsters'].get(monster_id,0) + 1
        player_data['score'] = player_data.get('score',0) + monster['score']



    # will print the status on the screen
    def game_player_show_status():
        print_dbg()

        status_text = \
            f"=== Player stats:" \
            + f"\n= health    : ({player_data['hp']}/{ player_max_hp })" \
            + f"\n= Atack     : {player_data['atk']}" \
            + f"\n= Defense   : {player_data['def']}" \
            + f"\n= Weapon    : {player_data['weapon'].get('name','None')}" \
            + f"\n= Armor     : {player_data['armor'].get('name','None')}" \
            + f"\n= Potions   : {player_data['lives']}"
        
        status_text += f"\n=== Items in the bag:"
        if len(player_data['items'])==0:
            status_text += f"\n= None"
        else:
            for it in player_data['items']:
                item_name = it['name']
                status_text +=   f"\n= {item_name}"

        status_text += f"\n=== Monsters Killed:"
        if len(player_data['killed_monsters'])==0:
            status_text += f"\n= None"
        else:
            for mo, k in enumerate(player_data['killed_monsters']):
                #mon_id      = player_data['killed_monsters'][mo]['name']
                #mon_name    = [ mon['name'] for mon in monsters if mon['id'] == mon_id ]
                #mon_count   = player_data['killed_monsters'][mon_id]
                status_text += f"\n= {k} : {player_data['killed_monsters'][k]}"

        status_text += f"\n= Monsters remaining: { len(monsters) - len(player_data['killed_monsters']) }"

        status_text += f"\n=== Done!"

        typewriter( status_text+'\n' )



    # will just print messages, and set a flag_teleporting 
    def game_action_teleport(): 
        print_dbg()
        # the flag will be make the player to restat the map_tile
        player_data['flag_teleporting'] = True

    # this will set the flag_guarantee which will make sure that the next monster to spawn is one we didn't fight
    def game_action_guarantee():
        print_dbg()
        # guarantee that the next monster is a new type
        player_data['flag_guarantee'] = True


    # this is to petrify the monster
    def game_action_petrify( monster, item ):
        print_dbg(f" ~ monster_event={monster}")
        # get the item that has the petrify effect
        monster['hp'] = 0
        monster['petrified'] = True
        # well, technically he's been killed, so we'll just take the win
        player_add_monster_to_kill_list( monster )


    # this is the sleep mechanic, the player has a 50/50 chance to get his full health back or be attacked
    def game_action_sleep( item ):
        print_dbg()

        text_action_success = item.get('action_success','')
        text_action_failed  = item.get('action_failed','')

        if chance_it(5): # 50/50
            player_data['hp'] = player_max_hp
            typewriter( text_action_success )
        else: 
            typewriter( text_action_failed )
            monster = game_spawn_monster()
            game_action_fight( monster, False )



    # to execute the item's action
    def game_action_item( item, monster_event ):
        print_dbg(f" ~ item={item}, monster_event={monster_event}")

        action_chance = item.get('action_chance',10)    # if 'action_chance' in item else 10
        action_func   = item.get('action_func','')      # if 'action_func' in item else ''
        text_success  = item.get('action_success','')   # if 'action_success' in item else ''
        text_failed   = item.get('action_failed', '')   # if 'action_failed' in item else ''

        # if theres no function to execute, whats the point of the prompt/action
        if not action_func: 
            print_err(f"doesn't seem to have an action_func='{action_func}', item={item}")
            return 
        
        # based upon the cance, see if it will not happen
        if not chance_it(action_chance): 
            # not aplicable for the sleep mechanic
            if action_func != 'game_action_sleep': 
                typewriter( text_failed ) 

        else:       # it will happen
            # not aplicable for the sleep mechanic
            if action_func != 'game_action_sleep': 
                typewriter( text_success )  
            # couoldn't get eval() to work so i'm testing for each case and run it here
            action_func = action_func.lower()
            if False: None
            elif action_func == 'game_action_petrify':
                game_action_petrify( monster_event, item )
            elif action_func == 'game_action_guarantee':
                game_action_guarantee( item )
            elif action_func == 'game_action_teleport':
                game_action_teleport( item )
            elif action_func == 'game_action_sleep':
                game_action_sleep( item )
            else: # don't have any other function, show error
                print_err(f"unexpected action_func='{action_func}', item={item}")
        
        # get the cooldown value from the loot_item list
        orig_item = next((it for it in loot_items if it['id'] == item['id'] ), None)
        item['cooldown'] = orig_item['cooldown'] if isinstance(orig_item,dict) else 3



    # is executed from game_player_show_choices() when the user makes a choice // it runs a specific function
    def game_choice_action( action_func,  monster_event={}, func_param={} ):
        print_dbg(f" ~ action_func={action_func}, func_param={func_param}, monster_event={monster_event}")
        # test for each function that can be used and run the // tried using eval() but couldn't make it work for function inside another function
        if False: None
        elif action_func == 'game_action_fight':                # starts the fight loop with the monster
            game_action_fight( monster_event )
        elif action_func == 'game_action_event':                # is the action from the event
            game_action_event( monster_event )
        elif action_func == 'game_action_item':                 # calls a function iwth the item, it will do the item action with a chance of success, then display the succes/fail message
            game_action_item( func_param, monster_event )
        elif action_func == 'game_move_new_tile':               # jumps to a new tile
            player_data['flag_leaving'] = True
            #game_move_new_tile()
        elif action_func == 'game_player_show_status':          # displays the stats, the items, and killed monsters
            game_player_show_status()
        # err check
        else: print_err(f" the action_func={action_func} is not in the if/else branch")

        

    # displays a list of choices for the user to pick from
    # will build a list of player choices from the encounter (monster/event), items, etc
    # but will display only those appropriate for the stage
    # situation: none, monster, event
    # moster_event: the actual mosnter / event the player is dealing with atm (dict)
    # stage: before, after // the 'before' with monster will develop into a warning, then a fight
    def game_player_show_choices( situation, monster_event={}, stage='' ):
        print_dbg(f" ~ situation={situation}, stage={stage}, monster_event={monster_event}")
        
        # dbg: sanity check
        if situation in ['monster','event'] and not monster_event:
            print_err(f'situation={situation}, stage={stage}, monster_event={monster_event}')
            #print(f'err=> {whoami()}: situation={situation}, stage={stage}, monster_event={monster_event}')
            #exit()

        player_choices = []
        nr_ord = 0

        # add the situation choices - fight
        if situation == 'monster' and stage == 'before':
            nr_ord+=1
            option = {}
            option['prompt']        = f'{nr_ord}. Fight'
            option['key']           = f'{nr_ord}'
            option['action_text']   = ''                    # no need for it
            option['func_call']     = 'game_action_fight'
            option['param']         = monster_event
            player_choices.append(option)

        # add the event choices
        if situation == 'event' and monster_event.get('action','') \
        and not monster_event.get('flag_event_is_done',False):
            nr_ord+=1
            option = {}
            option['prompt']        = f'{nr_ord}. '+monster_event['action']
            option['key']           = f'{nr_ord}'
            option['action_text']   = ''            # will be handled by game_action_event( event )
            option['func_call']     = 'game_action_event'
            option['param']         = monster_event
            player_choices.append(option)
        # add the item choices - teleport, petrify, sleep, 8-ball

        #print( f"\n{type(player_data.items)} {player_data.items is list} {player_data.items}\n" )
        # seems that an empty [] is not recognized as a list
        if isinstance(player_data['items'],list):
            for item in player_data['items']: 
                # checks if the item has action_prompt, has the same stage (before/after fight) and is  not on cooldown
                if item.get('action_prompt','') \
                and (not item.get('action_stage','') or item.get('action_stage','') == stage) \
                and (not item.get('cooldown',0)      or item.get('cooldown',0)==0):
                    nr_ord+=1
                    option = {}
                    option['prompt']        = f"{nr_ord}. "+item['action_prompt']+f" ({item['name']})"
                    option['key']           = f'{nr_ord}'
                    option['action_text']   = item.get('action_success','')
                    option['func_call']     = 'game_action_item'    # item['action_func']
                    option['param']         = item
                    player_choices.append(option)

        if stage != 'before':
            # add the print your stats choice
            nr_ord+=1
            option = {}
            option['prompt']        = f'{nr_ord}. Review your stats and experience'
            option['key']           = f'{nr_ord}'
            option['action_text']   = ''    # "You take a look at yourself and realize, you're pretty fit."
            option['func_call']     = 'game_player_show_status'
            option['param']         = ''
            player_choices.append(option)

            # add the leave map tile choices
            nr_ord+=1
            option = {}
            option['prompt']        = f'{nr_ord}. Go back into the forest and continue your exploration'
            option['key']           = f'{nr_ord}'
            option['action_text']   = 'You take a deep breath and venture back into the forest'
            option['func_call']     = 'game_move_new_tile'
            option['param']         = ''
            player_choices.append(option)
        
        # dbg: sanity check - if nr_ord >= 10 then its gonna have problems, 10 is basically 2 symbols 1 and 0, if needed you might use letters, like [F]ight
        if nr_ord >= 10: print_err( f'nr_ord is more tha 9. this will create problems. {nr_ord}' )

        # display the choices for the user to select
        allowed_answers = ''
        for option in player_choices:
            #print( '\t'+option['prompt'] )
            typewriter( option['prompt'] )
            allowed_answers += option['key']

        # gets the timed values and warning text for the get_answer()
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
        prompt_text = '\033[1;35mWhat do you choose? :\033[0m '
        #typewriter( prompt_text, newline = False)
        answer = get_answer( allowed_answers, answer_time, warn_time, warn_text, prompt_text = prompt_text )
        print()     # add a newline

        # if the player didn't aswer in time and it got shreded
        # update its hp with 0 and will be handled later on
        if answer == 'failed': 
            # for monster fight display you got killed message if any -- message from the monster or general
            if situation == 'monster':
                # the message is from the monster record
                if monster_event.get('losing','') \
                and monster_event['losing']:
                    losing_text = monster_event['losing']
                else: 
                    losing_text = "The fiend attacks you relentlesly untill you succumb from your wounds."

                # the player hp goes to 0
                player_data['hp'] = 0
                # check if you can revive him, if no end the game
                print()
                typewriter( "You .. there wasn't even a fight to lose! Your HP is 0." )
                
                # can you revive? 
                if player_data['lives'] > 0:
                    player_data['lives'] -= 1
                    player_data['hp'] = player_max_hp
                    print()
                    typewriter( f"Luckly, you managet to sip a potion of restoration before you died. Your HP is {player_data['lives']}" )
                    print()
                    typewriter( 'After leaving you for dead, the monster went away into the forest.' )
                    print()

                else:   # you're really dead
                    # losing message form monster
                    typewriter( losing_text )     # as in message for loosing against the monster
                    player_data['flag_leaving'] = True  # doesn't need to go through show_choices('after') bit

        # now we handle the choices
        else: 
            # get the dictionary from the list of options that has the key == answer
            option = next((item for item in player_choices if item["key"] == answer), None)

            # dbg-sanity check: we shoudl have at least an option
            if option == None or not option: 
                print_err(f"we should have at least an option here, \noption = {option}, answer = {answer}, player_choices = \n{player_choices}")

            # the function to be called for the chosen option
            funct_to_call = option['func_call']
            funct_param   = option['param']

            if funct_to_call:
                game_choice_action( funct_to_call,  monster_event , funct_param )
            else: 
                print_err(f"after the choioce I don't run a function? answer={answer}, funct_to_call={funct_to_call}, funct_param={funct_param} ")

            # if theres an after effect text we'll print that
            if 'action_text' in option and option['action_text']:
                typewriter( option['action_text'] )
                print()



    # the player encounters a monster
    def game_encounter_monster( monster_attack_first = False ):
        print_dbg()
        #-- spawn the monster
        new_monster = game_spawn_monster()
        #-- prnt ascii
        print_ascii( new_monster['ascii_img'] )
        #-- print name and story
        #-- print message for the event
        print_story( '\033[1m'+new_monster['name']+'\033[0m' )
        print()
        
        if not new_monster.get('story',''): 
            print_err(f"monster doesn't seem to have story={new_monster}")

        print_story( new_monster.get('story','') )
        #-- player options before
        game_player_show_choices( 'monster', new_monster, 'before' )
        #-- if its flag_teleporting he chose to teleport away
        if player_data['flag_teleporting']:
            player_data['flag_teleporting'] = False        # reset
            return
        #-- player options after
        player_data['flag_leaving'] = False
        # loop over the choices untill he decides to leave or he's dead or he won
        while not player_data['flag_leaving'] and player_can_do_new_tile():
            # nothng to do, empty clearing, show choices to user
            game_player_show_choices( 'monster', new_monster, 'after' )



    # player encounters encounters a new event
    def game_encounter_event():
        print_dbg()
        #-- spawn an event
        new_event = game_spawn_event()
        #-- print ascii for the event
        print_ascii( new_event['ascii_img'] )
        #-- print message for the event
        print_story( '\033[1m'+new_event['name']+'\033[0m' )
        print()
        print_story( new_event['story'] )
        print()
        #-- player show choices
        
        # it will stay in a loop until the choice was made to leave
        player_data['flag_leaving'] = False
        # loop over the choices untill he decides to leave
        while not player_data['flag_leaving']:
            game_player_show_choices( 'event', new_event )


    # if theres no event or monster to encounter on this tile
    def game_encounter_none():
        print_dbg()
        # story for none
        story_text = "You arrive into a clear area where the grass is tall, the birds are singing in the trees and theres exacly nothing special about this place. You take a sit on a fallen log and grab a bite."
        print_story( story_text )
        print()
        # it will stay in a loop until the choice was made to leave
        player_data['flag_leaving'] = False
        # loop over the choices untill he decides to leave
        while not player_data['flag_leaving']:
            # nothng to do, empty clearing, show choices to user
            game_player_show_choices( 'none' )



    # will loopt through the items in players inventory and decrement their cooldown value
    def player_decrement_items_cooldown():
        print_dbg()
        #print(f"player_data.items = {player_data.items} {type(player_data.items)}")
        if isinstance(player_data.items,list) :
            for item in player_data.items:
                if item.get('cooldown',0) > 0: 
                    item['cooldown'] -= 1


    # player travel to a new tile (or teleported to a new tile)
    def game_move_new_tile( monster_or_event = True ):
        print_dbg()
        
        # print ascii? and story (random?) for scenery
        game_print_encounter()
        print()
        # all items in inventory are checked and their cooldown are decremented
        player_decrement_items_cooldown()
        # if monster_or_event roll for a monster or for event, 
        
        
        #game_encounter_event()
        #game_encounter_monster()
        #return 
        # will chance what will happen next
        chance_monster = chance_it(chance_encounter_monster)
        chance_event   = chance_it(chance_encounter_event)
        
        print(f'chnace for monster: {chance_monster}, chance for event: {chance_event}')

        if chance_monster:
             game_encounter_monster()
        elif chance_event:
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
        player_still_alive = player_data['hp'] > 0 or player_data['lives'] > 0
        player_killed_all = ( len(monsters) == len(player_data['killed_monsters']) )
        return player_still_alive or player_killed_all


    # starts the game, prints the story and get on with the next tile in a loop
    def game_start():
        print_dbg()

        # todo: get player name
        player_name = ''       # not necesarly

        # reste player data - the plaer record with items, stats and score
        game_player_reset( player_name )

        # print game start ascii and story
        game_print_start()
        
        # throw tiles at the player in a loop
        while player_can_do_new_tile():
            game_move_new_tile()
            # debug: kill player
            #player_data['hp'] = 0
        
        # print game over ascii and story
        game_print_end(  )

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
