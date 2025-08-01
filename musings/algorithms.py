#algorithms
from collections import deque
class Sorting:

    
    def quicksort(self, arr):

        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort each half
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)
        
        # Merge the sorted halves
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        left_idx = 0
        right_idx = 0
        
        # Merge two sorted arrays
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        
        # Append remaining elements
        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        
        return result
    
def heap_sort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)

def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child position
        right = 2 * i + 2  # Right child position

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than root
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap

            # Heapify the root.
            heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate mid point
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    
    # Target is not present in array
    return -1

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f'Key {key} not found')

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f'Key {key} not found')
    
def bfs(graph, start):
    # Initialize a queue for BFS and add the start node
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set()
    # Mark the start node as visited
    visited.add(start)
    
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Get all adjacent nodes of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


if __name__ == "__main__":
        arr = [3, 6, 8, 10, 1, 2, 1]        
        qS = Sorting()
        sorted_arr = qS.quicksort(arr)
        print(sorted_arr)
        sorted_arr = qS.merge_sort(arr)
        print(sorted_arr)

        heap_sort(arr)
        print("Sorted array:", arr)
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7
        result = binary_search(arr, target)

        if result != -1:
            print(f"Element {target} is present at index {result}.")
        else:
            print(f"Element {target} is not present in the array.")

        hash_table = HashTable(10)
        hash_table.insert('apple', 5)
        hash_table.insert('banana', 7)
        hash_table.insert('cherry', 10)

        print(hash_table.get('banana'))  # Output: 7

        # hash_table.delete('banana')
        # print(hash_table.get('banana'))  # Raises KeyError: 'Key banana not found'
        graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

        # Perform BFS starting from node 'A'
        print('bfs')
        bfs(graph, 'A')
        print('\ndfs')
        dfs_recursive(graph, 'A')