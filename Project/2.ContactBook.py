# Q2: Casper Contact Book (OOP + JSON + Search)
# Build a contact book using classes. Allow the user to:
# Add new contacts (name, email, tags)
# Search by name or tag using a lambda function
# Store and load contacts using a JSON file
import pandas as pd
import os
import json

# Load or initialize the contact book
if os.path.exists("2.json"):
    with open("2.json", "r") as f:
        data = json.load(f)
        df = pd.DataFrame(data)
else:
    df = pd.DataFrame(columns=["name", "tags", "gmail"])

class Contacts:
    i = len(df)

    def __init__(self, name, tags, gmail):
        self.name = name
        self.tags = [tag.strip().lower() for tag in tags.split(",")]  # tags as list
        self.gmail = gmail

        df.at[Contacts.i, "name"] = name
        df.at[Contacts.i, "tags"] = self.tags
        df.at[Contacts.i, "gmail"] = gmail
        Contacts.i += 1

    def search_by_tag(self, tag):
        tag = tag.lower().strip()
        results = df[df["tags"].apply(lambda t: tag in t)]
        print("\n🔍 Search by Tag:")
        print(results if not results.empty else "No matching contacts found.")

    def search_by_name(self, name):
        name = name.lower().strip()
        results = df[df["name"].str.lower().str.contains(name)]
        print("\n🔍 Search by Name:")
        print(results if not results.empty else "No matching contacts found.")

# Get contact details from user
name = input("Enter your name: ")
tags = input("Enter your tags (comma separated): ")
gmail = input("Enter your Gmail: ")

# Create and store the contact
person = Contacts(name, tags, gmail)

# Save to JSON
with open("2.json", "w") as f:
    f.write(df.to_json(orient="records", indent=4))

# Ask user for search
print("\nSearch Options:")
print("1. Search by tag")
print("2. Search by name")
choice = input("Choose 1 or 2: ")

if choice == "1":
    tag = input("Enter tag to search: ")
    person.search_by_tag(tag)
elif choice == "2":
    name = input("Enter name to search: ")
    person.search_by_name(name)
else:
    print("Invalid choice.")
