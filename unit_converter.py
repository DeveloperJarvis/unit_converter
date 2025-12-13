# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the unit_converter Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# unit_converter - Convert distance, volume, temprature, speed, etc
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# unit_converter MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------

distance_units = {
    "km": {
        "miles": 0.621371,
        "metres": 1000,
        "yards": 1093.61,
        "feet": 3280.84,
        "inches": 39370.1
    },
    "miles": {
        "km": 1.60934,
        "metres": 1609.34,
        "yards": 1760,
        "feet": 5280,
        "inches": 63360
    },
    "metres": {
        "km": 0.0001,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    },
    "yards": {
        "km": 0.0009144,
        "metres": 0.9144,
        "miles": 0.000568182,
        "feet": 3,
        "inches": 36
    },
    "feet": {
        "km": 0.0003048,
        "metres": 0.3048,
        "yards": 0.3333,
        "miles": 0.000189394,
        "inches": 12
    },
    "inches": {
        "km": 0.0000254,
        "metres": 0.0254,
        "yards": 0.0277778,
        "feet": 0.0833333,
        "miles": 0.0000157828
    }
}

temperature_units = {
    "Celcius": {
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15
    },
    "Fahrenheit": {
        "Celsius": lambda f: (f - 32) * 5/9,
        "Kelvin": lambda f: (f - 32) * 5/9 + 273.15
    },
    "Kelvin": {
        "Celcius": lambda k: k - 273.15,
        "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
    }
}

volume_units = {
    "gallons": {
        "litres": 3.78541
    },
    "litres": {
        "gallons": 0.264172
    }
}

category_dict = {
    "Distance": distance_units,
    "Temperature": temperature_units,
    "volume": volume_units
}

def converter(category, convert_from, convert_to, value):
    convert = category_dict[category][convert_from][convert_to]
    if callable(convert):
        result = convert(value)
    else:
        result = value * convert
    print(f"\nResult: {value} {convert_from} = {result} {convert_to}")


def user_input(intro, dictionary):
    while True:
        print(intro)
        keys_list = list(dictionary.keys())

        for i, key in enumerate(keys_list, start=1):
            print(f"{i}. {key}")
        choice = input(f"Enter your choice (1-{len(keys_list)}): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(keys_list):
                return keys_list[choice - 1]
            print(f"Please select choice from 1 to {choice}. \n")

def main():
    loop_bool = True
    while(loop_bool):
        print("Welcome to the Unit Converter!")
        # 1. Input Prompt
        category = user_input(
            intro="Please select a category for conversion:",
            dictionary=category_dict
            )
        # 2. Unit Selection
        convert_from_dict = category_dict[category]
        convert_from = user_input(
            intro="Select unit to covert from:",
            dictionary=convert_from_dict
            )
        convert_to_dict = convert_from_dict[convert_from]
        convert_to = user_input(
            intro="Select unit to covert from:",
            dictionary=convert_to_dict
            )
        # 3. Value input
        while True:
            value = input("Enter value to convert: ")
            if value.replace(".", "", 1).replace("-", "", 1).isdigit():
                value = float(value)
                break
            print("Invalid Input! Please enter a number value.\n")
        
        # 4. Conversion Result
        converter(
                category=category,
                convert_from=convert_from,
                convert_to=convert_to,
                value=value
            )

        # 5. Looping
        while True:
            loop_input = input("Would you like to convert again? (yes/no): ")
            if loop_input == "no":
                print("Thank you for using the converter!..")
                loop_bool = False
                break
            elif loop_input == "yes":
                loop_bool = True
                break
            else:
                print("Kindly select choice either yes or no: ")
        print("------------------------------")
        
if __name__ == "__main__":
    main()