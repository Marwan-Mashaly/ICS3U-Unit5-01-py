#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program will convert temprature from Celsius to Fahrenheit


def temperature():
    # This function will convert temprature from Celsius to Fahrenheit
    # input
    tempc = input("Temperature in Celsius : ")
    print("")
    # process & output
    try:
        num_check = int(tempc)
        tempf = (num_check * 9/5) + 32
        print("{} * 9/5 + 32 = {}".format(num_check, tempf))
        print("")
        print("Temperature in Fahrenheit is :", tempf)

    except(ValueError):
        print("invalid number")


if __name__ == "__main__":
    temperature()
