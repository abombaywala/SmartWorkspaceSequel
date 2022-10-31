import json
from pprint import pprint  # The pprint module automatically formats Python objects for printing.
import yaml
import csv

# Iterating JSON Data
with open('service-policy.json', 'r') as opened_file:
    policy = opened_file.readlines()
print(policy)

with open('service-policy.json', 'r') as opened_file:
    policy = json.load(opened_file)
pprint(policy)

policy['Statement']['Resource'] = 'S3'
pprint(policy)

# Iterating YAML data
# pip install PyYAML - it is not in Python standard library
with open('service-policy.json', 'w') as opened_file:
    policy = json.dump(policy, opened_file)

with open('verify-apache.yml', 'r') as opened_file:
    verify_apache = yaml.safe_load(opened_file)
pprint(verify_apache)
for value in verify_apache:
    for key in value:
        if key == 'hosts':
            value['hosts'] = 'db-server'

with open('verify-apache.yml', 'w') as opened_file:
    yaml.dump(verify_apache, opened_file)

# csv
with open('addresses.csv', newline='') as csv_file:
    off_reader = csv.reader(csv_file, delimiter=',')
    for _ in range(5):
        print(next(off_reader))