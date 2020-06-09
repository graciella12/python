class Cone:
    def __init__(self, radius, height, slant):
        self.radius = radius
        self.height = height
        self.slant = slant

    def cone_volume(self):
        return self.height*3.14*self.radius**2/3
    def cone_area(self):
        return self.radius*3.14*(self.radius+self.slant)
radius = int(input('Enter cone radius: '))
height = int(input('Enter cone height: '))
slant = int(input('Enter cone slant height: '))
new_cone = Cone(radius, height, slant)

choice = input('enter 1 for volume \nenter 2 for area\n')
if choice == '1':
    print(f'the cone volume is {new_cone.cone_volume()} ')
elif choice == '2':
    print(f'the cone area is {new_cone.cone_area()} ')

