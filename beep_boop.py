"""This program uses a for loop to iterate over the range of numbers 0 to 1000. It then checks the current loop
number using the modulo operator % to see if it's a multiple of 5, 20, or 100, and prints the appropriate message for
each case.

If the loop number is a multiple of 100, it prints "beep boop". If it's a multiple of 20, it prints "boop". If it's a
multiple of 5 but not 20 or 100, it prints "beep". Otherwise, it continues to the next iteration of the loop without
printing anything.

The program should print out a sequence of "beep", "boop", and "beep boop" messages as it loops through the numbers
from 0 to 1000.

The time complexity of this program is O(n), where n is the number of iterations in the for loop. The space
complexity of this program is O(1), as it only uses a constant amount of memory to store a few variables.

"""


def main():
    for i in range(1001):
        # to start counting at 1 instead of zero
        loop_num = i + 1
        # If loop_num is a multiple of 100, print "beep boop"
        if loop_num % 100 == 0:
            print("beep boop")
        # If loop_num is a multiple of 20, print "boop"
        elif loop_num % 20 == 0:
            print("boop")
        # If loop_num is a multiple of 5, print "beep"
        elif loop_num % 5 == 0:
            print("beep")


if __name__ == '__main__':
    main()
