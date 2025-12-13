### **Low-Level Design (LLD) for a Unit Converter**

A **Unit Converter** is a tool that allows users to convert one unit of measurement to another. The design for a **Unit Converter** would handle various types of conversions, such as distance, temperature, volume, and speed. Below is the low-level design (LLD) for such a system, broken down into key components and features.

---

### **1. System Overview**

The **Unit Converter** is a Python-based command-line tool that supports multiple unit conversions. It will provide the user with the ability to convert values between different measurement units such as:

- **Distance**: Kilometers (km), Meters (m), Miles (mi), Yards (yd), etc.
- **Temperature**: Celsius (°C), Fahrenheit (°F), Kelvin (K), etc.
- **Volume**: Liters (L), Milliliters (mL), Gallons (gal), etc.
- **Speed**: Meters per second (m/s), Kilometers per hour (km/h), Miles per hour (mph), etc.

---

### **2. Core Components**

#### **a. Unit Conversion Logic**

The core of the converter is the logic that performs the mathematical conversions between units. This will involve:

- Predefined conversion rates or formulas between units (e.g., miles to kilometers, Celsius to Fahrenheit, etc.).
- Ensuring that each unit type has its respective conversion formulas stored.

**Conversion Examples**:

- **Distance**: 1 mile = 1.60934 kilometers
- **Temperature**: ( \text{Celsius to Fahrenheit} ) = ( \frac{9}{5} \times \text{Celsius} + 32 )
- **Volume**: 1 gallon = 3.78541 liters
- **Speed**: 1 m/s = 3.6 km/h

#### **b. User Interface (CLI)**

The user will interact with the converter via the command line interface (CLI). The steps for this interaction:

1. **Input Prompt**: Ask the user for the conversion they want to perform (e.g., Distance, Temperature).
2. **Unit Selection**: Ask the user to select the specific units they want to convert (e.g., kilometers to miles).
3. **Value Input**: Ask the user for the numeric value to convert.
4. **Conversion Result**: Display the converted value to the user.
5. **Looping**: After displaying the result, prompt the user if they would like to convert again.

---

### **3. Functional Components**

#### **a. Unit Conversion Functions**

Each category of units (e.g., distance, temperature, speed) will have its own function or set of functions to handle the conversion logic.

For example:

- **Distance Conversion**: Converts values between miles, kilometers, meters, etc.
- **Temperature Conversion**: Converts between Celsius, Fahrenheit, Kelvin, etc.
- **Volume Conversion**: Converts between liters, milliliters, gallons, etc.
- **Speed Conversion**: Converts between meters per second, kilometers per hour, miles per hour, etc.

#### **b. Input Validation**

To prevent invalid conversions, the system must ensure that:

- The user selects a valid category (distance, temperature, etc.).
- The units selected belong to the chosen category (e.g., temperature units like Celsius, Fahrenheit, and Kelvin).
- The input value is a valid numeric value.

#### **c. Conversion Data Structure**

A data structure will be used to store the conversion formulas and factors for different units. For instance:

- A dictionary or list of tuples could store conversion rates (e.g., for distance: miles to kilometers, kilometers to miles, etc.).
- Each unit type (distance, temperature, etc.) will have a separate dictionary.

#### **d. Error Handling**

The system should handle cases where the user provides invalid input, such as:

- Selecting invalid units.
- Entering non-numeric values for the conversion.
- Incorrect conversion attempts (e.g., trying to convert temperature to volume).

---

### **4. Data Structure Design**

**Conversion Data**: The following structure will represent the conversion data for each category.

Example for **Distance Conversion**:

```python
distance_units = {
    "km": {
        "miles": 0.621371,
        "meters": 1000,
        "yards": 1093.61,
        "feet": 3280.84
    },
    "miles": {
        "km": 1.60934,
        "meters": 1609.34,
        "yards": 1760,
        "feet": 5280
    },
    # other units...
}
```

Example for **Temperature Conversion**:

```python
temperature_units = {
    "Celsius": {
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15
    },
    "Fahrenheit": {
        "Celsius": lambda f: (f - 32) * 5/9,
        "Kelvin": lambda f: (f - 32) * 5/9 + 273.15
    },
    # other units...
}
```

---

### **5. System Flow (Workflow)**

1. **Start the Program**:

   - The program welcomes the user and presents options for conversion categories (distance, temperature, etc.).
   - User selects a category.

2. **Unit Selection**:

   - After selecting a category, the user is prompted to select the source unit and the target unit (e.g., kilometers to miles).

3. **Input Value**:

   - The user enters a numeric value that they want to convert.

4. **Perform the Conversion**:

   - The program checks if the units are valid for the selected category.
   - It performs the appropriate mathematical conversion using the predefined formulas or conversion rates.

5. **Display the Result**:

   - The converted value is shown to the user in the selected target unit.

6. **Repeat**:

   - The user is asked if they want to perform another conversion. If they choose "yes," the program repeats the process. If they choose "no," the program exits.

---

### **6. Example User Interaction**

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

---

### **7. Error Handling and Edge Cases**

- **Invalid Input**: If the user inputs a non-numeric value when asked for a number, the program should ask them again.
- **Invalid Unit Choice**: If the user selects units that are incompatible with the selected category, display an error message and prompt them to choose again.
- **Out of Range**: Ensure that the entered numeric values are within valid ranges (e.g., no negative values for distances or volumes unless they represent absolute values).

---

### **8. Future Enhancements**

- **Advanced Unit Support**: Support for additional unit types like weight, area, etc.
- **GUI Implementation**: A graphical user interface (GUI) version of the unit converter for easier interaction.
- **Currency Conversion**: Integration with live exchange rates for currency conversion.
- **Unit Conversion History**: Track and display past conversions to the user.
- **Batch Conversion**: Allow users to convert multiple values at once (e.g., multiple distances).

---

### **9. Pseudo-Algorithm**

```plaintext
1. Display a menu of available categories (distance, temperature, etc.).
2. User selects a category.
3. Based on category, display available units.
4. User selects source unit and target unit.
5. Prompt user for numeric value to convert.
6. Perform the conversion using predefined conversion rates or formulas.
7. Display the result.
8. Ask if the user wants to perform another conversion.
9. If yes, repeat. If no, exit.
```

---

### **10. Technologies Used**

- **Python**: Used for implementing the logic.
- **CLI (Command Line Interface)**: For interaction with the user.
- **Data Structures**: Dictionaries or lists to store unit conversion rates.
