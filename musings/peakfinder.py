
def brute_naive_peak(arr: list = None):
    # one dimension - given array find peak if exists
    # b >= a; b <=c
    # [1.....n/2....n-1, n]
    l = lambda a,b: a >= b
    p = 0 
    for x in range(1, len(arr)-1):
        if all([
            l(arr[x],arr[x-1]), l(arr[x], arr[x+1])]
            ):
            print('found', arr[x-1], arr[x], arr[x+1])
            p = p+1
        else:
            pass
    return p

def find_peak_divide_conquer(arr, low, high, peaks):
    """
    Finds a peak element in an array using divide and conquer.

    Args:
        arr: The input array.
        low: The starting index of the subarray.
        high: The ending index of the subarray.

    Returns:
        The index of a peak element, or None if the array is empty.
    """
    if low <= high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid])):
            print('found', mid, arr[mid])
            peaks.append(mid)

        # Recursively search for more peaks in left and right subarrays
        find_peak_divide_conquer(arr, low, mid - 1, peaks)
        find_peak_divide_conquer(arr, mid + 1, high, peaks)
    return peaks

def divideandconquerpeak(arr: list):
    # [1.....n/2-1,n/2, n/2+1....n-1, n]
    # at n/2 look right and left
    # if [n/2] < a[n/2-1], look at left (1...n/2-1), else look rihgt
    #else done
    peaks =  find_peak_divide_conquer(arr, 0, len(arr)-1, [])

    return peaks


#The greedy ascent algorithm is a technique used to find a local maximum in a given search space. It's an iterative process that starts from an initial point and repeatedly moves to a neighboring point with a higher value until no such neighbor exists. 
def get_neighbors_2d(point):
        """Returns the 4-connected neighbors of a 2D point
        Define neighbors per problem"""
        x, y = point
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def evaluate_2d(point, grid):
        """Evaluates a 2D point based on the grid value
        Define evaluation per problem"""
        x, y = point
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return grid[x][y]
        return -float('inf') # Return -infinity for out-of-bounds points

def greedy_ascent(start_point, get_neighbors_2d, evaluate_2d):
    """
    Performs a greedy ascent search to find a local maximum.

    Args:
        start_point: The starting point for the search.
        get_neighbors: A function that takes a point and returns its neighbors.
        evaluate: A function that takes a point and returns its value.

    Returns:
        The local maximum found by the greedy ascent algorithm.
    """

    #Start: Begin at an arbitrary point in the search space.
    current = start_point
    while True:
       # Get and  Evaluate Neighbors: Examine the neighboring points of the current location.
        neighbors = get_neighbors_2d(current)
        best_neighbor = None
        best_value = evaluate_2d(current)

        for neighbor in neighbors:
            neighbor_value = evaluate_2d(neighbor, )
            # Move: If a neighbor has a higher value than the current point, move to that neighbor.
            if neighbor_value > best_value:
                best_value = neighbor_value
                best_neighbor = neighbor

        if best_neighbor is None:
            return current  # Local maximum found
        current = best_neighbor

if __name__ == "__main__":
    r = brute_naive_peak([1,3,5,2,6,9,4,5])
    d = divideandconquerpeak([1,3,5,2,6,9,4,5])
    print(f'brute peaks {r}')
    print(f'd&c peaks {d}')

    grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

    start = (0, 0)
    local_max = greedy_ascent(start, lambda p: get_neighbors_2d(p), lambda p: evaluate_2d(p, grid))

    print(f"Local maximum found at: {local_max} with value {evaluate_2d(local_max, grid)}") # Output: Local maximum found at: (3, 3) with value 16
