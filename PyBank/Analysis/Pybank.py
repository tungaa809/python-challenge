import os
import csv
from collections import Counter

# Set the path for the input CSV file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file and store the data in a variable
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data = list(csv_reader)


# Compute the total number of months in the dataset and the total amount of profit/loss
num_months = len(data)
total_profit_loss = sum(int(row[1]) for row in data)

# Compute the average change in profit/loss over the entire period
total_change = 0
prev_profit_loss = 0
for row in data:
    profit_loss = int(row[1])
    change = profit_loss - prev_profit_loss
    total_change += change
    prev_profit_loss = profit_loss
avg_change = round(total_change / (num_months - 1), 2)

# Find the greatest increase and decrease in profit/loss over the entire period
max_increase = 0
max_decrease = 0
max_increase_date = ''
max_decrease_date = ''
prev_profit_loss = 0
for row in data:
    profit_loss = int(row[1])
    date = row[0]
    increase = profit_loss - prev_profit_loss
    if increase > max_increase:
        max_increase = increase
        max_increase_date = date
    if increase < max_decrease:
        max_decrease = increase
        max_decrease_date = date
    prev_profit_loss = profit_loss

# Print out the financial analysis
print("Financial Analysis")
print("-" * 45)
print(f"Total Months: {num_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${avg_change}")
print(f"Greatest increase in profits: {max_increase_date} (${max_increase})")
print(f"Greatest decrease in profits: {max_decrease_date} (${max_decrease})")
