import os
import csv
import numpy as np

# Set path for file
pypoll_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
len_cast = 0
candidates = {}

# Open the CSV
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Loop throught the rows to get the total number of votes cast and the list of candidates
    for row in csvreader:
        len_cast += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# To get the candidate with the most votes, we need to get the unique candidates
unique_candidates = np.unique(list(candidates.keys()))

# Construct the result string
result = ""
for candidate in unique_candidates:
    vote_count = candidates[candidate]
    vote_percentage = (vote_count / len_cast) * 100
    winner = max(candidates, key=candidates.get)
    result += f"{candidate}: {vote_count}, {vote_percentage:.2f}%. The winner is {winner}\n"

# Print the analysis to the terminal
print(result)

# Store the result in a text file
filename = "PyPoll/analysis/analysis_results.txt"
with open(filename, "w") as file:
    file.write(result)

print("Results have been exported to the analysis folder:", filename)