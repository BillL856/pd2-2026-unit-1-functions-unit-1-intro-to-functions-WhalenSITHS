""" #strings represent characters or text
x = "dang it Yi"
#inputs output strings
name = input("What's your name")
print(name)

def add(x,y):
    return x + y
z = add(5,15)
print(z)

#integers or numbers
a = int('5') 
bill = input("How much was the bill?")
print(int(bill) * .15) 

name = "Mason"
#use f string
print(f"His name is {name}") 

#Floot
#bill = 3.14  """

""" students = ["Cadee", "Mason", "Andy"]
#lists are a collection of data
#Can reference each item in a list by their index
print(students[0]) #Prints Cadee

# add student
students.append("Alina")

# we can iterate or loop through a list
for student in students:
    print(student) """

""" #Boolean true or false """
""" x= True
y= False
#evaluations use double ==
if y == True:
    print("Rodney") """

""" #Evaluations in lists
students = ["Cadee", "Mason", "Andy", "Alina"]
if "Alina" in students:
    print("Shes here")
else:
    students.append("Alina")
    print("We added Alina") """

""" x= 91
if x< 10:
    print("Less")
elif x ==10:
    print("Equal")
else:
    print("Greater")
 """

""" students = ["Cadee", "Mason", "Andy", "Alina"]
for student in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True """

""" name = "Cadee"
#print(name[0])
for letter in name:
    print(letter) """