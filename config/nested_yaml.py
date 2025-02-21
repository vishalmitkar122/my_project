import yaml

 # Open and load the YAML file
with open('config2.yaml', 'r') as file:
 config = yaml.safe_load(file)  # Correct variable name

 # Extract and print database configuration
database_config = config.get('database', {})  # Use 'config', not 'config1'

 # Iterate and print key-value pairs
for key, value in database_config.items():
 print(f"{key}: {value}")








logging.basicConfig(filename='text.log',level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')

logging.info(" {age - 10}")


