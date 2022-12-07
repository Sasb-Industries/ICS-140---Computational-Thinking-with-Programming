"""
ICS 140
Summer 2022
Assignment 9
Name: xxxxx xxxxxxxx

Use this file to complete assignment 9.
"""

def county_tax(sales):
    county_tax = 0.025
    return sales * county_tax
    # This function should receive the sales for a month and return the county tax

def state_tax(sales):
    state_tax = 0.05
    return sales * state_tax
    # This function should receive the sales for a month and return the county tax

def total_tax(county, state):
    return county + state

def main():
    sales = float(input("Please enter in amount to calculate tax : "))
    state = state_tax(sales)
    county = county_tax(sales)
    total = total_tax(state,county)
    print(f"The county tax is : ${county:.2f}")
    print(f"The state tax is :  ${state:.2f}")
    print(f"The total tax is :  ${total:.2f}")

if __name__ == '__main__':
    main()