# Unit Converter

## Overview

The **Unit Converter** is a Python-based command-line tool that helps users convert various types of units of measurement, such as **distance**, **volume**, **temperature**, **speed**, and more. It provides a straightforward interface where users can select the unit type they want to convert (e.g., kilometers to miles) and input the value to be converted. The tool then outputs the converted value.

This library supports multiple unit conversions, ensuring accurate and efficient conversion across different measurement types.

## License

The code is released under the **GNU General Public License v3.0**. You can freely use, modify, and redistribute the code, but it comes with no warranty.

For more details, see the full license text: [GNU General Public License v3.0](https://www.gnu.org/licenses/).

## Author

**Developer Jarvis** (Pen Name)
[GitHub Profile](https://github.com/DeveloperJarvis)

## Installation

To use the Unit Converter, you can either clone the repository or directly download the Python script.

### Clone the repository:

```bash
git clone https://github.com/DeveloperJarvis/unit_converter.git
cd unit_converter
python unit_converter.py
```

Alternatively, you can download the `unit_converter.py` script directly from the repository.

## Usage

### Running the Unit Converter

Run the script in your terminal to start the unit converter.

```bash
python unit_converter.py
```

The program will guide you through selecting the unit type (e.g., distance, temperature), the source unit, the target unit, and the value you wish to convert.

### Sample Interaction

```plaintext
Welcome to the Unit Converter!
Please select a category for conversion:
1. Distance
2. Temperature
3. Volume
4. Speed
Enter your choice (1-4): 1

Select the units to convert:
1. Kilometers to Miles
2. Miles to Kilometers
3. Meters to Yards
Enter your choice (1-3): 1

Enter the value to convert (in Kilometers): 10

10 Kilometers = 6.21371 Miles

Would you like to convert again? (yes/no): yes
```

### Available Categories

1. **Distance**: Convert between kilometers, miles, meters, yards, feet, etc.
2. **Temperature**: Convert between Celsius, Fahrenheit, and Kelvin.
3. **Volume**: Convert between liters, milliliters, gallons, pints, etc.
4. **Speed**: Convert between meters per second, kilometers per hour, miles per hour, etc.

### Example Conversion:

- Convert 10 kilometers to miles.
- Convert 25 Celsius to Fahrenheit.
- Convert 3 liters to gallons.
- Convert 15 meters per second to kilometers per hour.

## Code Structure

- **Conversion Functions**: Functions to convert between different units, each having predefined conversion factors/formulas.
- **CLI Interface**: Interactive command-line interface for user input.
- **Error Handling**: Ensures valid input from users and handles invalid choices gracefully.

## Future Enhancements

- **Additional Units**: Adding support for more unit types like weight, area, energy, etc.
- **Currency Conversion**: Integration with live exchange rates for currency conversion.
- **GUI Implementation**: A graphical user interface version of the unit converter.
- **Unit Conversion History**: Track and display the history of conversions performed by the user.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, submit an issue, or open a pull request.

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Write tests if applicable.
- Open a pull request describing your changes.

## Credits

- **Developer Jarvis** (Pen Name), Creator of the Unit Converter.
- Inspired by the need for simple unit conversions in daily life.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

## Creating tag

```bash
# 1. Check existing tags
git tag
# 2. Create a valid tag
git tag -a v1.0.0 -m "Release version 1.0.0"
# or lightweight tag
git tag v1.0.0
# push tag to remote
git push origin v1.0.0
```
