# Program 4-11 Weight Loss
# Shaun Hayworth
# CIS-2
# 10-24-2019
# Orinal source code and revision history can be found at https://github.com/SCHayworth/4-11-Weight-Loss

# Calculates expected weight at the end of each month over a 6-month period, given a user-supplied starting weight and assuming a loss of 4 pounds each month.

# Initialize LOSS_RATE constant at 4
# Change this value if the estimated rate of loss each month changes
LOSS_RATE = 4

# Prompt user for starting weight
weight = int(input('What is your starting weight in pounds? '))

for month in range (1, 6):

    # Calculate weight at the end of the current month
    weight -= LOSS_RATE

    # Print weight for the current month
    print(f'At the end of month {month} your weight will be {weight} lbs.')
