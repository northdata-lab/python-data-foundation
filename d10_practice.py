# print() displays something. 
# return sends a value back from the function.


# Step 1 — One object vs multiple objects

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, verify=False)  # verify=False is used to ignore SSL certificate verification

print(response.status_code)
users = response.json()

print(type(users))  # <class 'list'>
print(len(users))   # Number of user objects in the list

print(users[0])
print(users[0]["name"])
print(users[0]["email"])

# Step 2 — Loop through API results

for user in users:
    print(user["name"])

# Step 3 — Filter API data yourself

for user in users:
    if user["address"]["city"] == "Gwenborough":
        print(f"{user["name"]} - {user["address"]["city"]}")

# Step 4 — Turn API processing into a function
# Way 1: get all records and filter in Python

def find_users_by_city(users, city):
    for user in users:
        if user["address"]["city"] == city:
            return user

result = find_users_by_city(users, "Gwenborough")
print(result)

# Step 5 — API query parameters
# Python → API with parameter → API filters → Python receives result
# Way 2: send query parameters and let the API filter.
params = {
    "username": "Antonette"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params=params,
    verify=False
)

users = response.json()

print(response.url)
print(users)


# Step 6 - HTTP status handling

import requests

url = "https://jsonplaceholder.typicode.com/users/9999"

response = requests.get(url, verify=False)

print(response.status_code)

if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed")

# Step 7 — Make the API code safer

import requests

# params = {
#     "username": username
# }

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users",
#     params=params,
#     verify=False
# )


# if response.status_code == 200:
#     print("Request successful")
# elif response.status_code == 404:
#     print("User not found")
# else:
#     print(f"Request failed: {response.status_code}")


# Step 8 - Day 10 challenge
# Temporary workaround for corporate SSL certificate issue.
# Do not use verify=False in production.
import requests

def get_user_by_username(username):
    params = {
        "username": username
    }

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        params=params,
        verify=False 
    )

    if response.status_code == 200:
        users = response.json()

        if len(users) > 0:
            user = users[0]
            print(f"Name:{user["name"]}, Username: {user["username"]}, Email: {user["email"]}, City: {user["address"]["city"]}")
        else:
            print("User not found")   
    else:
        print("Request failed")

get_user_by_username("Antonette")






