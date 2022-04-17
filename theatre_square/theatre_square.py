from math import ceil


def theatre_square(value):
    values =value.split()
    width = (int)(values[0])
    height =(int)(values[1])
    square =(int)(values[2])
    possible_on_width = ceil(width/square)
    possible_on_height = ceil(height/square)
    return possible_on_height * possible_on_width

value =input()
print(theatre_square(value))

