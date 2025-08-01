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

def removeInPlace(nums, val):
    numP = nums
    numP[:] = list(filter(lambda item: item !=val, numP))

    for x in range(len(nums)-1, -1, -1):
            print(nums[x], nums)
            if nums[x] == val:
                nums.pop(x)
    print(f"lComp: {numP}, loop backward : {nums}")

from itertools import permutations
def findSubstring(s, words):
    # You are given a string s and an array of strings words. All the strings of words are of the same length.

    # A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

    # For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
    # Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
    res = []
    for i in range(len(words), len(words)+1):
        res.extend(list(permutations(words, i)))
    res[:] = ["".join(e) for e in res]
    idx2 = []
    for w in res:
         idx2.extend([i for i in range(len(s)) if s.startswith(w,i)])
    return list(set(idx2))
if __name__ == '__main__':
    print(reverseS( ["h","e","l","l","o"]))
    print(reverseInt(123), reverseInt(-123))
    print(findUnique('leetcode'))
    print(findNeedle('hello', "ll"))
    print(longestCommonPrefix(["flower","flow","flight"]))
    removeInPlace([0,1,2,2,3,0,4,2], 2)
    print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(findSubstring("foobarfoobar", ["foo","bar"]))