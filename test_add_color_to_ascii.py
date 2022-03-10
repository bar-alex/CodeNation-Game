#\033[31m
#\033[0m

file_name = 'ascii_monster_wolf.txt'
file_dest = 'ascii_monster_wolf_dest.txt'

# 30-black, 31-red, 32-green, 33-yellow, 34-blue, 35-purple, 36-cyan, 37-white
color     =  31 

with open(file_name,'r') as file, open(file_dest,'w+') as file_dest:
    for line in file.readlines():
        line = line.replace('{@}',f'\033[{31}m')
        line = line.replace('{*}','\033[0m')
        file_dest.writelines(line)

