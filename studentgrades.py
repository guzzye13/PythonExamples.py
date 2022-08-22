#Python program to find student grade
english = float(input("Please enter english marks: "))
math = float(input("Please enter Math score: "))
chemistry = float(input("Pleasse enter Chemistry score: "))
total = english + math + chemistry
percentage = (total / 300) * 100
print("Total Marks = %.2f" %total)
print("Marks percentage = %.2f" %percentage)

if(percentage >= 90):
    print("Grade = A")
elif(percentage >= 80):
    print("Grade = B")
elif(percentage >= 70):
    print("Grade = C")
elif(percentage >= 60):
    print("Grade = D")
elif(percentage >= 40):
    print("Grade = E")
else:
    print("Fail")

