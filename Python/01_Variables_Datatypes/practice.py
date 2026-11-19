```python
# PYTHON PRACTICE CODE (WITH COMMENTS)
# Topics: variables, data types, input, operators, if/elif/else, swapping

# storing all details in variables in one line
name, age, city, company, salary = "Shivendra", 22, "Raebareli", "Contify", 30000

# printing details using f string
print(f"My name is {name}, i am {age} years old, i am from {city},working at {company}, at salary of {salary} per month")


None_Type = None     # storing None value
check = True         # storing True in a boolean variable

# checking the data type of variables using type()
print(f"{name} is a {type(name)}")            # str
print(f"{age} is a {type(age)}")              # int
print(f"{check} is a {type(check)}")          # bool
print(f"{None_Type} is a {type(None_Type)}")  # NoneType


# taking two numbers from the user and converting them into int
a = int(input("Enter a number: "))
b = int(input("Enter a another number: "))

# taking the operator as input
c = input("Enter +, -, *, /. %, //, ** :")

# checking which operator the user has entered
if(c == "+"):
    print(f"{a}+{b} = {a+b}")        # addition
elif(c == "-"):
    print(f"{a}-{b} = {a-b}")        # subtraction
elif(c == "*"):
    print(f"{a}*{b} = {a*b}")        # multiplication
elif(c == "/"):
    print(f"{a}/{b}= {a/b}")         # normal division
elif(c == "%"):
    print(f"{a}%{b} = {a%b}")        # finding remainder
elif(c == "//"):
    print(f"{a}//{b} = {a//b}")      # division without decimal
elif(c == "**"):
    print(f"{a}**{b}= {a**b}")       # calculating power
else:
    # if user enters any other operator
    print("Invalid operator")


# taking current age from the user
age = int(input("Enter your age: "))

# adding 5 years to the current age
print(f"current age is {age} and after 5 year it will be {age+5}")


# printing values before swapping
print(f"value of a before swapping a = {a} & b = {b}")

# swapping values of a and b in one line
a, b = b, a

# printing values after swapping
print(f"value of a after swapping a = {a} & b = {b}")


'''Employee profile'''

# taking employee details from the user
name = input("Enter your name: ")
emp_id = int(input("Enter your employee id: "))
salary = int(input("Enter your salary: "))
dep = input("Enter your department: ")

print("Welcome to the company")

# printing all employee details using \n to move to the next line
print(f"Employee name : {name}\nEmployee id: {emp_id}\nEmployee salary: {salary}\nEmployee department: {dep}")


# taking product details from the user
product = input("Enter product name: ")
price = int(input("Enter product price: "))
qty = int(input("Enter product quantity: "))

# calculating total amount by multiplying price and quantity
total = price * qty

# printing the final invoice
print(f"\n INVOICE\n Product name: {product}\n Product price: {price}\n Product quantity: {qty}\n Total amount: {total}")
```
