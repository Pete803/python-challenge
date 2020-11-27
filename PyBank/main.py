import os
import csv

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
total_months = 0
net_total = 0
# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# print(budget_csv)
# print(type(budget_csv))
# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip and save header
    column_names = next(csvreader)
    # Loop through the data
    for row in csvreader:
        total_months += 1
        net_total += int(row[1]) 
        print(row)
        
    
analysis_report = (
    f"There are {total_months} total months in this data set\n"
    f"The net total of data set is ${net_total}\n"
)
print(analysis_report)

with open("Analysis_Report.txt",'w') as outputfile:
    outputfile.write(analysis_report)