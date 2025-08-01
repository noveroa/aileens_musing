
def dropDupes(nums):

    # in place, order matters; nums in non decreasing order
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return nums

def maxProfit(prices) :
    p = 0
    for i in range(len(prices)-1):
        buy_price, sell_price = prices[i], prices[i+1]
        print('Buy?', sell_price - buy_price)
        p += max(0, sell_price - buy_price)
        print('current profit', p)
    return p

def rotate(nums, k):
    #Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    for i in range(k):
        nums.insert(0, nums.pop())
    return nums


def dupesExist(nums):
    #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

    found = set()
    for i in nums:
        if i in found:
            return True
        else:
            found.add(i)
    return False

def singleNumber(nums):
    # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    # You must implement a solution with a linear runtime complexity and use only constant extra space.
    res = 0
    # This approach uses the XOR operation to find the unique element in an array where every other element appears twice. XOR of two identical numbers cancels them out (results in zero), so after XORing all the elements, only the element that appears once will remain. 
    # Find XOR of all elements
    for num in nums:
        res ^= num
    return res
    # for i in range(n):

    #     # Initialize count to 0
    #     count = 0

    #     for j in range(n):

    #         # Count the frequency of the element
    #         if arr[i] == arr[j]:
    #             count += 1

    #     # If the frequency of the element is one
    #     if count == 1:
    #         return arr[i]

    # # If no element exists at most once
    # return -1
from collections import Counter
def intersectArray(nums1, nums2):
    #Intersection of Two Arrays II
    # Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

    c = Counter(nums1) & Counter(nums2)
    return list(c.elements())

def plusOne(ints):
    # You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    # we start with a carry of 1
    c = 1
    for i in range(len(ints)-1, -1, -1):
        # starting with least sigF, add the carry
        digit = ints[i] + c
        # now update the index with the Plus 1:
        ints[i] = digit % 10
        # whats carries?
        c = digit // 10
    if c > 0:
        ints.insert(0,c)
    return ints 

def moveZeros(nums):
    #Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    #modify nums in-place instead.
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums

def twoSum(nums, target):
    #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    found = {}
    for i, d in enumerate(nums):
        print(f'current hash: {found}')
        c = target - d
        print(f'looking for {c} for index {i}, value {d}')
        if c in found:
            print(f'we\'ve seen {c} at index {found[c]}')
            return [found[c], i]
        # otherwise record the value and idx
        found[d] = i
    return []

def validSudoku(board):
    # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules: 
    #board = list of lists

    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    # Note:

    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    miniBoard = [[set() for _ in range(3)] for _ in range(3)]
    
    for i in range(9):
        for j in range(9):
            if not board[i][j].isnumeric(): # empty, we don't care (ie ')
                continue
            
            num = board[i][j]
            print('board value', num)

            # mini board index:
            # Calculate box index for 3x3 sub-boxes using integer division.
            y = i // 3 
            x = j // 3
            if (num in rows[i]) or (num in cols[j]) or (num in miniBoard[x][y]):
                # we've seen it already!
                return False
            else:
                rows[i].add(num)
                cols[j].add(num)
                miniBoard[x][y].add(num)
    return True

def rotateImage(image):
    #You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    for i in range(len(image)):
        print(i)
        for j in range(i + 1, len(image)):
            print(j)
            image[i][j], image[j][i] = image[j][i], image[i][j]

    # Now we reverse each row
    for row in image:
        row.reverse()
    return image


if __name__ == "__main__":
    print(dropDupes([0,0,1,2,3,3,4,5,6,6,7,7,7]))
    
    print(maxProfit([7,1,5,3,6,4]))

    print(rotate([1,2,3,4,5,6,7], 3))
    print(dupesExist([1,2,3,4]), dupesExist([1,1,1,3,3,4,3,2,4,2]))
    print(intersectArray([1,2,2,1], [2,2]))
    print(plusOne([1,2,3]), plusOne([9]))
    print(moveZeros([0,1,0,3,12]))
    print(twoSum([2,7,11,15], 9))
    s1 = [   ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    s2 = [  ["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    
    print(validSudoku(s1), validSudoku(s2))
    # m = [   [1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12],
    #         [13, 14, 15, 16]
    #     ]
    m =  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print (rotateImage(m))