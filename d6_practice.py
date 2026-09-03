import csv

# with open("approval_requests.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["status"] == "Rejected":
#             print(row)

# Step 2 — Store the filtered rows

# rejected_requests = []

# with open("approval_requests.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["status"] == "Rejected":
#             rejected_requests.append(row)


# print(rejected_requests)
# print(f"Rejected requests found: {len(rejected_requests)}")

# Step 3 — Write those rows to a new CSV
# You just built your first little ETL-style process:
# Extract CSV → Transform by filtering Rejected → Load into a new CSV.

# rejected_requests = []

# First block: read and filter the input file.

# with open("approval_requests.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["status"] == "Rejected":
#             rejected_requests.append(row)

# Second block: write the results to the output file.

# with open("rejected_requests.csv", "w", newline="") as file:
#     fieldnames = ["id", "approver", "status"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerows(rejected_requests)

# Step 5 — Make the filter reusable


# def filter_requests(status):
#     matching_requests = []

#     with open("approval_requests.csv", "r") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             if row["status"] == status:
#                 matching_requests.append(row)

#     return matching_requests


# result = filter_requests("Rejected")
# print(result)

# print(filter_requests("Approved"))
# print(filter_requests("Pending"))

# Step 6 — Combine filtering + CSV writing
# 🟢 You've now built a small reusable Extract → Filter → Export pipeline yourself. 

def filter_requests(status):
    matching_requests = []

    with open("approval_requests.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["status"] == status:
                matching_requests.append(row)

        return matching_requests

def write_requests(filename, requests):
    with open(filename, "w", newline="") as file:
        fieldnames = ["id", "approver", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(requests)


filtered = filter_requests("Rejected")
write_requests("rejected_requests.csv", filtered)


