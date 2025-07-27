#!/usr/bin/env python3
"""
Temperature Conversion Tool

This script demonstrates the concept of variable scope by using global variables
to store conversion factors for temperature conversions between Celsius and Fahrenheit.
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature converted to Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature converted to Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Get temperature input from user
        temp_input = input("Enter the temperature to convert: ").strip()
        
        # Validate that input is a numeric value
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Get unit specification from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on unit
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
