# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

#The data we need to retrieve
#1. TThe voter turnout for each county
#2. The percentage of votes from each county out of the total count
#3. The county with the highest turnout

import csv
import os
#Assign a variable for the file to load and the path.
# file_to_load=os.path.join("election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join(("users","gulizdestombe","class","election-analysis", "analysis", "county_results.txt")


#1. Initialize a total vote counter.
total_votes =  0

#County list
counties = []

#County votes dictionary
county_votes = {}

#Largest turnout and percentage count tracker
winning_county=""
largest_turnout=0
turnout_percentage=0

# 2: Track the largest county and county voter turnout.

# Read the csv and convert it into a list of dictionaries
with open("election_results.csv") as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes += 1

        # 3: Extract the county name from each row.
        county_name = row[1]

        # if county does not match any existing county in the county list.
        if county_name not in counties:

            # 4b: Add the existing county to the list of counties, set county_vote dictionary counter to 0.
            counties.append(county_name)
            
            print(county_votes)


        #4c  And begin tracking that county's vote count.
            county_votes[county_name] = 0
        #5.  Add a vote to that county's count
            county_votes[county_name] += 1
            print(county_votes)

# 6a: Write a for loop to get the county from the county dictionary and calculate the percentage of votes
    
for county_name in county_votes:
    #Retrieve vote count of a county.
    votes=county_votes[county_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
print(f"{county_name}: {turnout_percentage:.1f}% ({votes:,})\n")
    #Determine winning vote count and county
    #Determine if the votes are greater than the winning count.
if (votes>largest_turnout) and (vote_percentage>turnout_percentage):
        largest_turnout=votes
        turnout_percentage=vote_percentage
        largest_turnout=county_name
winning_county_summary = (
        f"----------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {largest_turnout:,}\n"
        f"Winning Percentage: {turnout_percentage:.1f}%\n"
        f"-----------------------------\n")
print(winning_county_summary)





# # 8: Save the county with the largest turnout to a text file.
#         txt_file.write(largest_county_summary)
