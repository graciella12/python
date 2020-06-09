doctors = []

def sebut():
    for orang in doctors:
        for key,val in orang.items():
            print(f'{key}: {val}')
    print("")

def make(nama, umur, spesialitas, namadoctor):
    nama = {}
    nama['nama'] =  namadoctor
    nama['umur'] =  umur
    nama['spesialitas'] =  spesialitas
while True:
    add = input('add doctor(y/n): ')
    if add == 'n':
        break
    elif add == "y":
        name = input('isi nama dokter: ')
        age = input('isi umur dokter: ')
        speciality = input('isi spesialitas dokter: ')
        doctors = make(name, age, speciality, name)
        

    else:
        print("input invalid")
    

sebut()