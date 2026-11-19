# ---------------------------------------------------------
# 1. Variables and f-string
# ---------------------------------------------------------

# Creating multiple variables in one line
name, age, city, company, salary = "Shivendra", 22, "Raebareli", "Contify", 30000

# Using f-string to print variable values inside a sentence
print(f"My name is {name}, i am {age} years old, i am from {city},working at {company}, at salary of {salary} per month")


# ---------------------------------------------------------
# 2. Data types
# ---------------------------------------------------------

None_Type = None     # Assigning None to a variable
check = True         # Storing a boolean value

# Checking the data type of different variables using type()
print(f"{name} is a {type(name)}")            # Checking string type
print(f"{age} is a {type(age)}")              # Checking integer type
print(f"{check} is a {type(check)}")          # Checking boolean type
print(f"{None_Type} is a {type(None_Type)}")  # Checking NoneType


# ---------------------------------------------------------
# 3. Calculator using if / elif / else
# ---------------------------------------------------------

# Taking two numbers from the user
# Converting input into int because input() normally returns a string
a = int(input("Enter a number: "))
b = int(input("Enter a another number: "))

# Taking the operator from the user
c = input("Enter +, -, *, /. %, //, ** :")

# Using if-elif to check which operator the user has entered
if(c == "+"):
    print(f"{a}+{b} = {a+b}")        # Adding both numbers
elif(c == "-"):
    print(f"{a}-{b} = {a-b}")        # Subtracting the numbers
elif(c == "*"):
    print(f"{a}*{b} = {a*b}")        # Multiplying both numbers
elif(c == "/"):
    print(f"{a}/{b}= {a/b}")         # Dividing both numbers
elif(c == "%"):
    print(f"{a}%{b} = {a%b}")        # Getting the remainder
elif(c == "//"):
    print(f"{a}//{b} = {a//b}")      # Getting the quotient without decimal
elif(c == "**"):
    print(f"{a}**{b}= {a**b}")       # Calculating power of a number
else:
    # This block runs when none of the above conditions match
    print("Invalid operator")


# ---------------------------------------------------------
# 4. Age after 5 years
# ---------------------------------------------------------

# Asking the user to enter their current age
age = int(input("Enter your age: "))

# Adding 5 to the current age and printing the result
print(f"current age is {age} and after 5 year it will be {age+5}")


# ---------------------------------------------------------
# 5. Swapping two variables
# ---------------------------------------------------------

# Printing the values before swapping
print(f"value of a before swapping a = {a} & b = {b}")

# Swapping the values of a and b using Python's multiple assignment
a, b = b, a

# Printing the values after swapping
print(f"value of a after swapping a = {a} & b = {b}")


# ---------------------------------------------------------
# 6. Employee profile
# ---------------------------------------------------------

'''Employee profile'''

# Taking employee details as input from the user
name = input("Enter your name: ")
emp_id = int(input("Enter your employee id: "))
salary = int(input("Enter your salary: "))
dep = input("Enter your department: ")

print("Welcome to the company")

# Using \n to print each employee detail on a separate line
print(f"Employee name : {name}\nEmployee id: {emp_id}\nEmployee salary: {salary}\nEmployee department: {dep}")


# ---------------------------------------------------------
# 7. Invoice
# ---------------------------------------------------------

# Taking product details from the user
product = input("Enter product name: ")
price = int(input("Enter product price: "))
qty = int(input("Enter product quantity: "))

# Calculating the total amount using price and quantity
total = price * qty

# Printing all product details along with the final bill amount
print(f"\n INVOICE\n Product name: {product}\n Product price: {price}\n Product quantity: {qty}\n Total amount: {total}")
