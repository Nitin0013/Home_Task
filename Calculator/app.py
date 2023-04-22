def income_tax(total_amount, income_tax_rate):
    return (total_amount * income_tax_rate) / 100


def calculate_income_tax(income_range):
    if income_range <= 250000:
        return 0
    elif income_range <= 500000:
        return income_tax(income_range - 250000, 5)
    elif income_range <= 1000000:
        return income_tax(income_range - 500000, 20) + 12500
    else:
        return income_tax(income_range - 1000000, 30) + 112500


if __name__ == "__main__":
    income_range = float(input("Enter Your Total Income : "))
    tax = calculate_income_tax(income_range)
    print(f"Total tax is :  Rs{tax}")
