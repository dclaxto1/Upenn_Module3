import os
import csv

#specify csv file
poll_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
css_votes = 0
dg_votes = 0
rad_votes = 0


#call and open csv file
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        #counting total number of votes = 369711
        total_votes +=1
        #calculating vote totals for each candidate
        if row[2] == "Charles Casper Stockham":
            css_votes +=1
        elif row[2] == "Diana DeGette":
            dg_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            rad_votes +=1
#calculating percentage of vote for each candidate
css_percent = round((css_votes/total_votes) *100,3)
dg_percent = round((dg_votes/total_votes) *100,3)
rad_percent = round((rad_votes/total_votes) *100,3)
winner = ""
winning_vote = 0

#Determining the winner
if int(css_votes) > int(total_votes/2):
    winner = "Charles Casper Stockham"
    winning_vote = css_votes
elif int(dg_votes) > int(total_votes/2):
    winner = "Diana DeGette"
    winning_vote = dg_votes
elif int(rad_votes) > int(total_votes/2):
    winner = "Raymon Anthony Doane"
    winning_vote = rad_votes
else:
    print(f"A runoff election is needed. No candidate received more than 50% of the popular vote")


#pritning election results in terminal
print(f"Election Results!")
print(f"______________________")
print(f"Total votes: {total_votes}")
print(f"______________________")
print(f"Candidates:")
print(f"Charles Casper Stockham: {css_votes}, {css_percent}%")
print(f"Diana DeGette: {dg_votes}, {dg_percent}%")
print(f"Raymon Anthony Doane: {rad_votes}, {rad_percent}%")
print(f"______________________")
print(f"The winner is {winner} with {winning_vote} votes!")
print(f"______________________")

#writing election results to a txt file
output_file = open("analysis/pollresults.txt","w")
output_file.write(f"Election Results!\n")
output_file.write(f"\n")
output_file.write(f"Total votes: {total_votes}\n")
output_file.write(f"\n")
output_file.write(f"Candidates:\n")
output_file.write(f"Charles Casper Stockham: {css_votes}, {css_percent}%\n")
output_file.write(f"Diana DeGette: {dg_votes}, {dg_percent}%\n")
output_file.write(f"Raymon Anthony Doane: {rad_votes}, {rad_percent}%\n")
output_file.write(f"\n")
output_file.write(f"The winner is {winner} with {winning_vote} votes!\n")
output_file.close