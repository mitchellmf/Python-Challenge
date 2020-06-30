import pandas as pd
import csv as csv
budget_df = pd.read_csv(r"C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW3 - Python\budget_data.csv")
budget_df.head()

f = open("PyBank.txt", "w")

unique_months = len(budget_df["Date"].unique())
total_profloss = budget_df["Profit/Losses"].sum()
avg_profloss = budget_df["Profit/Losses"].mean()
max_inc = budget_df["Profit/Losses"].max()
min_inc = budget_df["Profit/Losses"].min()

print(f"Total Months: {unique_months}")
print(f"Total: {total_profloss}")
print(f"Average Change: {avg_profloss}")
print(f"Greatest Increase in Profits: {max_inc}")
print(f"Greatest Decrease in Profits: {min_inc}")

print(f"Total Months: {unique_months}", file=f)
print(f"Total: {total_profloss}", file=f)
print(f"Average Change: {avg_profloss}", file=f)
print(f"Greatest Increase in Profits: {max_inc}", file=f)
print(f"Greatest Decrease in Profits: {min_inc}", file=f)

f.close()
