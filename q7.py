class Student:
    pass

class Marks:
    pass

# Instance of Student
std1 = Student()

# Instance of Marks
mrk1 = Marks()

# Check if std1 is instance of Student
print(isinstance(std1, Student))

# Check if mrk1 is instance of Marks
print(isinstance(mrk1, Marks))

# Check if Student is subclass of object
print(issubclass(Student, object))

# Check if Marks is subclass of object
print(issubclass(Marks, object))

# Output
# True
# True
# True
# True
