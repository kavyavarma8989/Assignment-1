
# Online Python - IDE, Editor, Compiler, Interpreter
#---------------Question1-----------------

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sorting the list
ages.sort() #sorting
print(ages)
l=len(ages)  #length
minimum=ages[0] # minimum age 
maximum=ages[l-1]# maximum age 
print("Min age:" ,minimum, "and Max age:",  maximum)
ages.append(ages[0])# appending minimum age
ages.append(ages[l-1])#appending maximum age
print(ages)
#Finding the median 
l=(len(ages)-1)//2 #calculated the index value
if((len(ages))%2!=0):  # odd
    median=ages[l]
    print("Median is :",median)
else:      # even
    median=(ages[l]+ages[l+1])/2 #average
    print("Median is :",median)
#Finding average
sum=0
for i in ages:  #all the i values
    sum=sum+i
print("Average is :",sum//len(ages))
#Range of ages 
ages.sort()
range=ages[len(ages)-1]-ages[0]
print("Range is:", range)

#-------------Question2--------------------

dog = dict () # empty dictonary for dog is created
#Added features to the dog
dog["name"] = "rocky",
dog["color"] = "white",
dog["breed"] = "husky",
dog["legs"] = "4",
dog["age"] = "5",
student = {   #creating a student dictonary
# added keys and values to the student
"first_name" : "Srikavya",
    "last_name" : "Gottumukkala",
    "gender" : "female",
    "age" : "21",
    "marital status": "single",
    "skills" : ["dancing","reading"],
    "country": "India",
    "city" : "vizag",
    "address" : "6808 w 141st ter apt 3201",
}
print(len(student))
x = student.get("skills") 
print(x)
print(type(x))
student['skills']+=['drawing'] 
print(student)
print(list(student.keys())) 
print(list(student.values()))

#------------Question 3-----------

Sisters=('Sravani','Geethika','Lakshmi','Deethya') #sisters tuple is created
Brothers=('Abhi','Anil','Aarush') #brothers tuple is created
Siblings=Sisters+Brothers
print(Siblings)
print("I have",len(Siblings),"Siblings")
fml=list(Siblings) #converting tuple to list
fml.append('Vanaja')
fml.append('Kartik')
family_members=tuple(fml)
print(family_members)

#--------------Question 4----------------

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("The length is:",len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Capgemini','Wipro','TCS']) #adding to the list 
print(it_companies)
it_companies.remove('IBM') #removing from list
print(it_companies)

C = A.union(B) #joining A and B
print(C)
A.intersection_update(B) # A intersection B
print(A)
print(A.issubset(B)) #A is subset of B
print(A.isdisjoint(B)) #A and B are not disjoint sets
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B)) 
del A #A set is deleted
del B #B set is deleted
print(len(age)) #length of the list
s= set(age) 
print(s)
print(len(s))

#-----------------Question5------------------

radius=30
_area_of_circle_= 3.14*(radius**2)
print("Area :",_area_of_circle_)
_circum_of_circle_= 2 * 3.14 * radius
print("Circumference:",_circum_of_circle_)
print("Enter the radius value:")
r=int(input())
area=3.14 * (r**2)
print("Area:",area)

#-----------------Question 6------------------------

text="I am a teacher and I love to inspire and teach people"
text=text.split()
set_text=set(text)
print("The count of unique words is:",len(set_text))

#-----------------Question 7---------------------

print("Name     Age  Country     City\nAsabench  250  Finland  Helsinki")

#------------------Question8--------------------

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square."%(radius,area))




