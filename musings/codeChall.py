def longestPalindrome(s):
        # given a string find longest palindrome
        
        # 110 % pythonic:
        # subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        substrings = []
        l = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                # substrings.append(s[i:j+1])
                t = s[i:j+1]
                if t == t[::-1] and len(t) > l:
                    substrings.append(t)
                    l = len(t)
        return max(substrings, key=len)


# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

#def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
 
# input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
import math
def kClosest(points, k):
        dist = []
        e = lambda a,b : (a-b)**2
        o = lambda a,b : math.sqrt(e(a,0) + e(b,0))
        
        for x,y in points:
            d = o(x,y)
            dist.append([d, [x,y]])
        dist.sort()
        return [d[1] for d in dist[:k]]
if __name__ == '__main__':
     print(longestPalindrome("babad"))
     print(kClosest([[1,3],[-2,2]], 1))
     print(kClosest([[3,3],[5,-1],[-2,4]], 2))