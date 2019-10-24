# 4-11 Weight Loss Program
Calculates expected weight at the end of each month over a 6-month period, given a user-supplied starting weight and assuming a loss of 4 pounds each month.

# Scope
If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds a month. Write a program (using a loop) that lets the user enter their starting weight, then creates and displays a table showing what their expected weight will be at the end of each month for the next 6 months if they stay on this diet.

## Sample Run
    What is your starting weight?  185
    At the end of month 1 your weight will be 181 lbs.
    At the end of month 2 your weight will be 177 lbs.
    At the end of month 3 your weight will be 173 lbs.
    At the end of month 4 your weight will be 169 lbs.
    At the end of month 5 your weight will be 165 lbs.

## Pseudocode
    START
    Set loss rate constant = 4
    Prompt user for starting weight
    FOR each of 6 months
      calculate the new weight
        weight = weight - loss rate
      print weight
    END
