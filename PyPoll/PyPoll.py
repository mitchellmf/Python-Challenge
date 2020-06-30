import pandas as pd
import csv as csv
election_df = pd.read_csv(r"C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW3 - Python\election_data.csv")
election_df.head()

f = open("PyPoll.txt", "w")

unique_cands = (election_df["Candidate"].unique())
unique_cands 

total_votes = election_df["Candidate"].count()

only_correy = election_df.loc[(election_df["Candidate"] == "Correy")]
total_correy = only_correy["Candidate"].count()
perc_correy = round((total_correy *100 / total_votes ),2)

only_khan = election_df.loc[(election_df["Candidate"] == "Khan")]
total_khan = only_khan["Candidate"].count()
perc_khan = round((total_khan *100 / total_votes ),2)
	
only_li = election_df.loc[(election_df["Candidate"] == "Li")]
total_li = only_li["Candidate"].count()
perc_li = round((total_li *100 / total_votes ),2)

only_otooley = election_df.loc[(election_df["Candidate"] == "O'Tooley")]
total_otooley = only_otooley["Candidate"].count()
perc_otooley = round((total_otooley *100 / total_votes ),2)



all_votes = []
all_votes.append(total_correy)
all_votes.append(total_khan)
all_votes.append(total_li)
all_votes.append(total_otooley)
all_votes

all_cands = []
all_cands.append(total_correy)
all_cands.append(total_khan)
all_cands.append(total_li)
all_cands.append(total_otooley)
all_cands

winner = max(all_votes)
winner

if winner == total_correy:
    winner_name = "Correy"
elif winner == total_khan:
    winner_name = "Khan"
elif winner == total_li:
    winner_name = "Li"
elif winner == total_otooley:
    winner_name = "O'Tooley"
winner_name

print(f"Total Votes: {total_votes}", file=f)
print(f"Correy: {perc_correy}% ({total_correy})", file=f)
print(f"Khan: {perc_khan}% ({total_khan})", file=f)
print(f"Li: {perc_li}% ({total_li})", file=f)
print(f"O'Tooley: {perc_otooley}% ({total_otooley})", file=f)
print(f"Winner: {winner_name}", file=f)

f.close()
