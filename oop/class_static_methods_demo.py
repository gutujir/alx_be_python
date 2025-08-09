class Calculator:
    """A class demonstrating class methods and static methods."""

    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method to add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.

        Args:
            cls: Reference to the class
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
