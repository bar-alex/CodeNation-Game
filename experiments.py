
print(f"\n# 1  {'='*50}\n")  
# -- tuples - they are imutable lists, more memory efficient as well

coral = ( 'blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral',)
print( coral )
print( coral[1] )
#coral[2] = "no coral"      # error
print( coral )



# ----------------------------------------------------------------------------------------
print(f"\n# 2  {'='*50}\n")  
# -- tuples in dicts

dict = {
    'blue coral': coral,
    'staghorn coral': 45,
    'pillar coral': "sraight up",
}

strenghts = {
    'weak': "blue coral",
    'medium': "pillar coral",
}

print( dict[ coral[1] ] )               # uses a tuple value to access a dicts value
print( dict[ strenghts['medium'] ] )    # uses a dicts value to access another dicts value



# ----------------------------------------------------------------------------------------
print(f"\n# 3  {'='*50}\n")  
# -- packing and unpacking tuples 

new_tuple = 4, 5, 'miui', True
print( new_tuple )

a, b, c, d = new_tuple
print(a,f'~{d}~',c,' - ',b)

print( type(new_tuple) )



# ----------------------------------------------------------------------------------------
print(f"\n# 4  {'='*50}\n")  
# -- blinking text and \r to overwrite text, also function to wait

def blink_once(multiplier=1,random_multiplier=False):
    from time import sleep
    from random import randint
    if random_multiplier: multiplier = randint(1,multiplier)
    #sys.stdout.write('\rTEXT')
    #print(f'\rTEXT{multiplier}', end='')
    print('\rTEXT', end='')
    sleep(0.3)
    #sys.stdout.write('\r     ')
    #print('\r'+' '*10, end='')
    print('\r'+' '*4, end='')
    sleep(0.2*multiplier)

def blink(number,progressive_wait=False,random=False):
     for x in range(0,number):
         if random: blink_once(number,True)
         elif progressive_wait: blink_once(x+1)
         else: blink_once()

print('\033[?25l', end="")  # try to hide blinking cursor // works
print('\nthree blinks:')
blink(3)
print('\ndegrading blink:')
blink(5,True)
print('\nrandom blink:')
blink(5,10,True)
print('\033[?25h', end="")  # curn cursor back on
print('\n')



# ----------------------------------------------------------------------------------------
print(f"\n# 5  {'='*50}\n")  
# -- colors and blink-ing using ansii escape sequences // blink-doesn't work in vscode

## octa:'\033[' hexa:'\x1b[' unicode:'\u001b['
## format '\033[<effect>;<color>;<background>m' // reset with '\033[0;0m'
## https://en.wikipedia.org/wiki/ANSI_escape_code
## https://stackabuse.com/how-to-print-colored-text-in-python/
## https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

effects = ('normal','bold','light','italic','underlined','blink')

print('Cheesy, red on yellow: \033[2;31;43m CHEESY \033[0;0m and that was cheesy' )
print('Same, using hexa: \x1b[2;31;43m CHEESY \033[0;0m and that was cheesy' )
print('Same, using unicode: \u001b[2;31;43m CHEESY \033[0;0m and that was cheesy' )

for i in range(0,6):
    print(f'Cheesy, red/yellow with effect {i}-{effects[i]}: \033[{i};31;43m CHEESY \033[0;0m and that was cheesy' )

print('\n')
# all colors

#import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        #sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(f"\033[38;5;{code}m"+code.ljust(4), end='')
    print("\033[0m")

print('\n')
# backgrounds

#import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        #sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print(f"\033[48;5;{code}m" + code.ljust(4), end='')
    print("\033[0m")

print('\n')



# ----------------------------------------------------------------------------------------
print(f"\n# 6  {'='*50}\n")  
# -- play with files

with open("fn.txt", "w+") as file:
    print('test line', file=file)
    print('newl line', file=file)
    file.write('|wrote with file.write')
    file.write('|\ranother one with file.write and \\r')
    file.write('|split text \nwith file.write')
    file.writelines(f'|written {1} with file.writelines'  )
    file.writelines('|split text \nwith file.writelines'  )
    file.write('\n')
    
    print( file.read() )
    # file.close()  # not needed ? 

print('# the file:')
with open("fn.txt", "r+") as file:
    print( file.read() )



# ----------------------------------------------------------------------------------------
print(f"\n# 7  {'='*50}\n")  
# -- typewritter effect
# alternative resreach -> threading.event.wait

# delay can be changed, can have 3 x delay on space, can have random (1 in 5) 3 x delay while writing the text
# unsing inkey, i could implement a printall with space/esc (after space clear buffer)
def typewriter( text, delay=0.01, newline=True, space_breaks=True, random_breaks=True, rush_on_enter_or_space=True ):
    def inkey():
        import msvcrt
        if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
        key = msvcrt.getch()
        if ord(key) == 0: key = msvcrt.getch()  # special chars
        if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
        return ord(key)
    
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


