name , age, city, company, salary = "Shivendra", 22, "Raebareli", "Contify", 30000
print(f"My name is {name}, i am {age} years old, i am from {city},working at {company}, at salary of {salary} per month")

None_Type= None
check=True
print(f"{name} is a {type(name)}")
print(f"{age} is a {type(age)}")
print(f"{check} is a {type(check)}")
print(f"{None_Type} is a {type(None_Type)}")

a=int(input("Enter a number: "))
b=int(input("Enter a another number: "))

c=input("Enter +, -, *, /. %, //, ** :")
if(c=="+"):
    print(f"{a}+{b} = {a+b}")
elif(c=="-"):
    print(f"{a}-{b} = {a-b}")
elif(c=="*"):
    print(f"{a}*{b} = {a*b}")
elif(c=="/"):
    print(f"{a}/{b}= {a/b}")
elif(c=="%"):
    print(f"{a}%{b} = {a%b}")
elif(c=="//"):
    print(f"{a}//{b} = {a//b}")
elif(c=="**"):
    print(f"{a}**{b}= {a**b}")
else:
    print("Invalid operator")

age=int(input("Enter your age: "))
print(f"current age is {age} and after 5 year it will be {age+5}")

print(f"value of a before swapping a = {a} & b = {b}")
a,b=b,a
print(f"value of a after swapping a = {a} & b = {b}")



'''Employee profile'''
name=input("Enter your name: ")
emp_id= int(input("Enter your employee id: "))
salary= int(input("Enter your salary: "))
dep= input("Enter your department: ")
print("Welcome to the company")
print(f"Employee name : {name}\nEmployee id: {emp_id}\nEmployee salary: {salary}\nEmployee department: {dep}")

product= input("Enter product name: ")
price= int(input("Enter product price: "))
qty= int(input("Enter product quantity: "))
total= price*qty
print(f"\n INVOICE\n Product name: {product}\n Product price: {price}\n Product quantity: {qty}\n Total amount: {total}")
