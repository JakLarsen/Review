#Basic Linked List implementation

import time


class Node:

    def __init__ (self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def length(self):
        return self.size

    def traverse(self):

        currentNode = self.head
        
        #IF NO NODES:
        if currentNode == None:
            print('No Nodes in Linked List.')

        #WE HAVE A POPULATED LINKEDLIST
        else:
            while currentNode:
                print(currentNode.val)
                currentNode = currentNode.next

    def print_every_other(self):

        i = 1
        currentNode = self.head

        #IF NO NDOES
        if currentNode == None:
            print(-1)
        else:
            while currentNode:
                if i % 2 != 0:
                    print(currentNode.val)
                currentNode = currentNode.next
                i += 1
    
    #YOU CANNOT APPEND A PREEXISTING NODE - MAKE NEW NODE FOR THIS TO PREVENT
    def append(self, val):

        our_node = Node(val)
        
        #IF NO NODES
        if not self.head:
            self.head = our_node
        
        #THERE IS ALREADY A HEAD
        else:
            currentNode = self.head
            #FIND LAST NODE
            while currentNode.next:
                currentNode = currentNode.next
            #APPEND TO LAST NODE
            currentNode.next = our_node
        
        #INCREMENT SIZE
        self.size += 1
    
    #YOU CANNOT APPEND A PREEXISTING NODE TO THE FRONT - MAKE NEW NODE FOR THIS TO PREVENT
    def append_front(self, val):

        our_node = Node(val)

        #IF NO NODES
        if not self.head:
            self.head = our_node

        #ALREADY POPULATED LINKED LIST
        else:
            our_node.next = self.head
            self.head = our_node
        
        self.size += 1
    
    def remove_all(self, val_to_remove):

        currentNode = self.head
        previousNode = None

        #WE NEED TO KEEP TRACK OF SECOND TO LAST NODE TO REPAIR LL
        #IF WE REMOVE THE HEAD, NEXT NODE BECOMES HEAD 

        #IF NO NODES EXIST:
        if not self.head:
            return ('NO NODES IN LIST')
        
        #PREPOPULATED LL
        while currentNode:
            print(f'PREVIOUS NODE: ', previousNode)
            print(f'CURRENT NODE: ', currentNode)
            #IF WE'RE AT THE HEAD
            if previousNode == None:
                print('CURRENT NODE IS THE HEAD')
                #IF WE REMOVE THE HEAD
                if currentNode.val == val_to_remove:
                    print('REMOVING THE HEAD')
                    #IF THERE IS ANOTHER NODE IN LIST, UPDATE IT TO HEAD
                    if currentNode.next:
                        self.head = currentNode.next
                        self.size -= 1
                    #IF THE LIST WAS ONLY THAT REMOVABLE HEAD NODE
                    else:
                        print('NO NODES IN LIST AFTER HEAD REMOVAL')
                        self.head = None
                        self.size = 0
                previousNode = currentNode
                currentNode = currentNode.next
            #WE HAVE A NON-REMOVABLE HEAD       
            else:
                print('WE HAVE NONREMOVABLE HEAD')
                if currentNode.val == val_to_remove:
                    print('WE ARE REMOVING THE CURRENT NODE')
                    previousNode.next = currentNode.next
                    del currentNode
                    self.size -= 1

                    currentNode = previousNode.next
                else:
                    print('NO REMOVAL OF THE CURRENT NODE')
                    previousNode = currentNode
                    currentNode = currentNode.next




        







#DRIVER IF IT IS THE MODULE BEING EXECUTED
if __name__ == '__main__':

    our_LL = LinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # our_LL.append(node1) # 1
    # our_LL.append(node2) # 2
    # our_LL.append(node3) # 3

    # our_LL.traverse() # 1 2 3

    # # These break our previous setup where we passed in a node instead of just a value
    # # our_LL.append(node2) # 2
    # # our_LL.append_front(node3) # 3

    # our_LL.traverse() # 3 1 2 3

    our_LL.append(1)
    our_LL.append(2)
    our_LL.append(3)

    # our_LL.traverse() # 1 2 3

    our_LL.append(2)

    # our_LL.traverse() # 1 2 3 2 (NO INF LOOP THIS TIME)

    our_LL.append_front(2)

    our_LL.traverse() # 2 1 2 3 2
    our_LL.print_every_other() # 2 2 2

    # print(our_LL.length()) # 5

    our_LL.remove_all(2)

    our_LL.traverse() # 1 3

    start = time.time()
    for i in range(100000):
        our_LL.append_front(i)
    print('100,000 iterations of appending to front LL: ', time.time() - start, 'seconds')

    our_list = []
    start = time.time()
    for i in range(100000):
        our_list.insert(0,i)
    print('100,000 iterations for appending to front List: ', time.time() - start, 'seconds')








