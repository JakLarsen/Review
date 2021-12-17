




                    # 12/16 - 12/17


# def same_freq_digits(n1, n2):
    
#     freq_map_n1 = {}
#     freq_map_n2 = {}

#     for digit in str(n1):
#         if digit in freq_map_n1:
#             freq_map_n1[digit] += 1 
#         else:
#             freq_map_n1[digit] = 1
    
#     for digit in str(n2):
#         if digit in freq_map_n2:
#             freq_map_n2[digit] += 1 
#         else:
#             freq_map_n2[digit] = 1
    
#     if len(str(n1)) != len(str(n2)): 
#         return False 
    
#     for digit_key in freq_map_n1:
#         if digit_key not in freq_map_n2:
#             return False
#         elif freq_map_n1[digit_key] != freq_map_n2[digit_key]:
#             return False
            
#     return True

# print(same_freq_digits(515,155)) # True
# print(same_freq_digits(515,15)) # False
# print(same_freq_digits(51,155)) # False
# print(same_freq_digits(512,155)) # False
# print(same_freq_digits(2,3)) # False
# print(same_freq_digits(2,2)) # True

# def check_palindrome(our_string):

#     start = 0
#     end = len(our_string) - 1

#     while end > start:
#         if our_string[start] != our_string[end]:
#             return False
#         end -= 1
#         start += 1
    
#     return True

# print(check_palindrome('tacocat')) # True
# print(check_palindrome('tacocats')) # False

# def python_palindrome(s):

#     return s == s[::-1]

# print(python_palindrome('tacocat')) # True
# print(python_palindrome('tacocats')) # False

# def find_mode(our_list):

#     freq_map = {

#     }

#     for num in our_list:
#         if num in freq_map:
#             freq_map[num] += 1
#         else:
#             freq_map[num] = 1
    
#     max_mode = -9999999
#     max_freq = 0
#     for num in freq_map:
#         if freq_map[num] >= max_freq:
#             max_freq = freq_map[num]
#             if num > max_mode:
#                 max_mode = num

#     return max_mode
# print(find_mode([0,0,1,1,1,2,2,2,2,3,3,3,3])) # 3
# print(find_mode([0,1,1,1,2,2,2,2,3,3])) # 2
    
# def find_median(our_list):

#     if len(our_list) % 2 == 0:
#         return (our_list[len(our_list)//2] + our_list[len(our_list)//2 +1])/2
#     else:
#         return our_list[len(our_list)//2]
# print(find_median([0,1,2,3,4,5,6,7,8,9])) # 4.5
# print(find_median([0,1,2,3,4,5,6,7,8])) # 4

# class Node:

#     def __init__(self, val = None, next = None):
#         self.val = val
#         self.next = next
    
# class LinkedList:

#     def __init__(self, head, tail):
#         self.head = head
#         self.tail = tail
    
#     def print_every_other(self):

#         i = 1
#         currentNode = self.head
#         while currentNode:
#             if i % 2 != 0:
#                 print(currentNode.val)

# def recursive_fibonacci_nth(n):

#     #BASE CASE
#     if n <= 1:
#         return n
#     return (recursive_fibonacci_nth(n-1) + recursive_fibonacci_nth(n-2))
# print(recursive_fibonacci_nth(9))


# def bracket_match(bracket_list):

#     bracket_dic = {
#         ']': '[',
#         ')': '(',
#         '}': '{'
#     }
#     left_bracket_list = []

#     for bracket in bracket_list:
#         #If it's a left-sided bracket
#         if bracket not in bracket_dic:
#             #Add to pop_queue
#             left_bracket_list.append(bracket)
#         #closing-bracket
#         elif bracket in bracket_dic:
#             #no opening-brackets to close
#             if not left_bracket_list:
#                 return False
#             #Check if it matches last opening bracket
#             elif left_bracket_list[-1] == bracket_dic[bracket]:
#                 left_bracket_list.pop()
#             else:
#                 return False

#     if left_bracket_list:
#         return False
#     else:
#         return True

# print(bracket_match(['[',']','(',')'])) #True
# print(bracket_match([']','[','(',')'])) #False
# print(bracket_match(['[','(',')',']'])) #True
                



# def average_of_pair_is_target(our_list, target):

#     value_set = set()

#     for value in our_list:
#         if 2*target-value in value_set:
#             return True
#         value_set.add(value)
#     return False

# print(average_of_pair_is_target([1,2,3,4,5,6,7,8], 7)) #True (8,6)
# print(average_of_pair_is_target([1,2,3,4,5,6,7,8], 14)) #False

# def count_pairs_sum_to_target(our_list, target):
#     count = 0

#     value_set = set()

#     for value in our_list:
#         if target - value in value_set:
#             count += 1
#         value_set.add(value)
#     return count

