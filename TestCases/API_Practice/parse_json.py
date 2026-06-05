import json

emp_data='{"employee": {"id": 101,"name": "Pavan","department": "IT","skills": ["Python", "Git", "SQL"]}}'
#Loads method parse json string and it returns dictionary
dict_conv= json.loads(emp_data)

print(type(dict_conv))
print(dict_conv['employee']['name'])

skills = dict_conv['employee']['skills']
print(type(skills))
print(skills)