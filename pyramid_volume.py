#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created June 2022
# This program calculates the volume of a square based pyramid

import math


def pyramid_volume(base_edge, height):
    # this function calculates volume of a square based pyramid

    # process
    volume = (base_edge**2) * (height / 3)

    return volume


def main():
    # this function gets input, calls a function, gives output
    print("This program calculates the volume of a square based pyramid.")
    print("")

    # input
    base_edge_string = input("Enter the length of the base edge (cm): ")
    height_string = input("Enter the height (cm): ")

    try:
        base_edge = float(base_edge_string)
        height = float(height_string)
        if base_edge >= 0 and height >= 0:
            # call function
            volume = round(pyramid_volume(base_edge, height), 2)
            # output
            print("\nThe volume is {} cm³.".format(volume))
        else:
            print("\nYour numbers cannot be negative. Please try again.")

    except Exception:
        print("\nYour numbers are invalid. Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
