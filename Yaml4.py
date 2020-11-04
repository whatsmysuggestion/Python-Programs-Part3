import yaml

users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

with open('users.yaml', 'w') as f:
    
     yaml.dump(users, f)