"""
Write a Python function triangle_area that takes the parameters x0, y0, x1, y1, x2, and y2, and returns
the area of the triangle with vertices (x0,y0), (x1,y1) and (x2,y2). (Hint: use the function
point_distance as a helper function and apply Heron's formula.)
"""

# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Triangle area (Heron's) formula
# Student should enter function on the next lines.
# Hint:  Also define point_distance as use it as a helper function.

def point_distance(x0, y0, x1, y1):
    """Return the distance between tow points given their vertices"""

    return (((x0 - x1) ** 2) + ((y0 - y1) ** 2)) ** 0.5


def triangle_area(x0, y0, x1, y1, x2, y2):
    """Return the rectangle area given its vertices"""

    # Compute the langths of the triangle three sides
    side1 = point_distance(x0, y0, x1, y1)
    side2 = point_distance(x2, y2, x1, y1)
    side3 = point_distance(x0, y0, x2, y2)

    # Using Heron's formula
    # Compute the semi-perimeter of the triangle
    s = (side1 + side2 + side3) / 2.0
    # Compute the triangle area
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

    return area


###################################################
# Tests
# Student should not change this code.

def test(x0, y0, x1, y1, x2, y2):
	print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
	print "(" + str(x1) + "," + str(y1) + "), and",
	print "(" + str(x2) + "," + str(y2) + ") has an area of",
	print str(triangle_area(x0, y0, x1, y1, x2, y2)) + "."

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
