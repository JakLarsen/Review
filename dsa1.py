




                    # 12/16




#LL STACK INSERT AND POP TAIL (OR HEAD - PICK)

class Node:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__ (self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def traverse(self):
        if self.head == None:
            print('Nothing in LL.')
        else:
            currentNode = self.head
            while currentNode:
                print(currentNode.val, currentNode)
                currentNode = currentNode.next
    
    def LL_peak_tail(self):
        print(f'Tail is: {self.tail}, {self.tail.val}')

    def LL_append(self, Node):
        if self.head == None:
            self.head = Node
            self.tail = Node
        else:
            self.tail.next = Node
            self.tail = Node

    def LL_pop(self):
        second_to_last = self.head

        #0 Nodes
        if self.head == None:
            return None
        #1 Node
        elif self.head.next == None:
            return self.head.val
        #2 + Nodes
        else:
            return

    
our_LL = LinkedList()
a_Node = Node('a')
b_Node = Node('b')
c_Node = Node('c')
our_LL.traverse()
our_LL.LL_append(a_Node)
our_LL.traverse()
our_LL.LL_append(b_Node)
our_LL.LL_append(c_Node)
our_LL.traverse()
our_LL.LL_peak_tail()
our_LL.LL_pop()
our_LL.traverse()
our_LL.LL_peak_tail()








# #Given a string sequence of brackets, return True if all bracket pairs surround closed pairs of brackets 
# # E.G. {[()]} is True but {([)]} is False
# # E.G. {}()[] is True but {)} is False

# # RUNDOWN
#     # We set up a dict of matching brackets with key left value right
#     # We have a list to hold left side brackets
#     # Each right side bracket we try to match against it's left side pair and if match, remove that from list
#     # If not match, return False
#     # If list not empty at end, return False
#     # If list empty at end, return True

# bracket_list1 = ['{','[','(',')',']','}']
# bracket_list2 = [']','{','[','(',')',']','}']
# bracket_list3 = ['{','[','(',')',']','}','[']
# bracket_list4 = ['[']
# bracket_list5 = ['[',']']
# bracket_list6 = ['[',']','(',')']
# def bracket_match(bracket_list = []):

#     bracket_dict = {
#         ']': '[',
#         ')': '(',
#         '}': '{'
#     }

#     left_bracket_checklist = []

#     if not bracket_list:
#         return False
    
#     for bracket in bracket_list:
#         if bracket in bracket_dict.values():
#             left_bracket_checklist.append(bracket)
#         elif bracket not in bracket_dict.values():
#             if not left_bracket_checklist:
#                 return False
#             elif left_bracket_checklist[-1] == bracket_dict[bracket]:
#                     left_bracket_checklist.pop()
#             else:
#                 return False

#     if left_bracket_checklist == []:
#         return True
#     else:
#         return False

# print(bracket_match(bracket_list1)) #True {[()]}
# print(bracket_match(bracket_list5)) #True []
# print(bracket_match(bracket_list2)) #False ]{[()]}
# print(bracket_match(bracket_list3)) #False {[()]}[
# print(bracket_match(bracket_list4)) #False [
# print(bracket_match(bracket_list6)) #True []()
            



# # Given a sorted array of integers and a target average, 
# #   determine if there is a pair of values in the array where the average of the pair equals the target. O(N)

# #RUNDOWN
#     # We save each value into a set as we iterate over the list
#     # (value + currVal)/2 = target
#     # So if 2*target - currVal = value in our set, we return True

# our_list = [1,2,3,4,5,6,7,8,9,10]
# def average_of_pair_is_target(our_list, target):

#     value_set = set()

#     for value in our_list:
#         paired_value =  2*target - value
#         if paired_value in value_set:
#             return True
#         value_set.add(value)
#     return False

# print(average_of_pair_is_target(our_list, 6)) #True - 5, 7
# print(average_of_pair_is_target(our_list, 4)) #True - 3, 5
# print(average_of_pair_is_target(our_list, 12)) #False - no pairs = 24




# Given a list and a target, return how many pairs of numbers sum to that target in O(N)

#RUNDOWN:
    # We save each value into a set as we iterate over the list
    # If the difference of the target and the currVal is a value we've saved
    # We have a pair that add to the target
    # We then update a count variable and add the pair as a tuple into a list

# our_list = [1,2,3,4,5,6,7,8,9,10,11,12]
# def return_pairs_of_additors_to_target_in_list(our_list, target):

#     potential_additors = set()
#     sum_pair_count = 0
#     pair_list = []

#     for value in our_list:
#         difference = target - value
#         if difference in potential_additors:
#             sum_pair_count += 1
#             pair_list.append((value, difference))
#         potential_additors.add(value)

#     return (f'Pairs that add to {target}: {sum_pair_count}. Our list of pairs: {pair_list}.')

# print(return_pairs_of_additors_to_target_in_list(our_list, 9)) # 4, [(5,4),(6,3),(7,2)(8,1)]

# # Given a list of numbers and a target, find if any 2 numbers sum to target in O(N)

# #RUNDOWN:
#     # We save each value into a set as we iterate over the list
#     # If the difference of the target and the currVal is a value we've saved 
#     # We know we have two values that would sum to our target
# our_list = [1,2,3,4,5,6,7,8,9]
# def sum_to_target_in_list(our_list, target):

#     dif_set = set()

#     for value in our_list:
#         difference = target - value
#         if difference in dif_set:
#             return ([True, difference, value])
#         dif_set.add(value)
#     return False

# print(sum_to_target_in_list(our_list, 9)) #True 4,5 will be the two that trigger
# print(sum_to_target_in_list(our_list, 6)) #True 2,4 will be the two that trigger
# print(sum_to_target_in_list(our_list, 0)) #False
# print(sum_to_target_in_list(our_list, 100)) #False



# #BASIC LINEAR SEARCH

# our_list = [0,1,2,3,4,5,6,7,8,9,10]
# print(["NO", "YES"][10 in our_list])

# #BASIC BINARY SEARCH

# def binary_search(our_list, val):

#     left = 0
#     right = len(our_list) - 1
#     mid = (left + right)//2

#     while right > left:
#         mid = (left + right)//2
#         if val > our_list[mid]:
#             left = mid + 1
#         elif val < our_list[mid]:
#             right = mid - 1
#         else:
#             return mid
#     return -1
# print(binary_search(our_list, 5)) #5


# #FIBONACCI SEQUENCE 0 1 1 2 3 5 8 13 21 34 etc
#     # Addition of the previous 2 numbers in the next number, starting with 0 1

# def recursive_fibonacci_nth_in_seq(n):

#     #BASE CASE
#     if n <= 1:
#         return n
    
#     #RECURSIVE CASE
#     else:
#         return (recursive_fibonacci_nth_in_seq(n-1) + recursive_fibonacci_nth_in_seq(n-2))
# print(recursive_fibonacci_nth_in_seq(9)) #21 (0 1 1 2 3 5 8 13 21 34)

# #Print first n numbers of fibonacci
# def print_fibonacci(n):
#     for i in range(n):
#         print(recursive_fibonacci_nth_in_seq(i))
# print_fibonacci(10) # 1 1 2 3 5 8 13 21 34 55

# def recursive_countdown(n):

#     #BASE CASE:
#     if n == 0:
#         print(0)
    
#     #RECURSIVE CASE
#     else:
#         print(n)
#         recursive_countdown(n-1)
# recursive_countdown(5) #5 4 3 2 1 0 column


# def recursive_sum_down(n):

#     #BASE CASE:
#     if n == 1:
#         return 1
    
#     #RECURSIVE CASE:
#     else:
#         return n + (recursive_sum_down(n-1))
# print(recursive_sum_down(5)) #15





                    # # 12/14





# #Basic Recursive Countdown

# def recursive_countdown(n):
#     print(n)
#     if n == 1: 
#         return 0
#     else:
#         return recursive_countdown(n-1)



# #Factorial recursion

# def factorial_recursion(n):
#     try:
#         if type(n) != int:
#             return ('Error: Not an integer.')
#         elif n == 0:
#             return 0
#         elif n == 1 or n == -1:
#             return n
#         elif n < 0:
#             return n * factorial_recursion(n+1)
#         elif n > 0:
#             return n * factorial_recursion(n-1)
#     except:
#         print("Error: Something else went wrong,")
    


# #Basic recursive sum

# def basic_recursive_sum(n):
#     if type(n) != int:
#         return ('Error: Not an integer.')
#     if n == 0:
#         return 0
#     elif n == 1: 
#         return 1
#     elif n < 0:
#         return n + basic_recursive_sum(n+1)
#     elif n > 0:
#         return n + basic_recursive_sum(n-1)



# if __name__ == '__main__':

#     print(recursive_countdown(4))

#     print(factorial_recursion(-5))
#     print(factorial_recursion(5))
#     print(factorial_recursion(1))
#     print(factorial_recursion(0))
#     print(factorial_recursion('x'))

#     print(basic_recursive_sum(-5))
#     print(basic_recursive_sum(5))
#     print(basic_recursive_sum(1))
#     print(basic_recursive_sum(0))
#     print(basic_recursive_sum('x'))
