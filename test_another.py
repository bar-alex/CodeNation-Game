
# linez = ''
# print( linez.find('=') )

# def print_game_start():
#     file_name = 'ascii_game_start.txt'
#     ascii_text = ''
#     story = ''
#     with open(file_name,'r') as file:
#         for line in file.readlines():
#             line.strip()
#             # we don't need to strip things.
#             if line[:2] == '##':        # collects the lines for the ascii image
#                 ascii_text += line 
#             elif line[:1] == '#':       # the line is a comment, ignore it
#                 continue
#             elif line.find('='):
#                 story = line[ line.find('=')+1:]        # everything after the '='
#                 story = story.strip()                   # strip leading and trailing spaces and new lines
#                 story = story.replace("\\n",'\n')
#             else:
#                 if line: print('err in process_ascii: shouldnt run, line is "{line}"')
#     print(ascii_text + '\n')
#     print(story)

# # name = 'tim is a great story teller'
# # slice = name[9 : ]

# # name[stat:]
# # name[:end]

# print_game_start()

# # # goes through the lines of an ascii file (ascii_monster_<>.txt or ascii_event_<>.txt) and
# #     # creates a dictionary with everything inside (ascii, list of drops, key/value pairs)
# #     # and that dictionary is validated and added tot the list passed as parameter (monsters or events)
# # def process_ascii(file_name, dest_list):
# #         print(f"dbg:process_ascii ~ file_name = '{file_name}'")
# #         with open(file_name,'r') as file:
# #             item_read = {}     # =dict()
# #             ascii_img = ""
# #             for line in file.readlines():
# #                 line = line.rstrip()        # removes \n

# #                 if line[:2] == '##':        # collects the lines for the ascii image
# #                     ascii_img += line + '\n'

# #                 elif line[:1] == '#':       # the line is a comment, ignore it
# #                     continue
# #                 else:
# #                     dict_value = 0

# #                     #print(f'dict key : value = {dict_key} : {dict_value}')   # debug
# #                     item_read[dict_key] = dict_value                        # adds the new key/value to dictionary

# #                 else:
# #                     if line: print('err in process_ascii: shouldnt run, line is "{line}"')
                
# #             # for debug purposes
# #             item_read['dbg_filename'] = file_name

# #             # validate the required fields are in there
# #             if validate_monster_item(item_read):
# #                 dest_list.append(item_read)

# #     # will print the game start ascii and the story
# #     def print_game_start():
# #         process_ascii(ascii_game_start.txt)
# #         print("dbg: print_game_start()")
# #         # todo: print game start story
# #         # read from text file
# #         # print ascii using "print_ascii(text)" and print the story using "print_story(text)" instead of  notmal print



















# # # items=[]

# # # def my_func(x, my_items ):
# # #     my_items.append(x)
# # #     print('inside: ',my_items)


# # # items.append(4)

# # # print('before: ',items)

# # # my_func(5,items)

# # # print('outside: ',items)

# # # items.append(6)

# # # print('at teh end: ',items)

# # print(  int('-2') )


