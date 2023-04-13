import math

def square_footage(length: int, width:int):
    return length * width

def circumference(radius: int):
    result = math.pi*2*radius
    return (f"{result:.2f}")
