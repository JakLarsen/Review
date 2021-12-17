


# 12/17






# 12/16/21



# #Testing name =  main guard
# from dsa1 import recursive_countdown

# def recursive_sum_down(n):

#     #BASE CASE
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum_down(n-1)
# print(recursive_sum_down(5)) # 15



## Find all indices of a value in a list
# our_list = [1,1,2,3,1,2,1,1,4]
# our_idices_of_one = [e for e,v in enumerate(our_list) if v == 1]
# print(our_idices_of_one)

# tuple_list = [(1,2), (3,4), (5,6)]
# for (i,v) in tuple_list:
#     print(i,v)

# our_list = ['a','b','c','d','e']
# our_indexed_list = enumerate(our_list)
# print([(e,v) for e,v in our_indexed_list])

# our_string = 'hel+lo'
# our_split_string = our_string.split('+')
# print(our_split_string)

# our_char_list = ['h','e','l','l','o']
# our_joined_string = "".join(our_char_list)
# print(our_joined_string)





#12/14/21





#What is polymorphism?
    # A short explanation would be that it is the ability for a funtion to be sent to different class objects
    # and each will utilize that funtion potentially differently dependent on the class. 
    # I.E. Two bird child classes could each have a .fly() method on them, but one is a penguin, so .fly() looks different for a penguin than a seagull

#What is Flask
    #Flask is a web development framework and collection of libraries for Python, allowing easier construction of web applications

#What is Flask SQLAlchemy
    #Flask SQLAlchemy is a library and Object Relational Mapping framework that allows us to abstract our sql database management a bit for more pythonic and class-based use

#What does it mean that Python is an Interpreted Language
    #This means that Python is first compuled into bytecode, which is executed by an interpreter on a virtual machine
    #This makes it more easily standardized across different systems and more dynamic
    #Compiled languages are translated into machine code and executed on the CPU

#What are Abstract Data Types
    #Abstract Data Types are logical rules or implementation patterns for data
    #E.G. QUEUE (FIFO) - can be implemented with a linked list, array, etc
    # Stack (LIFO)

#What are Data Structures
    #Data structures are the actual structures of data in the program; strutures of storing data
    #E.G. Array, list, linked-list, dictionary, binary tree, graphs

#How are arrays structured in memory?
    #The first idx's address is stored along with consecutive blocks in memory of a specific datatype or size
    #Retrieval is done by multiplying the idx by the datatype size as a means of finding the address

#Difference between static and dynamic arrays
    #Static arrays are a fixed size and generalyl a fized data type (or data type size i'd assume)
    #If a static array fills, it is recopied with double the space
    #Dynamic arrays allow for a non-fized size and dynamically allocated memory for entries


#BIGO array insertion to end until full : Constant time O1
#BIGO array insertion to end when full : Linear time ON (recopy array into space with 2n space)
#BIGO array insertion to arbitrary : Linear time ON
#BIGO array remove last item : Constant time O1
#BIGO array remove arbitrary : Linear time ON
#If most operations are insertions or deletions to an end of a DS, arrays are: great
#If most operations are arbitrary insertions or deletions of a DS, arrays are: suboptimal often

#How does a list function in python under the hood
    #Lists are objects in python that store a reference (8bytes) along with the data of the datatype(int = 4bytes)
    #This makes them strong for dynamicism but could potentiall TRIPLE the size of your DS
    #An array of ints stores the first reference and each data, 12 + 4 + 4 + 4 Bytes or CLOSE
    #A list stores EACH reference and data 12 + 12 + 12 + 12 bytes

# a = our_list creates a second reference of our_list

# #Basic Recursive Sum
# def basic_recursive_sum(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n < 0: return n + basic_recursive_sum(n+1)
#     else: return n + basic_recursive_sum(n-1)
# print(basic_recursive_sum(0))
# print(basic_recursive_sum(1))
# print(basic_recursive_sum(15))
# print(basic_recursive_sum(-15))

# our_list = [1,2,1,1,3,4,2,1,1,2]
# our_list_of_idxs = [e for e,v in enumerate(our_list) if v == 1]
# print(our_list_of_idxs)

#Basic recursive sum
# def sum_nums(n):
#     return 1 if (n==1) else n + sum_nums(n-1)
# print(sum_nums(10))

# our_list_to_sum  = [1,2,3,4,5,6,7,8,9,10, -1, -2]
# our_sum = sum(our_list_to_sum)
# print(our_sum)
# our_abs = abs(our_list_to_sum[-1])
# print(our_abs)
# our_dict = {'1': 'hey', '2': 'popsicle'}
# our_dict_list = [(k,v) for k,v in our_dict.items()]
# our_key_list = [k for k in our_dict]
# our_value_list = [v for v in our_dict.values()]
# print(our_dict_list)
# print(our_key_list)
# print(our_value_list)
# our_list = ['a','b','c']
# our_indexed_list = [(e,v) for e,v in enumerate(our_list)]
# print(our_indexed_list)
# our_tuple_list = [(1,2), (3,4), (5,6)]
# our_destructured_tuple_list = []
# for (i,v) in our_tuple_list: 
#     our_destructured_tuple_list.append(i)
#     our_destructured_tuple_list.append(v)
# print(our_destructured_tuple_list)
# our_list = [1,2,3,1,2,3,1,1,1]
# our_list_of_idx = [e for e, v in enumerate(our_list) if v==1]
# print(our_list_of_idx)
# our_enumerated_list = [(e,v) for e,v in enumerate(our_list)]
# print(our_enumerated_list)
# our_list_idxs = [e for e,v in enumerate(our_list) if v == 2]
# print(our_list_idxs)
# our_list = ['hey', 'apples', 'third word']
# our_enumerated_list = [(idx,value) for idx, value in enumerate(our_list)]
# print(our_enumerated_list)
# our_list = [0,1,2,3,4,5,6,7,8]
# print(our_list.index(1)) #1
# our_string = 'apple'
# our_string = our_string[0].capitalize() + our_string[1:]
# print(our_string)
# our_string = "captilize"
# our_string = our_string[0].capitalize() + our_string[1:]
# print(our_string)
# our_string_list = [i for i in our_string]
# our_separated_string_list = ','.join(our_string_list)
# print(our_separated_string_list)
# our_string_list.sort()
# print(our_string_list)
# a_separated_string = ','.join("capitalize")
# print(a_separated_string)
# print('Hello World')
# string_input = input()
# print('string_input: ', string_input)
# integer_input = int(input())
# print('integer_input: ', integer_input)
# a,b,c = map(int, input().split())
# print('multiple_integer_input: ', a,b,c)
# our_list = [int(i) for i in input().split()]
# print('our_list', our_list)
# our_list2 = [i for i in input().split()]
# print('our_list2', our_list2)
# our_list3 = input().split()
# print('our_list3', our_list3)
# our_char_list = [i for i in input()]
# print('our_char_list: ', our_char_list)
# our_tuple = [(int(i), -1) for i in input()]
# print(our_tuple)
# yneos = ['NO','YES'][int(input()) % 2 == 0]
# print(yneos)
# print("a" in "apple")
# print("apple"[1])
# print("abcdefg" > "abcdeff")
# print("abs" < "abz")
# print("abs" > "Abz")
# print("a" > "Z")
# print("A" < "Z")
# our_word = "apple"
# our_separated_list = our_word.split('l')
# our_input = "1+2+3+4+5"
# our_separated_list2 = our_input.split('+')
# print(our_separated_list)
# print(our_separated_list2)