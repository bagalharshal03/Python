student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
sem_no = input("Enter Your Semister: ")
branch_no = input("Enter Your Branch: ")

print("Enter marks obtained (out of 100):")
math_marks = float(input("Environmental: "))
physics_marks = float(input("Java: "))
english_marks = float(input("DCN: "))
chemistry_marks = float(input("MIC: "))
biology_marks = float(input("Python: "))
design_marks = float(input("UI/UX Design: "))

total_obtained = math_marks + physics_marks + english_marks + chemistry_marks + biology_marks
percentage = (total_obtained / 400) * 100

print("===========================================")
print("            STUDENT MARKSHEET          ")
print("===========================================")
print("Student Name :", student_name)
print("Roll Number :", roll_number)
print("Semister :", sem_no)
print("Branch :", branch_no)
print("-------------------------------------------")
print("Subject     | Marks Obtained")
print("-------------------------------------------")
print("Environmental |", math_marks)
print("Java          |", physics_marks)
print("DCN           |", english_marks)
print("MIC           |", chemistry_marks)
print("Python        |", biology_marks)
print("UI/UX Design  |", design_marks)
print("-------------------------------------------")
print("Total Score |", total_obtained, "out of 400")
print("Percentage  |", percentage)
print("===========================================")


