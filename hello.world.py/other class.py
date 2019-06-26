
import random

name=input("Enter your name:")
salary=input("Salary:")
raise_per=random.randint(0,100)
raise_amount=(int(salary)/raise_per)+int(salary)
print(f"{salary} {raise_amount}")
