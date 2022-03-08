

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





def warrior_king_of_tristram():

    # some config data
    monster_file_stem  = 'ascii_monster_'        # how all the moster files start
    event_file_stem    = 'ascii_event_'          # how all the events files start
    items_ascii_file   = 'ascii_loot_items.txt'  # holds all the items
    strings_ascii_file = 'ascii_strings.txt'     # holds the strings for encounters

    chance_encounter_monster = 7        # 7 out of 10 to fight a monster
    chance_encounter_event   = 5        # 5 out of 10 to have an event
    chance_encounter_monster = 2        # 2 out of 2 to have nothing special in the encounter

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


    # reads a keypress from the buffer if theres one there, otherwise returns 0
    def inkey():
        import msvcrt
        if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
        key = msvcrt.getch()
        if ord(key) == 0: key = msvcrt.getch()  # special chars
        if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
        return ord(key)


    # delay can be changed, can have 3 x delay on space, can have random (1 in 5) 3 x delay while writing the text
    # unsing inkey, i could implement a printall with space/esc (after space clear buffer)
    def typewriter( text, delay=0.01, newline=True, space_breaks=True, random_breaks=True, rush_on_enter_or_space=True ):
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
                    should_break = randint(1,5)==3
                if (char==' ' and space_breaks) or should_break: 
                    for _ in range(4): sleep(delay)
        if newline: print(flush=True)

    
    # rolls a dice and returns a value between 1 and faces (defaults to 6)
    def dice_roll(faces = 6):
        from random import randint
        return randint(1,faces)


    # answer must be from answer_list, will return 'failed' if no answer was given
    def get_answer(answer_list, answer_time=0, warn_time=0, warn_text=''):
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
                return chr(answer)
            elif warn_time and warn_text and tick_count == tick_warn:
                typewriter(warn_text,delay=0.01)
            elif answer_time and tick_count == tick_answer:
                return 'failed'


    # will load the monstrs from the text files into the monsters[] list
    def load_files(file_stem,calable_func,dest_list):
        from os import listdir, getcwd
        from os.path import isfile, join

        #file_stem = monster_file_stem
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
        print(f"dbg:process_ascii ~ file_name = '{file_name}'")
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
                    if line: print(f'err in process_ascii: shouldnt run, line is "{line}" ')
                
            # todo: remove this when everything works fine
            # for debug purposes
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
        print("dbg: process_Ascii_loot")
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
        typewriter( text, )

    
    # it will scan a file for an ascii afrt and a "story = value" 
    # and then it will print the ascii art and the story
    def print_ascii_and_story_from_file( file_name ):
        #file_name = 'ascii_game_start.txt'
        # todo: test file exists
        ascii_text = ''
        story = ''
        with open(file_name,'r') as file:
            for line in file.readlines():
                line.strip()
                if line[:2] == '##':        # collects the lines for the ascii image
                    ascii_text += line 
                elif line[:1] == '#':       # the line is a comment, ignore it
                    continue
                elif line.find('=') > 0:
                    story = line[ line.find('=')+1:]        # everything after the '='
                    story = story.strip()                   # strip leading and trailing spaces and new lines
                    story = story.replace("\\n",'\n')       # unescapes new lines in the story string
                else:
                    if line: print(f'err in process_ascii: shouldnt run, line is "{line}"')

        # print the ascii image
        print_ascii( ascii_text )
        
        # print the story - typewritter
        print_story( story )



    # will print the game start ascii and the story
    def print_game_start():
        print("dbg: print_game_start()")
        # read from text file
        # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of  notmal print
        print_ascii_and_story_from_file( 'ascii_game_start.txt' ) 


    # will print the game end ascii and the story // difere
    def print_game_end( player_won = False ):
        print("dbg: print_game_end()")
        # read from text file -- depending on player_won variable you check read differemt files
        # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of notmal print
        if player_won: print_ascii_and_story_from_file( 'ascii_game_win.txt' ) 
        else: print_ascii_and_story_from_file( 'ascii_game_loose.txt' ) 


    def print_game_encounter():
        print("dbg: print_game_enocunter()")
        # todo: print the game encounter stroy (and ascii? maybe not)
        # draw a chance string from encounters and print it using 'print_story()' instead of print()



    ## loads everything from files
    def game_setup():

        # load items in list -- validate_monster will check the items are in the list
        process_ascii_loot(items_ascii_file, loot_items)

        # load monsters from files
        load_files(monster_file_stem, process_ascii, monsters)

        # load events from files
        load_files(event_file_stem, process_ascii, events)

        # load flavor strings (foud youself into a clearing, departing the lcerang, etc)
        process_ascii_strings( strings_ascii_file )
        
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
    def game_reset_player( player_name = 'Player' ):
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


    # the player encounters a monster
    def game_encounter_monster( monster_attack_first = False ):
        print("dbg: game_encounter_monster()")
        # todo: build the function


    # player encounters encounters a new event
    def game_encouonter_event():
        print("dbg: game_encouonter_event()")
        # todo: build the function


    # if theres no event or monster to encounter on this tile
    def game_encounter_none():
        print("dbg: game_encounter_none")
        # todo: build the function


    # player travel to a new tile (or teleported to a new tile)
    def game_new_tile( monster_or_event = True ):
        print("debug: game_start_tile()")
        # todo: everythign happens here
        # print ascii? and story (random?) for scenery
        print_game_encounter()
        # if monster_or_event roll for a monster or for event, 
        if chance_encounter_monster >= dice_roll(10):
            game_encounter_monster()
        elif chance_encounter_event >= dice_roll(10): 
            game_encouonter_event()
        else: 
            game_encounter_none()
        # then roll for which monster or which event to use
        # action teh event or the monster
        # afer that, if player HP > 0 then check options after the fight
        # action option after the fight if any 
        # exit function after the player cjose which way to go 
        # (it goes back to the loop where it will run another game_start_tile)



    # starts the game, prints the story and get on with the next tile in a loop
    def game_start():
        print('dbg: game_start()')

        # todo: get player name
        player_name = ''

        # reste player data - the plaer record with items, stats and score
        game_reset_player( player_name )

        # print game start ascii and story
        print_game_start()
        return 
        # throw tiles at the player in a loop
        while player_data['hp'] > 0 and player_data['lives'] > 0:
            game_new_tile()
        
        # print game over ascii and story
        print_game_end()

        # todo asks the user if he'd like to start again ?
        # it should be in a loop only for this purpose


    ######################################################################
    ##  here, the application starts
    ######################################################################

    # loads all the data from the ascii files
    game_setup()

    # starts the game
    game_start()

    #my_list = []
    #process_ascii('ascii_monster_wolf.txt',my_list)
    #print( my_list )
    #print( my_list[0].get('name',None) )





warrior_king_of_tristram()
