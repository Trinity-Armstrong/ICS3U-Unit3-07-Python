#!/usr/bin/env python3

# created by: Trinity Armstrong
# created on: October 2019
# This program tells you if you have the grandmothers approval


def main():
    # This function tells you if you have the grandmothers approval

    # input
    print("Can I date your granddaughter?")
    print("")
    user_rich = input("Are you rich (answer yes or no): ")
    user_good_looking = input("Are you good looking (answer yes or no): ")

    # process & output
    if user_rich == "yes" or user_good_looking == "yes":
        print("")
        print("You can date my granddaughter!")
    elif user_rich == "no" and user_good_looking == "no":
        print("")
        print("You cannot date my granddaughter.")
    else:
        print("")
        print("Error!")


if __name__ == "__main__":
    main()
