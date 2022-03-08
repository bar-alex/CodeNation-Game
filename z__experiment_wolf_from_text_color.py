
## octa:'\033[' hexa:'\x1b[' unicode:'\u001b['
## format '\033[<effect>;<color>;<background>m' // reset with '\033[0;0m'

#\033[2;9m
#\033[0;0m

#with open('ascii_wolf.txt','r', encoding="latin-1") as file:       "unicode_escape"
from distutils import text_file


with open('ascii_monster_wolf.txt','r') as file:        # , encoding="unicode_escape"
#with open('ascii_wolf.txt','r') as file:
    import  codecs
    for line in file.readlines() :
        #text_line = '\033[1;9;0m' + line + '\033[0;0m'
        #text_line = line.replace( '\\u001b[', '\u001b[' )
        #print( text_line , end='')
        #text_line = line.decode("unicode_escape")
        #print( fr'{line}' , end='' )
        #text_line = line.replace( '\\u001b[', '\u001b[' )
        #print('%s' %line..decode('unicode_escape'), end='')
        text_line = line
        #text_line = list( line )
        #text_line = codecs.decode( line, "utf-8" )
        print( text_line , end='' )

print('\n')