# print(count_pairs_sum_to_target([0,1,2,3,4,5,6,7,8], 9)) #4
# print(count_pairs_sum_to_target([0,1,2,3,4,5,6,7,8], 25)) #0

# def pair_sum_to_target(our_list, target):

#     value_set = set()

#     for value in our_list:

#         if target - value in value_set:
#             return True
#         value_set.add(value)

#     return False
# print(pair_sum_to_target([0,1,2,3,4,5], 8)) #True, 5,3
# print(pair_sum_to_target([0,1,2,3,4,5], 11)) #False

# def basic_binary(our_list = [1,2,3,4,5,6,7,8,9], target = 11):

#     left = 0
#     right = len(our_list)-1

#     while left <= right:
#         mid = (left + right)//2

#         if target == our_list[mid]:
#             return mid
#         elif target < our_list[mid]:
#             right = mid - 1
#         elif target > our_list[mid]:
#             left = mid + 1

#     return -1
# print(basic_binary())


# def recursive_fibonacci_nth(n):

#     #BASE CASE
#     if n <= 1:
#         return n
#     else:
#         return(recursive_fibonacci_nth(n-1) + recursive_fibonacci_nth(n-2))
# print(recursive_fibonacci_nth(9))

# def print_fibonacci_first_n(n):
#     for i in range(n):
#         print(recursive_fibonacci_nth(i))

# print_fibonacci_first_n(9)

# def recursive_countdown(n):

#     print(n)

#     #BASE CASE
#     if n == 0:
#         return
#     else:
#         return recursive_countdown(n-1)
# recursive_countdown(5)


# def factorial_recursion(n):

#     #BASE CASE
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursion(n-1)
# print(factorial_recursion(5))

# def get_mean(our_list):
#     return sum(our_list)/len(our_list)

# print(get_mean([1,2,3,4,5,6,7,8,9,10]))


# #LL STACK INSERT AND POP TAIL (OR HEAD - PICK)

# class Node:

#     def __init__(self, val = None, next = None):
#         self.val = val
#         self.next = next

# class LinkedList:

#     def __init__ (self, head = None, tail = None):
#         self.head = head
#         self.tail = tail

#     def traverse(self):
#         print('TRAVERSING')
#         if self.head == None:
#             print('Nothing in LL.')
#         else:
#             currentNode = self.head
#             while currentNode:
#                 print(currentNode.val, currentNode)
#                 currentNode = currentNode.next

#     def LL_peak_head(self):
#         print(f'Head is: {self.head}, {self.head.val}')

#     def LL_peak_tail(self):
#         print(f'Tail is: {self.tail}, {self.tail.val}')

#     def LL_append(self, Node):
#         if self.head == None:
#             self.head = Node
#             self.tail = Node
#         else:
#             self.tail.next = Node
#             self.tail = Node

#     def LL_pop(self):

#         #0 Nodes
#         if self.head == None:
#             return None
#         #1 Node
#         elif self.head.next == None:
#             pop_val = self.head.val
#             self.head = None
#             self.tail = None
#             return pop_val
#         #2 + Nodes
#         # else:
#         else:
#             currentNode = self.head
#             #second to last Node will be in currentNode after
#             while currentNode.next.next:
#                 currentNode = currentNode.next
#             #Grab tail to return
#             pop_val = currentNode.next.val
#             #Set second to last to tail
#             currentNode.next = None
#             self.tail = currentNode
#             return pop_val
    
#     def LL_print_every_other(self):

#         #0 Nodes
#         if self.head == None:
#             print('LL is empty.')
        
#         #Nodes in list
#         counter = 1
#         currentNode = self.head
#         while currentNode:
#             if counter % 2 != 0:
#                 print(f'Node: {counter} is: {currentNode.val}.')
#             currentNode =  currentNode.next
#             counter += 1

# #Basic LL methods 
# our_LL = LinkedList()
# a_Node = Node('a')
# b_Node = Node('b')
# c_Node = Node('c')
# c_Node = Node('d')
# c_Node = Node('e')
# our_LL.traverse()
# our_LL.LL_append(a_Node)
# our_LL.traverse()
# our_LL.LL_pop()
# our_LL.traverse()
# our_LL.LL_append(a_Node)
# our_LL.LL_append(b_Node)
# our_LL.LL_peak_tail()
# our_LL.traverse()
# our_LL.LL_pop()
# our_LL.LL_peak_tail()
# our_LL.traverse()


# #Print every other
# num_LL = LinkedList()
# first = Node(1)
# second = Node(2)
# third = Node(3)
# fourth = Node(4)
# fifth = Node(5)
# num_LL.LL_append(first)
# num_LL.LL_append(second)
# num_LL.LL_append(third)
# num_LL.LL_append(fourth)
# num_LL.LL_append(fifth)
# num_LL.traverse()
# num_LL.LL_print_every_other()











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

