import datetime

class Ward:
    def __init__(self, name:str, mem_list:list=None):
        self.name = name
        self.mem_list = mem_list if mem_list else []
    
    def add_person(self, person):
      if(isinstance(person, Person) == True):
        self.mem_list.append(person)
        return True
      return False

    def describe(self):
        print(f"Ward: {self.name}")
        for mem in self.mem_list:
            mem.describe()
            print("-"*60)
    def count_doctor(self):
        count = 0
        for mem in self.mem_list:
            if isinstance(mem, Doctor):
                count += 1
        return count
    
    def sort_age(self):
      year = datetime.date.today().year
      self.mem_list.sort(key=lambda x: year-x.yob)
        
    
    def compute_avg(self):
      avg = 0
      count = 0
      for t in self.mem_list:
        if(isinstance(t, Teacher) == True):
          avg += t.yob
          count += 1
      return avg/count
    
class Person:
    def __init__(self, name:str, yob:int):
        self.name = name
        self.yob = yob
    
    def describe(self):
        print(f"Person - Name: {self.name} _ YoB: {self.yob}")

class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student - Name: {self.name} _ YoB: {self.yob} _ Grade: {self.grade}")
        
class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} _ YoB: {self.yob} _ Subject: {self.subject}")
        
class Doctor(Person):
    def __init__(self, name:str, yob:int, specialty:str):
        super().__init__(name, yob)
        self.specialty = specialty
        
    def describe(self):
        print(f"Doctor - Name: {self.name} _ YoB: {self.yob} _ Specialty: {self.specialty}")


# Run Program
ward_1 = Ward("Ward 1")
student_1 = Student("Student 1", 2000, "A")
student_1.describe()
print("-"*60)

teacher_1 = Teacher("Teacher 1", 1980, "Math")
teacher_1.describe()
print("-"*60)

doctor_1 = Doctor("Doctor 1", 1970, "Cardiology")
doctor_1.describe()
print("-"*60)

print(end="\n\n")
teacher_2 = Teacher("Teacher 2", 1985, "Science")
doctor_2 = Doctor("Doctor 2", 1980, "Neurology")

ward_1.add_person(student_1)
ward_1.add_person(teacher_1)
ward_1.add_person(doctor_1)
ward_1.add_person(teacher_2)
ward_1.add_person(doctor_2)

ward_1.describe()

print(end="\n\n")

print(f"Number of Doctors: {ward_1.count_doctor()}")
print(end="\n\n")

print("After sort by Age")
ward_1.sort_age()
ward_1.describe()
print(end="\n\n")

print(f"Average YoB of Teachers: {ward_1.compute_avg()}")