"""
Tests for the Yahtzee game
"""

from poc_simpletest import TestSuite

from mini_project import


def test_score():
    """
    Tests for the function score()
    """
    print("Tests for 'score' function")
    test_suite = TestSuite()

    # Testing with empty hand
    result = score([])
    test_suite.run_test(result, 0, '0')
    # Testing with non-empty hand
    result = score([1, 3])
    test_suite.run_test(result, 3, '1')
    # Testing with non-empty hand
    result = score([1, 3, 1, 1])
    test_suite.run_test(result, 3, '2')
    # Testing with non-empty hand
    result = score([4, 3, 4, 3, 3])
    test_suite.run_test(result, 9, '3')

    # Show report
    test_suite.report_results()





# Running tests
test_score()
print()

