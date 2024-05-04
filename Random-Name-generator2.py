import string
import random

def generate_unique_ec2_names(num_instances, department_name):
  
    unique_names = []
    for i in range(num_instances):
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        unique_name = f"{department_name}-ec2-{i+1}-{random_str}"
        unique_names.append(unique_name)
    return unique_names

num_instances = int(input("Enter the number of EC2 instances you want names for: "))
department_name = input("Enter the name of your department: ").lower()

unique_names = generate_unique_ec2_names(num_instances, department_name)
for name in unique_names:
    print(name)
    
    
