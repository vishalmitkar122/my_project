import os
import yaml

def load_config(yaml_file):
    with open('config2.yaml', "r") as file:
        config = yaml.safe_load(file)
    return {key: os.getenv(key.upper(), value) for key, value in config.items()}

def main():
    yaml_file = "config.yaml"
    config = load_config(yaml_file)
    print("Final Configuration:")
    print(yaml.dump(config, default_flow_style=False))

if __name__ == "__main__":
    main()
