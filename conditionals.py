"""
file: conditionals.py
language: python3
author: bre5933@rit.edu Brian R Eckam
description: Create two separate functions: divisible() and triangle() with tests for each.
The divisible() function will test if two integers are evenly divisible.
The triangle() function will test to see if three parameters, sides of a triangle, can create a triangle.
The test functions are kept in the program to show the output of multiple inputs.
"""


def divisible(int1, int2):
    """
    divisible() will check to see:
    1) If the two arguments are evenly divisible
    2) 0 is one of the arguments
    3) Either of the arguments are negative
    4) The arguments are equal

    """
    greater = max(int1, int2)
    lesser = min(int1, int2)
    if int1 <= 0 or int2 <= 0:
        print("Inputs must be positive Integers!")

    elif int1 == int2:
        print("Those integers are equal:", int1)

    elif greater % lesser == 0:
        print(greater, "is divisible by", lesser)
    else:
        print(greater, "is not divisible by", lesser)


def test_divisible():
    """
    test_divisible() tests all the properties of the function divisible to make sure it works as intended
    """
    divisible(0, 1)
    divisible(2, -2)
    divisible(48, 24)
    divisible(3, 90)
    divisible(-1, 455565)
    divisible(1111223, 0)
    divisible(314159, 314159)
    divisible(45, 21)
    divisible(12, 3001)
    divisible(345, 5)


def triangle(side1, side2, side3):
    """
    triangle() will test to see if the three arguments given will create a triangle.
    Assume the arguments are side lengths
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Triangles require sides of positive length!")
    elif side1 > 0 and side2 > 0 and side3 > 0:
        if (side1 + side2 >= side3) and (side2 + side3 >= side1) and (side3 + side1 >= side2):
            print("Side lengths", side1, ",", side2, "and", side3, "can form a triangle.")
        else:
            print("Side lengths", side1, ",", side2, "and", side3, "can not form a triangle.")


def test_triangle():
    """
    test_triangle() will test the triangle function
    """
    triangle(-1, 2, 3)
    triangle(1, 1, 1)
    triangle(5, 12, 13)
    triangle(1, 3, 5)
    triangle(300, 400, 500)
    triangle(1, 2, 30)
    triangle(1, -2, 3)
    triangle(1, 2, -3)
    triangle(1, 2, 3)


def main():
    """
    this is the main function which will be run
    """
    test_divisible()  # call test_divisible
    test_triangle()  # call test_triangle


main()  # runs the main function
