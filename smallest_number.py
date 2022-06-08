#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds the smallest number out of random numbers

import random


def smallest_number(random_numbers):
    # this function finds the smallest number
    val1 = random_numbers[0]

    for a_single_number in random_numbers:
        if val1 > a_single_number:
            val1 = a_single_number

    return val1


def main():
    # this function creates the array

    random_numbers = []

    # process
    for loop_counter in range(10):
        number = random.randint(0, 100)
        random_numbers.append(number)
        print("Random number {0} is: {1}".format(loop_counter + 1, number))
    print("")

    smallest = smallest_number(random_numbers)

    print("The smallest number is {}".format(smallest))


if __name__ == "__main__":
    main()
