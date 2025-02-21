import yaml

with open("config1.yaml", "r") as file:
    config = yaml.safe_load(file)

port = config["database"]["port"]
level = config["logging"]["level"]

if not (1024 <= port <= 65535):
    print("Error: Invalid database port.")
elif level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
    print("Error: Invalid logging level.")
else:
    print("Configuration is valid!")