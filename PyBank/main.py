import os
import csv

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


total_months = 0
net_total = 0
rev_change = 0
max_change = 0
min_change = 0
current_value = 0
previous_value = 0
rev_change_list = []

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip and save header
    column_names = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        current_value = int(row[1])   
        rev_change = current_value - previous_value
        rev_change_list.append(rev_change)
        previous_value = current_value
        print(row)
    
# Analysis Report    
analysis_report = (
    "Analysis Report\n"
    "-------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${rev_change}\n"
    f"Greatest Increase in Profits: {max_change}\n"
    f"Greatest Decrease in Profits: {min_change}\n"

)
print(analysis_report)

with open("Analysis_Report.txt",'w') as outputfile:
    outputfile.write(analysis_report)