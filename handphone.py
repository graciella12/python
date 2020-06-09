phones=[]
class Handphone:
    def __init__(self, version, brand, color):
        self.version = version
        self.brand = brand
        self.color = color
    def info(self):
        print(f"Version: {self.version}\nBrand: {self.brand}\ncolor: {self.color}")
    def register(self):
        phones.append(self)
while True:
    forward = input("Enter a phone? (y/n) ")
    if forward == 'n':
        break
    elif forward =='y':
        phoneversion = input('Enter phone version: ')
        phonebrand = input('Enter phone brand: ')
        phonecolor = input('Enter phone color: ')

        handphone1 = Handphone(phoneversion, phonebrand, phonecolor)
        handphone1.register()

for phone in phones:
    phone.info()