#CSV Layout
#Voter ID, County, Candidate

# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates
# each of the following:
        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        #  The winner of the election based on popular vote.

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

import os
import csv

total_votes = 0
candidate_count = {}
unique_candidates = []
vote_count_per = []
percent_won = []
candidate_analysis = []

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip and save header
    column_names = next(csvreader)

    # Count total votes
    for row in csvreader:
        total_votes = total_votes + 1
        
        if (row[2] in candidate_count):
            candidate_count[row[2]] += 1
        # If this is 1st vote for candidate, then set vote count =1    
        else:
            candidate_count[row[2]] = 1
            
winner = ""
winner_count = 0
for candidate in candidate_count:
    if candidate_count[candidate] > winner_count:
        winner_count = candidate_count[candidate]
        winner = candidate

# Analysis Report    
analysis_report = (
     "Election Results\n"
     "-------------------------------\n"
    f"Total Votes: {total_votes}\n"
     "-------------------------------\n"
     )
for candidate in candidate_count:
    analysis_report += f"{candidate} = "
    analysis_report += f"{candidate_count[candidate]} ("
    analysis_report += f"{round((candidate_count[candidate]/total_votes)*100,2)}%)\n"
analysis_report +="-------------------------------\n"

analysis_report += f"Winner: {winner}\n"
print(analysis_report)

with open("Analysis_Report_Election.txt",'w') as outputfile:
    outputfile.write(analysis_report)