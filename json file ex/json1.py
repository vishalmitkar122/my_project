import json

with open('first.json','r') as file:
    config =json.load(file)

app_name =config.get('app_name','unknown')
version = config.get('version','unknown')
author = config.get('author','nknown')

print(f"app name : {app_name}\nversrion :{version}\n author :{author}")