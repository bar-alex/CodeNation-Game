

def inkey():
    import msvcrt
    if not msvcrt.kbhit(): return 0         # nothing in beyboard buffer to be read
    key = msvcrt.getch()
    if ord(key) == 0: key = msvcrt.getch()  # special chars
    if ord(key) == 3: exit()                # because getch prevents normal ctrl+c
    return ord(key)

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


def get_player_answer(answer_list, answer_time=0, warn_time=0, warn_text=''):
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



print('\n')

with open('ascii_batman.txt','r') as file:
    m_face = ''     # the ascii art
    story = ''      # the story/description
    warn = ''       # warinig text when he doesn't hurry to fight it
    m_atk = 0       # monster's attack
    m_def = 0       # monster's defence
    m_drops = []    # list of potential drops along with the chance of rolling (out of 10) - it's a list of lists
    for line in file.readlines():
        line = line.strip()
        if line[:2] == '##':
            #print(line, end='')
            m_face += line + '\n'
            #print(line)

        elif line[:5].lower()=='story': 
            story = line[line.find('=')+1:].strip()
            #print(story)

        elif line[:4].lower()=='warn': 
            warn = line[line.find('=')+1:].strip()

        elif line[:3].lower()=='atk': 
            #print( line[line.find('=')+1].strip() )
            m_atk = int( line[line.find('=')+1:].strip() )

        elif line[:3].lower()=='def': 
            m_def = int( line[line.find('=')+1:].strip() )

        elif line[:5].lower()=='drops': 
            s = line[line.find('=')+1:].strip()
            #print(s)
            m_drops = [ l.split(':') for l in s.split(',') if l ]
            #print(m_drops)


print(m_face)

typewriter(story.replace('\\n','\n'), newline=False)
typewriter(" (a)ttack / (f)lee:\n")

answer = get_player_answer('af',10,5,warn+'\n')

if answer == 'failed':
   # print("You failed to attack in time, so the monster did quick work of you. You're dead.")
   text = "You failed to attack in time, so the monster did quick work of you. You're dead."
   typewriter(text)

elif answer=='f':
    #print("You decided to save your hide, so you turned tail and run.")
    text = "You decided to save your hide, so you turned tail and run."
    typewriter(text)

elif answer=='a':
    text = f'Monster Attack: {m_atk} \nMonster Defence: {m_def}'
    typewriter(text)

    #print("With a quick woosh, then and bam, you did flop and then a zap. The creature lies motionless at you feet. Congrats!")
    text = "With a quick woosh, then and bam, you did flop and then a zap. The creature lies motionless at you feet. \nCongrats!"
    typewriter(text)

    # get random loot based on chances shuriken:8 -> 8 out of 10 to drop shuriken
    from random import choice, randint
    item_gained = ''
    for item in m_drops:
        if randint(1,11) <= int(item[1]): item_gained = item[0]
    if item_gained: print(f'\nThe creature dropped a {item_gained}')
    else: print("\nThe creature didn't carry anythig unfortunately.")

else: 
    print(f"\nerr: shouldn't run. answer == {answer}")

print()
