import os
import csv

# Set path for file
pybank_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Set variables
len_month = 0
total_financials = 0
initial = 0
monthly_change = []

# Open the CSV
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        # Calculate the total number of months included in the dataset
        len_month += 1
        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_financials += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        if initial != 0:
            current_change = int(row[1])
            temp_change = current_change - initial
            monthly_change.append(temp_change)
        
        # Set the initial value to the first row
        initial = int(row[1])

# The average of the changes in "Profit/Losses" over the entire period   
average_change = sum(monthly_change) / len(monthly_change)
max_change = max(monthly_change)
min_change = min(monthly_change)

# Set the index of the max and min change, to get the corresponding change date
max_change_index = monthly_change.index(max_change) + 1
min_change_index = monthly_change.index(min_change) + 1

max_change_date = ""
min_change_date = ""

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Loop through the rows to get the corresponding change date
    for i, row in enumerate(csvreader):
        if i == max_change_index:
            max_change_date = row[0]
        elif i == min_change_index:
            min_change_date = row[0]

# Construct the result string
result = f"Total number of months: {len_month}\n"
result += f"Net total amount of 'Profit/Losses': ${total_financials}\n"
result += f"Average change in 'Profit/Losses': ${average_change}\n"
result += f"Maximum change: ${max_change} in {max_change_date}\n"
result += f"Minimum change: ${min_change} in {min_change_date}\n"

# Print the analysis to the terminal
print(result)

# Export a text file with the results
filename = "PyBank/analysis/analysis_results.txt"
with open(filename, "w") as file:
    file.write(result)

print("Results have been exported to the analysis folder:", filename)
