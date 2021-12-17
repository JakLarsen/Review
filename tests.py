


            #SIMPLE



# #Should throw: 
# #   AssertionError: Should be 6.
# assert sum([1,2,3]) == 4, "Should be 6."



            # STILL SIMPLE



# def test_sum():
#     assert sum([1,2,3]) == 6, "Should be 6."
#     # assert sum([1,2,3]) == 4, "Should be 6."
# def test_sum_tuple():
#     assert sum((1,2,3)) == 6, "Should be 6."
#     # assert sum((1,2,3)) == 4, "Should be 6."

# if __name__ == "__main__":

#     test_sum()
#     test_sum_tuple()

#     print('All tests passed')



            #BASIC DOCTESTS



from doctest import testmod

def factorial(n):
    """
    Recursive Factorial

    >>> factorial(3)
    6
    >>> factorial(4)
    120
    
    """
    return 1 if n <= 1 else n * factorial(n-1)

testmod()


            #UNITTEST - Built-in python test-runner



# import unittest
# from unittest import TestCase



# class TestSum(TestCase):

#     def test_sum(self):
#         """Test the sum() function with lists"""
#         self.assertEqual(sum([1,2,3]), 6, "Should be 6")
    
#     #This one will fail
#     def test_sum_tuple(self):
#         """Test the sum() function with tuples"""
#         self.assertEqual(sum((1,2,2)), 6, "Should be 5")
#         self.assertEqual(sum((1,2,2)), 5, "Should be 5")


# if __name__ == '__main__':
#     unittest.main()

# #Can also call python -m unittest tests from the cmdline