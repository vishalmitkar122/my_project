import json

# Load JSON file
with open("second.json", "r") as file:
    data = json.load(file)

# Check if 'database' key exists and is a dictionary
if "database" in data and isinstance(data["database"], dict):
    print("Database ")
    for key, value in data["database"].items():
        print(f"{key}: {value}")
else:
    print("No 'database' object found in the JSON file.")
