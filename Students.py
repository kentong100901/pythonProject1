import unittest

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if not isinstance(lname, str):
            raise ValueError("Last name must be a string")
        if not isinstance(fname, str):
            raise ValueError("First name must be a string")
        if not isinstance(major, str):
            raise ValueError("Major must be a string")
        if not isinstance(gpa, float) or not (0.0 <= gpa <= 4.0):
            raise ValueError("GPA must be a float between 0.0 and 4.0")

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

class TestStudent(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_object_created_required_attributes(self):
        student = Student("Tan", "Li Ming", "Computer Science")
        self.assertEqual(student.last_name, "Tan")
        self.assertEqual(student.first_name, "Li Ming")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        student = Student("Kawasaki", "Yuki", "Physics", 3.5)
        self.assertEqual(student.last_name, "Kawasaki")
        self.assertEqual(student.first_name, "Yuki")
        self.assertEqual(student.major, "Physics")
        self.assertEqual(student.gpa, 3.5)

    def test_student_str(self):
        student = Student("Tanaka", "Aiko", "Biology", 3.2)
        self.assertEqual(str(student), "Tanaka, Aiko has major Biology with gpa: 3.2")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            Student(123, "John", "Chemistry")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            Student("Doe", 123, "Math")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            Student("Doe", "John", 123)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            Student("Doe", "John", "History", 4.5)

def main():
    student1 = Student("Kim", "Soo Jin", "Computer Science")
    student2 = Student("Ken", "TU", "Mathematics", 3.9)
    print(student1)
    print(student2)

if __name__ == '__main__':
    unittest.main()

# To create the students and print them:
main()
