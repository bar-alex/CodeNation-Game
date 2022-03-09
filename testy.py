
# useful in debug, tells the name of the calling function
def whoami( lvl=0 ):
    import sys
    return sys._getframe(1+lvl).f_code.co_name


# prints an problem  message in red and includes the function where the error hapened
def print_err( message ):
    text_to_print = f"\033[1;31merr=>{whoami(1)}: "+message+"\033[0m"
    from pprint import pprint
    #pprint( text_to_print )
    print( text_to_print ) 




# def whoami( lvl=0 ):
#     import sys
#     return sys._getframe(1+lvl).f_code.co_name

def func_two():
    return whoami(1)

def one_func():
    x = 5
    print_err( f"x = {5} {['mama',4,'tata','geta',4,['mama','mari',5,{'tica':3,'popa':4,'gica':'tatooine'}]]}" )
    #print_err( f"x = {5}" )
    return func_two()

print( one_func() )


# import os
# clear = lambda: os.system('cls')
# clear()

# eval( 'print("something fshy")' )

# from inspect import getmembers, isfunction

# from the_game import warrior_king_of_tristram
# print(getmembers(warrior_king_of_tristram, isfunction))


# linez = ''
# print( linez.find('=') )

# if linez.find('='): print('i have =')
# else: print('i dont have = ')

# xx = 'ascii_monster_'

# from os.path import exists as file_exists
# print( file_exists(xx+'*.txt') )


# from os import listdir, getcwd
# from os.path import isfile, join
# ascii_file_stem_monster = 'ascii_monster_'  
# curent_dir = getcwd()
# files_in_dir = listdir(curent_dir)
# #print(files_in_dir)
# #xx = [f for f in listdir(curent_dir) if isfile(join(curent_dir, f)) and f[:len(ascii_file_stem_monster)].lower()==ascii_file_stem_monster]
# xx = [f for f in files_in_dir if f[:len(ascii_file_stem_monster)].lower()==ascii_file_stem_monster]
# #if xx: print(True)  
# print(xx)

# print( 3 % 6 )

# print( '\n'.isspace() )

# print( (0.1-0.02) )
# print( (0.1-0.02)/0.01 )

# x = 10 / (1)
# print( x )

# print( "miaw  miuz \npop".split() )

# print( 5 / 9)

# print('\a')
# print(chr(7))

# if []: print('list is there')
# else: print('list is not there')

# import winsound
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 100  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)

# import winsound
# winsound.Beep(1320, 50)
# winsound.PlaySound('SystemHand',winsound.SND_ALIAS)
# winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

