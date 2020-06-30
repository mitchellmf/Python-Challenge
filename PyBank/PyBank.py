import pandas as pd
import csv as csv
budget_df = pd.read_csv(r"C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW3 - Python\budget_data.csv")
budget_df.head()

f = open("PyBank.txt", "w")

unique_months = len(budget_df["Date"].unique())
print(f"Total Months: {unique_months}", file=f)
total_profloss = budget_df["Profit/Losses"].sum()
print(f"Total: {total_profloss}", file=f)
avg_profloss = budget_df["Profit/Losses"].mean()
print(f"Average Change: {avg_profloss}", file=f)
max_inc = budget_df["Profit/Losses"].max()
print(f"Greatest Increase in Profits: {max_inc}", file=f)
min_inc = budget_df["Profit/Losses"].min()
print(f"Greatest Decrease in Profits: {min_inc}", file=f)

f.close()
