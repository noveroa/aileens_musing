def reverseS(s):
    # Write a function that reverses a string. The input string is given as an array of characters s.
    # You must do this by modifying the input array in-place with O(1) extra memory.
    s.reverse()
    #s[::-1]

def reverseInt(i):
    # Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    MIN=-(2**31)
    MAX=(2**31)-1
    s = str(i)
    res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1]) # reverse and remove sign
    return res if MIN <= res <= MAX  else 0

from collections import Counter

def findUnique(s):
    # create a hash counter with python
    c = Counter(s)
    for i, d in enumerate(s):
        if c[d] == 1:
            return i
    return -1

def validAnagram(s,t):

    return sorted(s) == sorted(t)

import re
def validPalindrome(s):
    # drop spaces and non alphanums
    t = re.sub(r'[\W+]', '', s).lower().strip()
    t = re.sub(r"_", "", t)
    return t == t[::-1]

def findNeedle(h, n):
    return h.find(n)

def longestCommonPrefix(arr):
        
        arr.sort()

        # Get the first and last strings after sorting
        first = arr[0]
        last = arr[-1]
        minLength = min(len(first), len(last))

        i = 0
        # Find the common prefix between the first
        # and last strings
        while i < minLength and first[i] == last[i]:
            i += 1

        # Return the common prefix
        return first[:i]

if __name__ == '__main__':
    print(reverseS( ["h","e","l","l","o"]))
    print(reverseInt(123), reverseInt(-123))
    print(findUnique('leetcode'))
    print(findNeedle('hello', "ll"))
    print(longestCommonPrefix(["flower","flow","flight"]))