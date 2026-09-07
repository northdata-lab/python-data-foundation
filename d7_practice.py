# Day 7 objective
# You now have a small but properly structured automation:
# export_requests("Approved")
#         ↓
# validate status
#         ↓
# generate filename
#         ↓
# filter_requests()
#         ↓
# write_requests()
#         ↓
# approved_requests.csv



# Step 2: Automatic filename
# status = "Approved"

# filename = status.lower() + "_requests.csv"  # .lower() converts: Rejected → rejected. Then Python adds: + "_requests.csv". giving: rejected_requests.csv

# print(filename)

# Day 6 code

import csv
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


# Step 3 — Build export_requests() -> 
    # status → filter data → generate filename → create file → write matching records
    # "Pending" → filter Pending records → create filename pending_requests.csv → write those records
# Create a third function that coordinates those two:

# def export_requests(status):
#     filename = status.lower() + "_requests.csv"

#     filtered = filter_requests(status)
#     write_requests(filename, filtered)

# export_requests("Banana")

# Step 4 — Add validation

# Notice the indentation: 
# export_requests()
#     ├── valid statuses
#     ├── if invalid
#     │      └── stop
#     ├── create filename
#     ├── filter
#     └── write

def export_requests(status):
    valid_statuses = ["Approved", "Pending", "Rejected"]

    if status not in valid_statuses:    # It asks: "Is this value NOT contained in this list?"
        print("Invalid status")         # without a value simply stops the function immediately.
        return

    filename = status.lower() + "_requests.csv"

    filtered = filter_requests(status)
    write_requests(filename, filtered)

# export_requests("Approved")
# export_requests("Pending")
# export_requests("Rejected")
export_requests("Banana")
