
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
        #if validate_monster_event_item(item_read):
        #    dest_list.append(item_read)


encounters  = []     # list of encounters strings 

# will lload all the strings from ascii_strings.txt into encounters
def process_ascii_strings():
    #print("dbg: process_Ascii_loot")
    # todo: load all the strings from ascii_strings into the encounters[] list
    file_name = 'ascii_strings.txt'
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

process_ascii_strings()

#print( encounters )

from pprint import pprint
pprint( encounters )

