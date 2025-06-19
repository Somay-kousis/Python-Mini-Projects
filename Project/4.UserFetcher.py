# Q4: Random User Fetcher (API + JSON Parsing + File Write)
# Use the Random User API to:
# Fetch 5 random users
# Display each user's name, email, country
# Save this data to a local file (users.json)
# Let the user search by country
# 📌 Hint:
# Use the requests library to fetch data.
# Use .json() to convert the response.
# Save relevant fields only.
# Use a class or simple dictionary list.
# Use lambda with filter() to implement country search.

import requests
import os
import json
import pandas as pd

# Create DataFrame with correct column names
df = pd.DataFrame(columns=["Name", "Email", "Country"])

# Fetch data from API
response = requests.get("https://randomuser.me/api/?results=5")
data = response.json()

# Populate DataFrame
i = 0
for user in data["results"]:
    df.at[i, "Name"] = user["name"]["first"] + " " + user["name"]["last"]
    df.at[i, "Email"] = user["email"]
    df.at[i, "Country"] = user["location"]["country"]
    i += 1

# Search function
def search(country):
    # Filter by matching country (case-insensitive)
    mf = df[df["Country"].str.lower() == country.lower()]
    print(mf)

# Display all fetched users
print(df)

# Run search
search("india")

# Save to JSON file
with open("4.json", "w") as f:
    json.dump(df.to_dict(orient="records"), f, indent=4)
