print('login')

for tries in range (3,0,-1):
    print (f'you have {tries} tries')

    username = input('enter username ')
    password = input('enter password ')
    if username == ('gras') and password == ('123'):
        print ('login sucess')
        break
    else:
        print ('login invalid')

