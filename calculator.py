print ('calculator')
try:
    a = int(input('enter number '))
except vallueerror:
    print(error)
b = int(input('enter another number '))
c = a + b
d = a - b
e = a * b
f = a / b
print("enter 1 to add ")
print('enter 2 to subtract ')
print("enter 3 to multiply ")
print('enter 4 to divide')
answer = input('answer')

if answer  == ("1"): 
    print(f' {c}')

if answer == ('2'):
    print(f'{d}')

if answer ==('3'):
    print(f'{e}')

if answer ==('4'):
    print(f'{f}')
