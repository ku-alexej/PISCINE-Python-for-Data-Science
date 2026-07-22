from new_student import Student

try:
    student = Student(name="Edward", surname="agle")
    print(student)
except Exception as e:
    print(f"Error: {e}")

try:
    student = Student(name="Edward", surname="agle", active=False)
    print(student)
except Exception as e:
    print(f"Error: {e}")

try:
    student = Student(name="Edward")
    print(student)
except Exception as e:
    print(f"Error: {e}")


try:
    student = Student(name="Edward", surname="agle", id="custom_id_123")
    print(student)
except Exception as e:
    print(f"Error: {e}")

try:
    student = Student(name="Edward", surname="agle", login="custom_login")
    print(student)
except Exception as e:
    print(f"Error: {e}")

try:
    student = Student(name="Edward", surname="agle", wrong_param="unexpected")
    print(student)
except Exception as e:
    print(f"Error: {e}")
