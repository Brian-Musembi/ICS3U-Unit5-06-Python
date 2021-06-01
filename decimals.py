#!/usr/bin/env python3

# Created by Brian Musembi
# Created on June 2021
# This program rounds a number to a user-specific decimal place


def decimalRound(user_num, dec_place):
    # This function rounds a number to a user-specific decimal place

    # process
    user_num[0] = user_num[0] * (10 ** dec_place[0]) + 0.5
    user_num[0] = int(user_num[0])
    user_num[0] = user_num[0] / (10 ** dec_place[0])


def main():
    # this function receives input
    print("This program rounds a number to a specific decimal place.")
    print("")

    # list
    user_num = []
    dec_place = []

    # input
    while True:
        try:
            user_input = input("Please enter a number you want to round: ")
            user_float = float(user_input)

            dec_input = input("Enter how many decimal places you want"
                              " to round your number to: ")
            dec_int = int(dec_input)
            print("")

            # adding to list
            user_num.append(user_float)
            dec_place.append(dec_int)

            # call function
            decimalRound(user_num, dec_place)

            break

        except Exception:
            # output
            print("Please enter a number for both values, try again.")

    # output
    print("{0} rounded to {1} decimal places is {2}".format(user_input,
                                                            dec_place[0],
                                                            user_num[0]))


if __name__ == "__main__":
    main()
