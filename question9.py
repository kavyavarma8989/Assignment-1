
# Online Python - IDE, Editor, Compiler, Interpreter
Students_num = int(input(" enter number of students in a class"))
print("Total number of students  is", Students_num)
Student_wt = []
for i in range(0,Students_num):
     Student_wt.append(int(input('enter the weight')))
print("Weights in lbs :", Student_wt)   
Student_kgs = []
for i in range(0,Students_num):
    Student_kgs.append(Student_wt[i]*0.453592)
print('Weights in kgs:',Student_kgs)
