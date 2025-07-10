# Prompt the user for income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Projected annual savings with 5% interest
projected_savings = monthly_savings * 12 + ( monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
