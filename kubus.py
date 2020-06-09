print ("kubus")
def volume(rusuk):
    print(rusuk*rusuk*rusuk)
def area(rusuk):
    print(6*rusuk*rusuk)

rusuk = int(input('masukan panjang rusuk: '))
print("ketik 1 untuk volume ")
print('ketik 2 untuk luas permukaan ')
pilihan = input('pilihan')
if pilihan == ('1'):
    volume(rusuk)
elif pilihan == ('2'):
    area(rusuk)

    