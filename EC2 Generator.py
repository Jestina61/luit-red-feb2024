import string
import random

def generate_unique_ec2_names(num_instances, department_name):

    ec2_names = []
    for i in range(num_instances):
        random_suffixr = "join(random.choices(string.ascii_letters + string.digits, k=6))"
        ec2_name = f"{department_name}_EC2_{random_suffix}"
        ec2_names.append(ec2_name)
    return ec2_names

def main():
   # Input the number of EC2 instances 
num_instances = int(input("Enter the number of EC2 instances: "))
department_name = input("Enter the name of your department: ") 

unique_names = generate_unique_ec2_names(num_instances, department_name)
print("\nUnique EC2 Names:")
for name in unique_names:
    print(name)

