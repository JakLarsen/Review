





from os import curdir


class Node:

    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:

    def __init__(self, head = None, tail = None, size = 0):
        self.head = head
        self.tail = tail
        self.size = size
    
    def traverse_forward(self):

        if not self.head:
            print('NO DLL')
        else:
            current_node = self.head
            while current_node:
                print(current_node.val)
                current_node = current_node.next
        
    def traverse_backwards(self):

        if not self.head:
            print('NO DLL')
        else:
            current_node = self.tail
            while current_node:
                print(current_node.val)
                current_node = current_node.prev

    
    def append(self, val):

        our_node = Node(val)
        
        #IF EMPTY
        if not self.head:
            self.head = our_node
            self.tail = our_node
        
        #IF NOT EMPTY
        else:
            self.tail.next = our_node
            #REMEMBER TO UPDATE PREV AND TAIL WITH DLL
            our_node.prev = self.tail
            self.tail = our_node
        
        self.size += 1

    def append_front(self, val):

        our_node = Node(val)

        #IF EMPTY
        if not self.head:
            self.head = our_node
            self.tail = our_node
        else:
            our_node.next = self.head
            self.head.prev = our_node
            self.head = our_node
        
        self.size += 1






#DRIVER GUARD - IF MODULE ITSELF EXECUTED
if __name__ == '__main__':

    our_DLL =  DLL()

    our_DLL.append(1)
    our_DLL.append(2)
    our_DLL.append(3)

    our_DLL.traverse_forward() # 1 2 3

    our_DLL.append_front(2)

    our_DLL.traverse_forward() # 2 1 2 3
    our_DLL.traverse_backwards() # 3 2 1 2





