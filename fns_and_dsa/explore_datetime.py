#!/usr/bin/env python3
"""
Explore datetime Module

This script demonstrates the use of Python's datetime module for handling
dates and times, including displaying current datetime and calculating future dates.
"""

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in a readable format.
    
    This function:
    - Gets the current date and time using datetime.now()
    - Saves it in a current_date variable
    - Formats and prints it as "YYYY-MM-DD HH:MM:SS"
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")


def calculate_future_date():
    """
    Calculate and display a future date based on user input.
    
    This function:
    - Prompts the user to enter a number of days
    - Saves the future date in a future_date variable
    - Calculates the date after adding the specified days
    - Prints the future date in "YYYY-MM-DD" format
    """
    try:
        # Get user input for number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)
        
        # Calculate future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        
        # Format and display the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to run the datetime exploration demo.
    """
    print("=== DateTime Module Exploration ===")
    print()
    
    # Part 1: Display current date and time
    display_current_datetime()
    print()
    
    # Part 2: Calculate future date
    calculate_future_date()


if __name__ == "__main__":
    main()
