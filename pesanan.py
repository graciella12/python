orders = ['es teh manis', 'nasi pecel', 'sambal bawang']
quantity = [4,2,3]
total = 0
print('pesan apa aja kak?  \nkakak sudah pesan: ')
for order in range (len(orders)):
        print ( orders[order],"nya ",quantity[order])

def tamba():
    tambahf = input('tambah apa kak? ')
    return tambahf
def tambaq():
    tambahf = int (input('tambah berapa kak?'))
    return tambahf
while True :
    pesen = input('ada tambahan kak? y/n ')
    if pesen == ("y"):
        tambahan= tamba()
        orders.append(tambahan)
        tambahan= tambaq()
        quantity.append(tambahan)
        

    elif pesen == ('n'):
        print('saya ulang pesanannya ya kak')
        for order in range (len(orders)):
             orders[order] = orders[order]+"nya"
        dicti = dict(zip(orders, quantity))
        
        for key, value in dicti.items():
            print(key, value)
            total = total+value
               
        print("terima kasih ditunggu",total," menit ya pesanannya")
        break

        
    

