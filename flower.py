class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price
    def info(self):
        print(f'Name: {self.name}\nPetals:{self.petals}\nPrice {self.price}')

    def change_flower_name(self, newname):
        self.name = newname
    def change_flower_petals(self, newpetals):
        self.petals = newpetals
    def change_flower_price(self, newprice):
        self.price = newprice

name = input('Enter flower name ')
petals = int(input('Enter flower petals ' ))
price = float(input('Enter flower pirce '))



flower1= Flower(name, petals, price )

while True:
    change = input('Do you want to change anything? ')
    if change == 'n':
        break
    elif change == 'y':
        category = input('Enter 1 for name\nEnter 2 for petals\nEnter 3 for price\nCategory: ')
        if category == '1':
            flowername = input('Enter new flower name: ')
            flower1.change_flower_name(flowername)
        elif category == '2':
            flowerpetals = int(input('Enter new flower petals: '))
            flower1.change_flower_petals(flowerpetals)
        elif category == '3':
            flowerprice = float(input('Enter new flower price: '))
            flower1.change_flower_price(flowerprice)

flower1.info()



