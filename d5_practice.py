# Day 5 — Python + CSV Data

# import csv -> loads Python's built-in CSV functionality
# open(....) -> opens your file
# with -> automatically closes the file when Python finishes
# csv.DictReader() -> converts each CSV row into a dictionary using the header names

# CSV → DictReader → dictionary → access individual columns → formatted output


import csv

# approved_count = 0
# pending_count = 0
# rejected_count = 0

# with open("approval_requests.csv", "r") as file:
#     reader = csv.DictReader(file)

    # for row in reader:
    #     print(row)

    # for row in reader:
    #     print(f"Request {row['id']} - {row['approver']} - {row['status']}")

#CSV file → DictReader → each row → check status → increment counter → final summary
    # for row in reader:
    #     if row['status'] == 'Approved':
    #         approved_count += 1
    #     elif row['status'] == 'Pending':
    #         pending_count += 1
    #     elif row['status'] == 'Rejected':
    #         rejected_count += 1
    #     else:
    #         print("Unknown request")

    #print(f"Approved: {approved_count}, Pending: {pending_count}, Rejected: {rejected_count}")
    # print(f"Approved: {approved_count}")
    # print(f"Pending: {pending_count}")
    # print(f"Rejected: {rejected_count}")


# What's happening here
# "approval_requests.csv"
#         ↓
#      filename
#         ↓
# open(filename, "r")
#         ↓
#    reads that file

# filename here is variable
# def summarize_csv(filename): # makes your function reusable.
#     approved_count = 0
#     pending_count = 0
#     rejected_count = 0

#     with open(filename, "r") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             if row['status'] == 'Approved':
#                 approved_count += 1
#             elif row['status'] == 'Pending':
#                 pending_count += 1
#             elif row['status'] == 'Rejected':
#                 rejected_count += 1
#             else:
#                 print("Unknown request")
#         return approved_count, pending_count, rejected_count


    

##call the function using the actual filename: approval_requests.csv
# approved, pending, rejected = summarize_csv("approval_requests.csv")

# print(f"Approved: {approved}")
# print(f"Pending: {pending}")
# print(f"Rejected: {rejected}")


# Step 8 passed. Your function is now reading a real CSV, processing every row, 
# classifying statuses, counting totals, returning multiple values, and handling a missing file.

def summarize_csv(filename): # makes your function reusable.
    total_count = 0
    approved_count = 0
    pending_count = 0
    rejected_count = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['status'] == 'Approved':
                approved_count += 1
            elif row['status'] == 'Pending':
                pending_count += 1
            elif row['status'] == 'Rejected':
                rejected_count += 1
            else:
                print("Unknown request")

            total_count += 1
    return approved_count, pending_count, rejected_count, total_count

# Step 7 — Handle missing files gracefully
try: 
    approved, pending, rejected, total = summarize_csv("approval_requests.csv")

    print(f"Total requests: {total}")
    print(f"Approved: {approved}")
    print(f"Pending: {pending}")
    print(f"Rejected: {rejected}")

except FileNotFoundError:
    print("Error: CSV file not found.")