typewriter("This is my church. This is where I heal my hurts.")
typewriter(f"Lets bring some\033[2;31;43m color \033[0;0minto our lives ~~ 🌴🏄‍♀️🌴")     # 🍹🏖️
col_f = '\033[38;5;124m'
col_b = '\033[48;5;224m'
col_e = '\033[0;0m'
snip = 'try to'
typewriter(f"Lets {snip} bring {col_f}some more {col_b}color {col_e}into our lives🍻")



# ----------------------------------------------------------------------------------------
# print('\n# 8')
# # -- threading ? // works, but quirky, maybe
# from threading import Timer

# def hello():
#   print(" Hello darkness ", end='')

# print('threading?: ',end='')
# #t = Timer(0.05, "print('hello')" )     # doesn't work
# t = Timer(0.05, hello )     # don't use () here
# t.start()  # After 0.05 seconds, "Hello" will be printed
# print(' my old firend. ', end='')



# ----------------------------------------------------------------------------------------
print(f"\n# 9  {'='*50}\n")  
# -- loading progress with %

def loading(bar=False):
    from time import sleep
    print("Loading...")
    for i in range(0, 100):
        sleep(0.03)
        #sys.stdout.write(u"\033[1000D" + str(i + 1) + "%")
        #sys.stdout.flush()
        if not bar:
            print(f'\r{i+1}%', end='', flush=True)
        else:
            x = int((i+1)/5)
            print(f"\r[{ '🌸'*(x) }{ '🍀'*(20-x) } {i+1}%]", end='', flush=True)
    print()
    
loading()
loading(True)



# ----------------------------------------------------------------------------------------
print(f"\n# 10  {'='*50}\n")  
# -- read keypress -- ESC to escape a loop for example


# Ctrl+C, Ctrl+X, Ctrl+Z, Ctrl+Y = 3, 24, 26, 25
# Esc, Enter, Tab, Sapce, Bksp, Del, Ins = 27, 13, 9, 32, 8, 83, 82
# Home, End, PgUp, PgDown = 71, 79, 73, 81
# Left, Right, Up, Down = 75, 77, 72, 80
def inkey():
    import msvcrt
    if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
    key = msvcrt.getch()
    if ord(key) == 0: key = msvcrt.getch()  # special chars
    if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
    return ord(key)


print('start loop - press key (ESC to break):')
from time import sleep
while True:
    sleep(0.1)
    xx = inkey()
    if xx: print(f'\nAscii: {xx} Char:"{chr(xx)}"', flush=True)
    if xx == 27: break
    print('💖', end='', flush=True)



# ----------------------------------------------------------------------------------------
print(f"\n# 11  {'='*50}\n")  
# -- ticks - game loop?, uses inkey to detect keypress

def inkey():
    import msvcrt
    if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
    key = msvcrt.getch()
    if ord(key) == 0: key = msvcrt.getch()  # special chars
    if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
    return ord(key)

#print('You get into a clearing and discover a huge bear. \nYou should probably do something soon, before he sees you.\nChoose 1, 2, 3, 4:')
typewriter('You get into a clearing and discover a huge bear. \nYou should probably do something soon, before he sees you.\nChoose 1, 2, 3, 4:')
tick = 0.1
seconds = 10
warn_after = 5

tick_total = seconds/tick
tick_warn = warn_after/tick
tick_count = 0

from time import sleep 
while tick_count < tick_total:
    sleep(0.1)
    tick_count += 1
    answer = inkey()
    if chr(answer) in '1234':
        #print(f'\nYou have chosen wisely. Using magic spell no. {chr(answer)} you turn the bear into a history lesson.', flush=True)
        typewriter(f"\nYou have chosen wisely. Using magic spell no. {chr(answer)} you turn the bear into a history lesson.")
        break
    if tick_count == tick_warn:
        #print("\nThe bear turns around and notices you. \nAfter a moment's hesitation it rushes twards you bearing his fangs\nHe's going to eat well tonight and you're invited to dinner!")
        typewriter("\nThe bear turns around and notices you. \nAfter a moment's hesitation it rushes twards you bearing his fangs\nHe's going to eat well tonight and you're invited to dinner!")
    if tick_count == tick_total:
        #print("\nThe last thing you remeber is the bear's sounds of delight as he munches on your insides.\nAh, this should have gone differently, you think to yourself, if only you could remember the incantations.\nYou fade into oblivion ..")
        typewriter("\nThe last thing you remeber is the bear's sounds of delight as he munches on your insides.\nAh, this should have gone differently, you think to yourself, if only you could remember the incantations.\nYou fade into oblivion ..")

if tick_count < tick_total:
    #print('\nWell done. You won!')
    typewriter('\nWell done. You won!')
else:
    #print('\nHow could you fail? You only had to press some numbers..')
    typewriter('\nHow could you fail? '\
        'You only had to press some numbers..')



# ----------------------------------------------------------------------------------------
print(f"\n# 12  {'='*50}\n")  
# -- print an ascii from file
## http://www.glassgiant.com/ascii/

print('\n')

with open('ascii_wolf.txt','r') as file:
    for line in file.readlines():
        print(line, end='')

print('\n')
