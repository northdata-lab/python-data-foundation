# Four core JSON operations:
# A useful way to remember it: the s means string.

# json.dumps()  # Python → JSON string
# json.loads(json_data)     → JSON string → Python

# json.dump()   # Python → JSON file
# json.load(file)           → JSON file -> Python

request = {
    "id": 101,
    "approver": "Team Leader",
    "status": "Approved"
}

print(request)
print(request["status"])
print(request["approver"])

# Step 2 — Python dictionary → JSON

import json

json_data = json.dumps(request) # Converting dictionary to json which makes it to 'String'.

print(json_data)
print(type(request))
print(type(json_data))


# Step 3 — JSON string → Python dictionary

converted_back = json.loads(json_data)

print(converted_back)
print(type(converted_back))
print(converted_back["status"])

# # Step 4 — Read an actual JSON file
# The important part: json.load(file) converts the JSON file into a Python dictionary, not a string.

with open("approval_request.json", "r") as file:
    request_from_file = json.load(file)  # JSON file → Python

print(request_from_file)
print(type(request_from_file))
print(request_from_file["status"])


# Step 5 — Python → JSON file
# Now let's do the opposite and create a JSON file using Python.

new_request = {
    "id": 103,
    "approver": "Product Owner",
    "status": "Rejected"
}

with open("new_request.json", "w") as file:
    json.dump(new_request, file)


# Step 6 — JSON with multiple records

# requests is a list
requests = [
    {"id": 101, "status": "Approved"},
    {"id": 102, "status": "Pending"},
    {"id": 103, "status": "Rejected"},
    {"id": 104, "status": "Approved"}
]

for request in requests:
    if request["status"] == "Approved":
        print(request)


# Step 7 — Final Day 8 challenge
# Let's connect JSON + your previous filtering knowledge.
# Create a JSON file called approval_requests.json containing multiple records:

# Your challenge is to:

# open approval_requests.json → json.load() it → loop through the resulting data → print only "Pending" records.

with open("approval_requests.json", "r") as file:
    request_from_file1 = json.load(file)

    for request in request_from_file1:
        if request["status"] == "Pending":
            print(request)
 