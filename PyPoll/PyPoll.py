import os
import csv
from collections import Counter

# set the path for the input CSV file
election_data_csv = os.path.join("Resources", "election_data.csv")

# open the CSV file and create a CSV reader object
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # skip the header row
    next(csv_reader)
    
    # count the total number of votes using a Counter object
    vote_counts = Counter()
    for row in csv_reader:
        candidate_name = row[2]
        vote_counts[candidate_name] += 1

# calculate the total number of votes
total_votes = sum(vote_counts.values())

# print the election results
print("Election Results")
print("-" * 45)
print(f"Total Votes: {total_votes}")
print("-" * 45)

# print the vote counts and percentages for each candidate
for candidate_name, vote_count in vote_counts.items():
    percentage = (vote_count / total_votes) * 100
    print(f"{candidate_name}: {percentage:.2f}% ({vote_count})")

print("-" * 45)

# determine the winner based on the popular vote
winner = vote_counts.most_common(1)[0][0]
print(f"Winner: {winner}")

print("-" * 45)