import yaml

#Ex 1 - basic configuration working with yaml file

# read yaml file
with open ("config.yaml",'r') as file:
    config = yaml.safe_load(file)


    print("App name:", config.get('app_name'))
    print('Version:',config.get('version'))
    print('Author :', config.get('author'))

