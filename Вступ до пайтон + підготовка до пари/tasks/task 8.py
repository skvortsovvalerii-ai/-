# Student Name: Valerii Skvortsov
# Current Date: May 25, 2026
# Description: This program converts Celsius degrees to Fahrenheit and Kelvin scales.

celsius = 25.0

fahrenheit = 32 + (9 / 5) * celsius
kelvin = celsius + 273.15

print("Fahrenheit:" + format(fahrenheit, "^15.2f"))
print("Kelvin:" + format(kelvin, "^15.2f"))