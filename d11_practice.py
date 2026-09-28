# Step 1 — Install pandas
import pandas as pd # pd is simply the conventional short alias programmers use for pandas. 

print(pd.__version__)

# Step 2 — Your first DataFrame
# df is the conventional short name for DataFrame.

import pandas as pd

requests = [
    {"id": 101, "approver": "Team Leader", "status": "Approved"},
    {"id": 102, "approver": "Data Steward", "status": "Pending"},
    {"id": 103, "approver": "Product Owner", "status": "Rejected"},
    {"id": 104, "approver": "Team Leader", "status": "Approved"},
]

df = pd.DataFrame(requests)

print(df)
print(type(df))

# Step 3 — Explore the DataFrame

# df.shape - tells you the DataFrame's rows × columns. - (rows, columns)
# df.columns - tells you the column names.
# df.head() - shows the first 5 rows by default.

print(df.shape)
print(df.columns)
print(df.head())

# Step 4 — Select columns

print(df["status"])             # prints 1 column: status
print(df[["id", "status"]])     # prints multiple columns: id & status

# Step 5 — Filter without a for loop

# It returns a True/False Series for every row,
# Then we use that True/False result as a filter.

print(df["status"] == "Approved")

# returns only the Approved rows.

approved_df = df[df["status"] == "Approved"]

print(approved_df)

# Step 6 — Count statuses

print(df["status"].value_counts())

# Step 7 — Sorting a DataFrame


requests = [
    {"id": 101, "approver": "Team Leader", "status": "Approved"},
    {"id": 102, "approver": "Data Steward", "status": "Pending"},
    {"id": 103, "approver": "Product Owner", "status": "Rejected"},
    {"id": 104, "approver": "Team Leader", "status": "Approved"},
]

df = pd.DataFrame(requests)

sorted_df = df.sort_values("id", ascending=False)

print(sorted_df)

# Step 8 — Grouping

approver_counts = df.groupby("approver").size() # group rows by approver → count how many rows are in each group.

print(approver_counts)

# Step 9 — Read a real CSV with pandas

approval_df = pd.read_csv("approval_requests.csv")

print(approval_df)
print(approval_df.shape)

# Step 10 — Final Day 11 challenge
# Total requests: 7
# Approved: 3
# Pending: 2
# Rejected: 2

print(f"Total requests: {approval_df.shape[0]}")
print(approval_df["status"].value_counts())