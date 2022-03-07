
def typewriter( text, delay=0.03, newline=True, space_breaks=True, random_breaks=True ):
    from time import sleep
    from random import randint
    should_break = False
    for char in text:
        if random_breaks: 
            should_break = randint(1,5)==3
        print(char, end='', flush=True)
        sleep(delay)
        if (char==' ' and space_breaks) or should_break: 
            for _ in range(4): sleep(delay)
    if newline: print(flush=True)

