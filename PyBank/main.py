import os
import csv
import statistics
os.getcwd()

filepath = os.path.join("Desktop", "python-challenge", "Pybank", "budget_data_copy.csv")

with open(filepath, 'r', newline="") as csvfile:
    csvcontent = csv.reader(csvfile, delimiter=",")

    header = next(csvcontent)
    tot_months = sum(1 for line in csvcontent)

total = 0


with open(filepath, 'r', newline="") as csvfile:
    csvcontent = list(csv.reader(csvfile, delimiter=","))
    
    maxvalrow = csvcontent[26]
    maxvaldate = maxvalrow[0]

    minvalrow = csvcontent[45]
    minvaldate = minvalrow[0]
    

with open(filepath, 'r', newline="") as csvfile:
    csvcontent = csv.reader(csvfile, delimiter=",")

    profloss = []

    header = next(csvcontent)
    for i in csvcontent:
        profloss.append(i[1])

    new_profloss = []

    for j in profloss:
        new_profloss.append(int(j))
    profloss = new_profloss

    for k in new_profloss:
        total = total + k

    avg_change = round((total/tot_months),2)

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {maxvaldate} (${max(new_profloss)})")
print(f"Greatest Decrease in Profits: {minvaldate} (${min(new_profloss)})")

minpos = new_profloss.index(min(new_profloss))

maxpos = new_profloss.index(max(new_profloss))

f= open("PyBankAnalysis.txt","w+")

f.write("Financial Analysis")
f.write("\n------------------------------")
f.write(f"\nTotal Months: {tot_months}")
f.write(f"\nTotal: ${total}")
f.write(f"\nAverage Change: ${avg_change}")
f.write(f"\nGreatest Increase in Profits: {maxvaldate} (${max(new_profloss)})")
f.write(f"\nGreatest Decrease in Profits: {minvaldate} (${min(new_profloss)})")

f.close()