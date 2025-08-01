import sys, os

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next
    
    def insertEnd(self, data):
        
        if self.head == None:
            self.head = Node(data)
        else:
            c = self.head
            while c.next:
                c = c.next
            c.next = Node(data)
    
    def insertStart(self, data):
        new_node= Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insertIndex(self, data, index):
        
        if index == 0:
            self.insertStart(data)
        else:
            
            pos = 0
            c = self.head
            while c != None and pos+1 != index:
                c = c.next
                pos = pos+1
            if c != None:
                new_node = Node(data)
                new_node.next = c.next
                c.next = new_node
            else:
                print('Out of range')

    def merge(self, first, second):
  
        # If either list is empty, return the other list
        if not first:
            return second
        if not second:
            return first

        # Pick the smaller value between first and second nodes
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second
        
    def splitList(self, head = None):
        if not head:
            head = self.head
        fast = head
        slow = head
     
        # one step 
        while fast and fast.next:
            # Move fast pointer two steps 
            fast = fast.next.next
            if fast:
                #and slow pointer one step until end
                slow = slow.next

        # Split the list into two halves
        second = slow.next
        slow.next = None
        return second
    
    def merge_sort(self, head):
  
    # Base case: if the list is empty or has only one node, 
    # it's already sorted
        if not head or not head.next:
            return head

    # Split the list into two halves
        second = self.splitList(head)

    # Recursively sort each half
        head = self.merge_sort(head)
        second = self.merge_sort(second)

    # Merge the two sorted halves
        return self.merge(head, second)
    
    def printLL(self):
        c = self.head
        while c:
            print (c.data)
            c = c.next

       
if __name__ == "__main__":

    l = LinkedList()

    for i in [3,5,6,1,3,7,3,9,0]:
        l.insertEnd(i)

    l.printLL()

    l.insertStart(0)
    l.printLL()

    l.insertIndex(2, 2)
    l.printLL()

    l.insertIndex(2, 50)
    print("***presort***")
    l.printLL()
    f = l.merge_sort(l.head)
    print("***postsort***")
    while f:
        print (f.data)
        f= f.next