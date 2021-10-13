
"""
Created on Wed Oct  6 19:15:51 2021

@author: zakria
"""

#student details
student={
    'name':'Zakria Rehman',
    'session': 2018,
    'semester': 7,
    'reg_Number':"18-SE-30",
    }

#subject details
subjects=(
    'SPM','ST', 'ML', 'VL', 'HRM'
    )

#departments of UET Taxila
departments= {'Software', 'Computer', 'Mechanical', 'Civil', 'Electrical', 'Industrial'}


#declaring a grade calculator

#as definition is not equired,but definition is as follows
def compute_grade(weightage):
    grade= None
    if (weightage >= 80):
        grade="A"
    elif (weightage >= 70):
        grade= "B"
    elif (weightage >= 60):
        grade= "C"
    elif (weightage>=50):
        grade= "D"
    else:
        grade= "F"
    
    return grade
marks= int(input("Enter Your Marks: "))
grade= compute_grade(marks)
print("Your Calculated Grade is: ", grade)

#

#loop for displaying subjects
print("Student Details:\n")
for subject in subjects:
    print(subject)

print("Departments of UET Taxila:\n")
for department in departments:
    print(department)

#loop for displaying students

    
#displaying keys
print(student.keys())

#displaying values
print(student.values())
print()
    