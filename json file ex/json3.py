import json

with open("json3.json", "r") as file:
    data = json.load(file)

# Print database key-value pairs
print("Database contents:")
for key, value in data.get("database", {}).items():
    print(f"{key}: {value}")

# Print services name and URL
print("\nServices:")
for service in data.get("services", []):
    print(f"Name: {service.get('name', 'Unknown')}, URL: {service.get('url', 'No URL provided')}")
