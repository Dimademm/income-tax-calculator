# Define the tax brackets and rates
lower_limit_1 = 34431.01
upper_limit_2 = 74416.01
tax_rate_1 = 0.108
tax_rate_2 = 0.1275
tax_rate_3 = 0.174


# Get the income from the user

income = float(input("Please enter employee's annual income... CAD($) "))

# Calculate the tax amount
if income < 0:
    print("Error: Income cannot be negative. Please try again")
    stop

elif income <= lower_limit_1:
    tax_amount = income * tax_rate_1
    bracket = "10.8% [$0, $34,431.01)"
elif income <= upper_limit_2:
    tax_amount = (lower_limit_1 * tax_rate_1) + (income - lower_limit_1) * tax_rate_2
    bracket = "12.75% [$34,431.01, $74,416.01)"
else:
    tax_amount = (lower_limit_1 * tax_rate_1) + (upper_limit_2 - lower_limit_1) * tax_rate_2 + (income - upper_limit_2) * tax_rate_3
    bracket = "17.40% [$74,416.01 +)"

# Print the result
print("Employee's provincial tax Bracket:", bracket)
print("Employes's provincial tax Amount: ${:.2f}".format(tax_amount))

