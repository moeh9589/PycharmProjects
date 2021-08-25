import math

def square_area(base):
    sqarea= base**2
    return sqarea
def tri_area(tribase,height):
    triarea= tribase*height/2
    return triarea
def rectangle_area(rectbase,rectheight):
    rectarea=rectbase*rectheight
    return rectarea
def circle_area(radius):
    circarea= math.pi * radius
    return circarea

def shape(usercalc):
    
    if usercalc=='Square':
        base=float(input("Please enter a length for the base"))
        print (square_area(base))

    elif usercalc=='Triangle':
        tribase=float(input("Please enter a length for the base"))
        height=float(input('Please enter a length for the height'))
        print (tri_area(tribase,height))
    elif usercalc=='Rectangle':
        rectbase=float(input("Please enter a length for the base"))
        rectheight = float(input('Please enter a length for the height'))
        print (rectangle_area(rectbase,rectheight))
    elif usercalc=='Circle':
        radius=float(input('Please enter a length for the radius'))
        print (circle_area(radius))

print("This is a program to calcluate the area of a shape")
print()
shape(input('Please enter a shape: Square, Rectangle, Circle, or Triangle==> '))

