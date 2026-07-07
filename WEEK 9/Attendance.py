def log_attendance(name, roll_number, status):
    return f"Roll No: {roll_number} | Name: {name} -> {status}"

print("--- Attendance System Assignment ---")

students = ["Alex", "Emma", "Ryan"]
attendance_status = ["Present", "Absent", "Present"]

for index in range(len(students)):
    
    record = log_attendance(students[index], index + 1, attendance_status[index])
    print(record)