"""
Given the pre-defined variables first_name and last_name, write an assignment statement that
defines the variable name_tag whose value is the string "My name is % %." where the percents should be
replaced by first_name and last_name. Note that, in Python, you can use the + operator
on strings to concatenate (i.e. join) them together into a single string
"""

# Compute a name tag, given the first and last name.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
first_name = "Joe"
last_name = "Warren"


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#first_name = "Scott"
#last_name = "Rixner"


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#first_name = "John"
#last_name = "Greiner"


###################################################
# Name tag formula
# Student should enter formula on the next line.

name_tag = "My name is " + first_name + " " + last_name + "."

###################################################
# Test output
# Student should not change this code.

print name_tag


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#My name is Joe Warren.

# Test 2 output:
#My name is Scott Rixner.

# Test 3 output:
#My name is John Greiner.
