# Unit Converter

This is a Python-based **Unit Converter** program that allows users to easily convert between various units of measurement for:
- **Length**
- **Weight**
- **Temperature**
- **Time**
- **Volume**

## How It Works
1. The user selects a conversion type by entering a number (e.g., `1` for Length, `2` for Weight, etc.).
2. The program displays the supported units for the selected conversion type.
3. The user inputs:
   - The value they wish to convert.
   - The unit they are converting from.
   - The unit they are converting to.
4. The program calculates the result and displays it.

## Features
- **Length Conversion**: meter (m), kilometer (km), mile, centimeter (cm).
- **Weight Conversion**: kilogram (kg), gram (g), pound (lb), ounce (oz).
- **Temperature Conversion**: Celsius (C), Fahrenheit (F), Kelvin (K).
- **Time Conversion**: seconds (s), minutes (min), hours (h).
- **Volume Conversion**: liter (L), milliliter (mL), gallon (gal).

## Modular Design
The program is divided into separate Python files for better maintainability:
- `Length.py` for length conversions.
- `Weight.py` for weight conversions.
- `Temp.py` for temperature conversions.
- `Time.py` for time conversions.
- `Volume.py` for volume conversions.

## Usage
1. Clone the repository.
2. Run the `main.py` file using Python 3:
   ```bash
   python Main.py
   ```
3. Follow the on-screen instructions to perform conversions.

## Example
### Input:
```
1 (Select Length)
1000 (Value to Convert)
m (From Unit)
km (To Unit)
```
### Output:
```
m to km is: 1.0
```

## Credits
Coded by **The GD / Taha**  
