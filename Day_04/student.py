class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_highest(self):
        if len(self.grades) == 0:
            return None
        return max(self.grades)

    def get_lowest(self):
        if len(self.grades) == 0:
            return None
        return min(self.grades)


# Example usage
student1 = Student("Lakshaya")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

print("Name:", student1.name)
print("Grades:", student1.grades)
print("Average:", student1.get_average())
print("Highest Grade:", student1.get_highest())
print("Lowest Grade:", student1.get_lowest())
