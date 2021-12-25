from linked_list import LinkedList

#NAIVE SOLUTION ON (2N)

# def print_middle(self):
        
#         current_node = self.head

#         if not current_node:
#             return -1
#         else:
#             if self.size % 2 == 0:
#                 threshold = self.size//2
#             else:
#                 threshold = self.size//2 + 1

#             i = 1
#             while i  < threshold:
#                 current_node = current_node.next
#                 i += 1

#         print(current_node.val)


# #FASTER - TWO POINTERS WITH SLOW POINTER
# #TWO POINTER O(N)
#     def find_middle(self):

#         current_node = self.head

#         if not current_node:
#             return -1
#         else:
#             fast_pointer = current_node
#             half_pointer = current_node
#         i = 1
#         while fast_pointer.next:
#             fast_pointer = fast_pointer.next
#             if i % 2 == 0:
#                 half_pointer = half_pointer.next
#             i += 1

#         print(half_pointer.val)

our_LL = LinkedList()
our_LL.append(1)
our_LL.append(2)
our_LL.append(3)
our_LL.append(4)

# print(our_LL.length())

our_LL.print_middle()
our_LL.find_middle()

our_LL.append(5)

our_LL.print_middle()
our_LL.find_middle()