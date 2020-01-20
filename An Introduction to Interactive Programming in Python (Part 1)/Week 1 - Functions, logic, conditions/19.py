"""
Write a Python function name_and_age that take as input the parameters name (a string) and age (a number)
and returns a string of the form "% is % years old." where the percents are the string forms of
name and age. The function should include an error check for the case when age is less than zero.
In this case, the function should return the string "Error: Invalid age".
"""


# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    """
    Returns name and age string and checks for age less than zero
    """

    if age >= 0:
        return name + " is " + str(age) + " years old."
    else:
        return "Error: Invalid age"

###################################################
# Tests
# Student should not change this code.

def test(name, age):
    """Tests the name_and_age function."""

    print name_and_age(name, age)


test("Joe Warren", 52)
test("Scott Rixner", 40)
test("John Greiner", -46)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Joe Warren is 52 years old.
# Scott Rixner is 40 years old.
# Error: Invalid age
