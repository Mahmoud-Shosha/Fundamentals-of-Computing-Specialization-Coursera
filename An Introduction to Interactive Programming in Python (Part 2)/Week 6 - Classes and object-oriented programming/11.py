"""
Implement a Student class which has the fields person (Person object), password (string), and projects
(list of strings). (Note that class uses another class, just as in Blackjack.) This class should include the following
methods:, __init__ which takes a person (specified as Person object) and a password (specified as a string) and creates
a Student object (the list of projects should be empty to start), get_name which returns the student's full name,
check_password which take a supplied password and returns a Boolean indicating whether the supplied password matches
the student's created password, get_projects which returns the list of the student's projects and,
add_project(project_name) which adds the specified project to the student's list of projects. Note that this last
method does not check whether the project already exists in the list.
"""


# Implementation of Student class

# definition of Person class
class Person:

    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year

    def full_name(self):
        return self.first_name + " " + self.last_name

    def age(self, current_year):
        return current_year - self.birth_year

    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.birth_year)


#################################################
# Student adds code where appropriate

# definition of Student class
class Student:

    # the person parameter must be a Person object
    def __init__(self, person, pwd):
        self.person = person
        self.password = pwd
        self.projects = []

    # use the full_name method for Person
    def get_name(self):
        return self.person.full_name()

    def check_password(self, pwd):
        return pwd == self.password

    def get_projects(self):
        return self.projects

    def add_project(self, project):
        self.projects.append(project)


###################################################
# Testing code

joe_person = Person("Joe", "Warren", 52)
joe_student = Student(joe_person, "TopSecret")

print joe_student.get_name()
print joe_student.check_password("qwert")
print joe_student.check_password("TopSecret")

print joe_student.get_projects()
joe_student.add_project("Create practice exercises")
print joe_student.get_projects()
joe_student.add_project("Implement Minecraft")
print joe_student.get_projects()

####################################################
# Output of testing code

# Joe Warren
# False
# True
# []
# ['Create practice exercises']
# ['Create practice exercises', 'Implement Minecraft']


