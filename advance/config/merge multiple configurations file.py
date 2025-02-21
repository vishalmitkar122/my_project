import yaml
import os
from collections.abc import Mapping


def load_yaml(file_path):
    """Load YAML file and return the data."""
    with open('multiple1.yaml', "r") as file:
        return yaml.safe_load(file) or {}


def deep_merge(dict1, dict2):
    """Recursively merge two dictionaries, with dict2 taking precedence."""
    for key, value in dict2.items():
        if isinstance(value, Mapping) and key in dict1 and isinstance(dict1[key], Mapping):
            dict1[key] = deep_merge(dict1[key], value)
        else:
            dict1[key] = value
    return dict1


def main():
    base_config = load_yaml("base_config.yaml")
    override_config = load_yaml("override_config.yaml")

    merged_config = deep_merge(base_config, override_config)

    print("Final Merged Configuration:")
    print(yaml.dump(merged_config, default_flow_style=False))


if __name__ == "__main__":
    main()
