# 81. 42.	Write a Python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
''' Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F '''

Physics=int(input("Enter marks of Physics: "))
Chemistry=int(input("Enter marks of Chemistry: "))
Biology=int(input("Enter marks of Biology: "))
Mathematics=int(input("Enter marks of Mathematics: "))
Computer=int(input("Enter marks of Computer: "))

total=Physics+Chemistry+Biology+Mathematics+Computer
percentage=(total/500)*100

if(percentage>=90):
    print("Grade A")
elif(percentage>=80):
    print("Grade B")
elif(percentage>70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
elif(percentage>=40):
    print("Grade E")
else:
    print("Grade F")
