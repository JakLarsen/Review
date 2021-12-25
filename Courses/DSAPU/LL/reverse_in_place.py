from linked_list import LinkedList


#  def reverse_in_place(self):
#         #NAIVE just constructs another list with flipped pointers

#         #3 POINTER REVERSAL
#         current_node = self.head
#         if not current_node:
#             return None
        
#         prev_node = None
#         next_node = None

#         while current_node:
#             next_node = current_node.next
#             current_node.next = prev_node
#             prev_node = current_node
#             current_node = next_node
#         self.head = prev_node



our_LL = LinkedList()
our_LL.append(1)
our_LL.append(2)
our_LL.append(3)
our_LL.append(4)

our_LL.traverse()

our_LL.reverse_in_place()

our_LL.traverse()