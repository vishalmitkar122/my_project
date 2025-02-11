import yaml

# Load the YAML file
with open("config3.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract and print service details
services = config.get("services", [])

for service in services:
    name = service.get("name", "Unknown")
    url = service.get("url", "Unknown")
    print(f"Service Name: {name}, URL: {url}")