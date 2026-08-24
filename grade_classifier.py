full_name = input("Enter your name and surname: ").strip()

mark1 = float(input("Enter your mark for subject 1: "))
mark2 = float(input("Enter your mark for subject 2: "))
mark3 = float(input("Enter your mark for subject 3: "))

average_mark = (mark1 + mark2 + mark3) /3

if average_mark >=80:
    letter_grade = "A"
    status = "Pass"
elif average_mark >=70 and average_mark <=79:
    letter_grade = "B"
    status = "Pass"
elif average_mark >=60 and average_mark <=69:
    letter_grade = "C"
    status = "Pass"
elif average_mark >=50 and average_mark <=59:
    letter_grade = "D"
    status = "Pass"
else:
    letter_grade = "F"
    status = "Fail"

if mark1 <40:
    flag = "Subject 1 Needs intervention!"
elif mark2<40:
    flag = "Subject 2 Needs intervention!"
elif mark3<40:
    flag = "Subject 3 Needs intervention!"
else:
    flag = "No attention needed"

print(f"\nReport Card for: {full_name}")    
print("===================================")
print(f"Subject 1: {round(mark1, 2)}")
print(f"Subject 2: {round(mark2, 2)}")
print(f"Subject 3: {round(mark3, 2)}")
print("===================================")
print (f"Average Mark: {round(average_mark, 2)}")
print(f"Grade Symbol: {letter_grade}")
print(f"Pass/Fail: {status}")
print(f"Intervention: {flag}")