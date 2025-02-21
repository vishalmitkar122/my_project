import yaml


# Load YAML file
with open("config5.yaml", "r") as file:
    config = yaml.safe_load(file)

# Extract required configurations
auth_config = config["app"]["components"]["auth"]
cache_config = config["app"]["components"]["cache"]

# Print configurations in a formatted way
print("Authentication Configuration:")
print(f"  Enabled: {auth_config['enabled']}")
print(f"  Method: {auth_config['method']}\n")

print("Cache Configuration:")
print(f"  Value: {cache_config}")


