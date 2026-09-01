# Warm up - Loop condition
# for = repeat through items, if/elif/else = decide what to do, print() = display the result.
# For comparison, use ==

statuses = ["Approved", "Pending", "Rejected", "Approved", "Pending", "Approved"]

for status in statuses:
    if status == "Approved":
        print("Approved request")
    elif status == "Pending":
        print("Waiting for approval")
    else:
        print("Rejected request")
        
# Function (def, return)
#Instead of putting the decision logic directly inside the loop, we can create a reusable function:

# def function_name(parameter):
    # logic
#    return result



def check_status(status):
    if status == "Approved":
        return "Approved request"
    elif status == "Pending":
        return "Waiting for approval"
    elif status == "Rejected":
        return "Rejected request"
    else:
        return "Unknown status"


result = check_status("Approved")
print(result)

result = check_status("Pending")
print(result)

result = check_status("1")
print(result)

result = check_status("1")
print(result)

# Step 4 - Function with a loop
# check_status() function already does one job: take one status and classify it.
# Important idea is: List → loop picks one item → function processes that item → result is printed.
# list -> for loop -> function -> return -> output

def check_status(status):
    if status == "Approved":
        return "Approved request"
    elif status == "Pending":
        return "Waiting for approval"
    elif status == "Rejected":
        return "Rejected request"
    else:
        return "Unknown status"
    
statuses = [
    "Approved", 
    "Pending",
    "Rejected", 
    "Approved", 
    "Pending", 
    "Approved"
]

for status in statuses:
        result = check_status(status)
        print(result)

# Step 5 - Dictionaries

requests = [
    {"id":101, "approver": "Team Leader", "status": "Approved"},
    {"id":102, "approver": "Data Steward", "status": "Pending"},
    {"id":103, "approver": "Product Owner", "status": "Rejected"},
    {"id":104, "approver": "Team Leader", "status": "Approved"}
]

for request in requests:
    print(f"Request {request["id"]} - {request["approver"]} - {request["status"]}")

# Step 6 - Find how many requests are Approved.
requests = [
    {"id":101, "approver": "Team Leader", "status": "Approved"},
    {"id":102, "approver": "Data Steward", "status": "Pending"},
    {"id":103, "approver": "Product Owner", "status": "Rejected"},
    {"id":104, "approver": "Team Leader", "status": "Approved"}
]

# request["status"] == "Approved" -> it's a comparison, so Python returns True or False.
for request in requests:
    print(f"Total approved requests: {request["status"] == "Approved"}")

# Filters approved records
for request in requests:
    if request["status"] == "Approved":
        print(request)

# Counts APPROVED records
approved_count = 0

for request in requests:
    if request["status"] == "Approved":
        approved_count = approved_count + 1

print(f"Total approved requests: {approved_count}")

# Counts PENDING records
pending_count = 0

for request in requests:
    if request["status"] == "Pending":
        pending_count = pending_count + 1

print(f"Total pending requests: {pending_count}")

# Counts REJECTED records
rejected_count = 0

for request in requests:
    if request["status"] == "Rejected":
        rejected_count = rejected_count + 1

print(f"Total rejected requests: {rejected_count}")


#Step 7 - Making code more efficient

approved_count = 0
pending_count = 0
rejected_count = 0

for request in requests:
    if request["status"] == "Approved":
        approved_count = approved_count + 1
    elif request["status"] == "Pending":
        pending_count = pending_count + 1
    elif request["status"] == "Rejected":
        rejected_count = rejected_count + 1
    else:
        print(f"Unknown status: {request['status']}")

print(f"Total approved requests: {approved_count}")
print(f"Total pending requests: {pending_count}")
print(f"Total rejected requests: {rejected_count}")

# Step 8 - Final day challenge
# The key concept is the direction of information: requests → function → processing → return → variables
# return sends data back from a function. print() displays data on your screen.
requests = [
    {"id": 1, "status": "Approved"},
    {"id": 2, "status": "Approved"},
    {"id": 3, "status": "Pending"},
    {"id": 4, "status": "Rejected"}
]

def summarize_requests(requests):
    approved_count = 0
    pending_count = 0
    rejected_count = 0

    for request in requests:
        if request["status"] == "Approved":
            approved_count += 1
        elif request["status"] == "Pending":
            pending_count += 1
        elif request["status"] == "Rejected":
            rejected_count += 1
        else: 
            print(f"Unknown status: {request['status']}")

    return approved_count, pending_count, rejected_count

approved, pending, rejected = summarize_requests(requests)

print(f"Approved: {approved}")
print(f"Pending: {pending}")
print(f"Rejected: {rejected}")


#Second version
def summarize_requests(requests):
    approved_count = 0
    pending_count = 0
    rejected_count = 0

    for request in requests:
        if request["status"] == "Approved":
            approved_count += 1
        elif request["status"] == "Pending":
            pending_count += 1
        elif request["status"] == "Rejected":
            rejected_count += 1
        else: 
            print(f"Unknown status: {request['status']}")

    return approved_count, pending_count, rejected_count

result = summarize_requests(requests)
print(result)
print(type(result))

