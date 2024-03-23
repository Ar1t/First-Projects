dollars = 8
dollars == 8.0


total = 0
grade_count = 0
grade1=int(input('enter grade'))
grade2=int(input('enter grade'))
if grade1 >= 50 :
    total = total + grade1
    grade_count = grade_count + 1
elif grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1
if grade_count > 0:
    print(total/grade_count)
else:
    print(0.0)