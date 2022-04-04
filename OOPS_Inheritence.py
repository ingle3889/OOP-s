class Student: 
    #Class Attribute species = 'humans' 
    # Initializer / Object Attributes 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        print("Student's name is " + name + " and age is " + str(age)) 
    def grade(self, grades): 
        self.grades = grades 
        print("The grade of student is: " + grades) 
class Girl(Student): 
    def __init__(self, name, age): 
        super().__init__(name, age) 
        print("Girl class is ready") 
    
    def whichclass(self): 
        print("This is Girls class which is a child class of Student class.") 
stu1 = Student("John", 16)
stu1.grade("A+") 
stu2 = Student("Smith", 24) 
stu2.grade("B") 
print("\n") 
girl1 = Girl("Anna", 21) 
girl1.whichclass() 
girl1.grade("B")
