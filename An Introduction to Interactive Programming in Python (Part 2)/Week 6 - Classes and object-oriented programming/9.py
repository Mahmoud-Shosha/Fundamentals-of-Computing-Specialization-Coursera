"""
Before proceeding to the task of implementing Memory using the Tile class that we developed in Week 6a, your job is to
complete couple of pairs of exercises in which we implement and then use some simple classes. As your first task,
implement a Person class which has the fields first_name, last_name and birth_year. This class should include
the methods: __init__ which takes strings for the two name fields and an integer for the year of birth, full_name
returns the full name for a person as a string, which is the first name followed by a space, followed by the last name,
age which takes the current year as input and returns the age in years of the person (Don't worry about days and months
here, just return the difference of the two years.), and __str__ returns a string that includes the first name and
last name of the person as well as their year of birth.
"""


# Implementation of Person class


#################################################
# Student adds code where appropriate

# definition of Person class
class Person:

    def __init__(self, first, last, year):
        self.first = first
        self.last = last
        self.year = year

    def full_name(self):
        return self.first + " " + self.last

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return "The person's name is " + self.full_name() + ". Their birth year is " + str(self.year)


###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)

print joe
print john
print stephen
print scott

print joe.age(2013)
print scott.age(2013)  # yeah, right ;)
print john.full_name()
print stephen.full_name()

####################################################
# Output of testing code - results of __str__ method may vary

# The person's name is Joe Warren. Their birth year is 1961
# The person's name is John Greiner. Their birth year is 1966
# The person's name is Stephen Wong. Their birth year is 1960
# The person's name is Scott Rixner. Their birth year is 1987
# 52
# 26
# John Greiner
# Stephen Wong