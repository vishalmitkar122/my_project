import yaml
import sys

# Load the YAML file
with open("config4.yaml", "r") as file:
    config = yaml.safe_load(file)

# Get the environment from the command-line argument
if len(sys.argv) != 2:
    print("Usage: python read_config.py [dev|prod]")
    sys.exit(1)

env = sys.argv[1]

# Fetch and print the environment configuration
try:
    env_config = config["environment"][env]
    print(f"Configuration for '{env}':")
    for key, value in env_config.items():
        print(f"{key}: {value}")
except KeyError:
    print("Invalid environment. Choose 'dev' or 'prod'.")
