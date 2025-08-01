import sys, os
import numpy as np

def npMatrix( matrix: list[list[int]] = [[3,7,8], [9,11,13], [15,16,17]]):

    m = np.array(matrix)
    rows, cols = m.shape
    print(f"Rows: {rows}, Columns: {cols}")

def listMatrix(matrix: list[list[int]] = [[3,7,8], [9,11,13], [15,16,17]]):
    """
    Given a matrix (list of lists), return the elements that are the minimum in their row and maximum in their column.
    """
            
    cols =  [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    rows =  [matrix[i] for i in range(len(matrix))]

    magics = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if min(rows[i]) == max(cols[j]):
                magics.append(matrix[i][j]) 
    return magics


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # # Method to add a node at the beginning of the LL
    # def insertAtBegin(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        # Print the linked list

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    
def offEvenLinkedList(head : list[int] = [1,2,3,4,5]):
    """
    1. Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    2. Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed)
    """
    l = LinkedList()
    for i in head:
        l.insertAtEnd(i)
    l.printLL()

    def oddEvenList(head):
        if not head or not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        odd = odd_head
        even = even_head
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return odd_head
        
    result1 = oddEvenList(l.head)
    # Expected output: 1 -> 3 -> 5 -> 2 -> 4
    current = result1
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # matrices = [
    #     [[3,7,8], [9,11,13], [15,16,17]],
    #     [[1,10,4,2],[9,3,8,7],[15,16,17,12]],
    #     [[7,8],[1,2]]
    #     ]
    # for matrix in matrices:
    #     print(f"Matrix: {matrix}")
    #     print(listMatrix(matrix))

    
    offEvenLinkedList()