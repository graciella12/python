import random
import time
ind = random.randint(1,9)

while True:
    if 1<=ind<=3:
        gbk = 'gunting'
    elif 4<=ind<=6:
        gbk = 'batu'
    elif 7<=ind<=9:
        gbk = 'kertas'
   
    main = input('mau main gunting kertas batu? y/n ')
    if main == ("n"):
        print('ok byee')
        break
        
    elif main == ("y"):
        ind = random.randint(1,9)
        answer = input('mau pakai gunting kertas atau batu? ')
        if answer == 'gunting':
            if gbk =='gunting':
                print('seri -_-')
            elif gbk == 'kertas':
                print('menang :)')
            elif gbk == 'batu':
                print('kalah :(')
        elif answer == 'batu':
            if gbk =='gunting':
                print( 'menang :)')
            elif gbk == 'batu':
                print('seri-_-')
            elif gbk == 'kertas':
                print('kalah :(')
                
        elif answer == 'kertas':
            if gbk == 'gunting':
                print('kalah:(')
            elif gbk == 'kertas':
                print('seri -_-')
            elif gbk == 'batu':
                print('menang:)')
        print('computer pakai',gbk)


