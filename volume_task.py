def cube_volume(length):
    volume = length * length * length
    return volume

def cuboid_volume(length, width, height):
    volume = length * width * height
    return volume

def cylinder_volume(height, radius):
    pi = 3.142
    volume = pi * radius * radius * height
    return volume

def pyramid_volume(base, height):
    volume = base * base * height * (1/3)
    return volume

def sphere_volume(radius):
    pi = 3.142
    volume = radius * radius * radius * pi * (4/3)
    return volume

shape = input("""Which shape volume?
cube => 1
cuboid => 2
cylinder => 3
square_pyramid => 4
sphere => 5
(type the number)
""")

#cube
if shape == ("1"):
    length1 = int(input("Whats the length of one side? "))
    cube_volume(length1)
    answer1 = cube_volume(length1)
    print ("the volume is ", answer1, "cm^3")

#cuboid
elif shape == ("2"):
    length2 = int(input("Whats the length? "))
    width2 = int(input("Whats the width? "))
    height2 = int(input("Whats the height? "))
    answer2 = cuboid_volume(length2, width2, height2)
    print("the volume is ", answer2, "cm^3")

#cylinder
elif shape == ("3"):
    height3 = int(input("Whats the height? "))
    radius3 = int(input("Whats the radius? "))
    answer3 = cylinder_volume(height3, radius3)
    print("the volume is ", answer3, "cm^3")

#square_pyramid
elif shape == ("4"):
    base4 = int(input("Whats the base? "))
    height4 = int(input("Whats the height? "))
    answer4 = pyramid_volume(base4, height4)
    print("the volume is ", answer4, "cm^3")

#sphere
elif shape == ("5"):
    radius5 = int(input("Whats the radius? "))
    answer5 = sphere_volume(radius5)
    print("the volume is ", answer5, "cm^3")

else:
    print("Invalid shape try again ):")
