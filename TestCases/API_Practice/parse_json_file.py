import json

with open('C:\\Users\\45680\\Documents\\Sales_Tech_sample\\TestCases\\Data\\emp_data.json') as f1:
    dict_data= json.load(f1)
    #print(dict_data)
    #print(type(dict_data))
    #Print the company Name as below
    #print(dict_data['company']['name'])
    count=0
    high_paid_emp=[]
    python_skilled_emps=[]
    total_emp=0
    for dept in dict_data['company']['departments']:
        #print(dept['name'])
        count+=1
        for emp in dept['employees']:
            print(emp['name'], "-", dept['name'])
            if emp['salary'] > 500000:
                high_paid_emp.append(emp['name'])
            if 'Python' in emp['skills']:
                python_skilled_emps.append(emp['name'])
            total_emp+=1
                 
                
    
print("Total Departments:", count)
print("Total Employees:", total_emp)
print("High Paid Employees:", high_paid_emp)
print("Python Skilled Employees:", python_skilled_emps)
