import os
import csv
import operator

filepath = os.path.join("Desktop", "python-challenge", "PyPoll", "election_data.csv")


vote_dict = {}
vote_count = 0

with open(filepath, 'r', newline="") as csvfile:
    pypoll_csv = csv.reader(csvfile, delimiter=",")

    next(pypoll_csv)
    for row in pypoll_csv:
        if row[2] not in vote_dict:
            vote_dict.update({row[2]:1})
            vote_count += 1

        else:
            vote_dict[row[2]] += 1
            vote_count += 1

locals().update(vote_dict)

khan_percent = round((Khan/vote_count*100),3)
correy_percent = round((Correy/vote_count*100),3)
li_percent = round((Li/vote_count*100),3)
otooley_percent = round(((vote_dict["O'Tooley"])/vote_count*100),3)

OTooley = vote_dict["O'Tooley"]

winner = max(vote_dict.items(), key=operator.itemgetter(1))[0]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
print(f"Khan: {khan_percent}% ({Khan})")
print(f"Correy: {correy_percent}% ({Correy})")
print(f"Correy: {li_percent}% ({Li})")
print(f"Correy: {otooley_percent}% ({OTooley})")
print("-------------------------")
print(f"Winner: {winner}")

f = open("PyPollAnalysis.txt", "w+")

f.write("Election Results")
f.write("\n-------------------------")
f.write(f"\nTotal Votes: {vote_count}")
f.write("\n-------------------------")
f.write(f"\nKhan: {khan_percent}% ({Khan})")
f.write(f"\nCorrey: {correy_percent}% ({Correy})")
f.write(f"\nCorrey: {li_percent}% ({Li})")
f.write(f"\nCorrey: {otooley_percent}% ({OTooley})")
f.write("\n-------------------------")
f.write(f"\nWinner: {winner}")

f.close()