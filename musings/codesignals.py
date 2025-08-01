

import string

lowercase_alphabet = string.ascii_lowercase
uppercase_alphabet = string.ascii_uppercase

# lowercase_alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
# uppercase_alphabet = ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))

def char_shift(s):
    r = ''
    for c in range(len(s)):

        if s[c] in lowercase_alphabet:
            char_idx = lowercase_alphabet.index(s[c])
            if char_idx == 25:
                r += 'a'
            else:
                r += lowercase_alphabet[char_idx + 1]
        elif s[c] in uppercase_alphabet:
            char_idx = uppercase_alphabet.index(s[c])
            if char_idx == 25:
                 r += 'A'
            else:
                 r += uppercase_alphabet[char_idx + 1]
             
        else:
             r += s[c]
    print(r)
    print("".join(chr(ord(i)+1) if i.isalpha() else i for i in s))

def swapCase(s):
    #return s.swapcase()
    r = ''
    for c in range(len(s)):
        ch = s[c]
        if ch in lowercase_alphabet:
            r += uppercase_alphabet[lowercase_alphabet.index(ch)]
        elif ch in uppercase_alphabet:
            r += lowercase_alphabet[uppercase_alphabet.index(ch)]   
        else:
             r += ch
    print(r)
    x = lambda c: chr(ord(c)-32) if ord(c)>=97 else chr(ord(c)+32)
    e = "".join(x(c) if c.isalpha() else c for c in s)
    print(e)
    
import re
def palindrome(s):
    # TODO: Implement the function to check whether the provided string is a palindrome or not; ignore case and punction
    text = re.sub(r'[\W+]', '', s)
    print( text.lower() == text[::-1].lower())
    
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    found = {}
    for i, d in enumerate(nums):
        print(f'current hash: {found}')
        c = target - d
        print(f'looking for {c} for index {i}, value {d}')
        if c in found:
            print(f'we\'ve seen {c} at index {found[c]}')
            return [found[c], i]
        found[d] = i
    return []

def longest_non_rpt_subs(s):
    subs = []
    c = ''
    curr_max = 0
    for i in range(len(s)):
        # find all substrings
        for j in range(i, len(s)):
            # meet requirement of non repeating?
            if s[j-1] != s[j]:
               subs.append(s[i:j+1])
               curr_max = max(subs, key=len)
               if len(s[i:j+1]) >= curr_max:
                   c = s[i:j+1]
               
    print(f'max length, {curr_max}, subs: {c}')

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

def mergeTwoLists(list1, list2):
        #list1: Optional[ListNode], list2: Optional[ListNode]
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append remaining nodes from either list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next
    
if __name__ == '__main__':
 
    s = 'Hello, Zoe!'
    char_shift(s)
    palindrome('raceCar')
    palindrome("A man, a plan, a canal: Panama")
    palindrome('world')
    swapCase(s)
    # # print('Solution', twoSum(nums = [2,7,11,15], target = 9))
    # # print('Solution',twoSum(nums = [3,2,4], target = 6))
    # # print('Solution',twoSum(nums = [3,3], target = 6))
    # longest_non_rpt_subs('abcabcbb')
    
    
    node1_l1 = ListNode(2)
    node2_l1 = ListNode(4)
    node3_l1 = ListNode(3)

    # Link the nodes for l1
    node1_l1.next = node2_l1
    node2_l1.next = node3_l1

    # The head of l1 is node1_l1
    l1 = node1_l1

    node1_l2 = ListNode(5)
    node2_l2 = ListNode(6)
    node3_l2 = ListNode(4)

    # Link the nodes for l1
    node1_l2.next = node2_l2
    node2_l2.next = node3_l2

    # The head of l1 is node1_l1
    l2 = node1_l2
    addTwoNumbers(l1,l2)
    x = addTwoNumbers(l1,l2)
    print (x.val)
    while x.next: 
        x = x.next
        print(x.val)
    print('------')
    node1_l1 = ListNode(1)
    node2_l1 = ListNode(3)
    node3_l1 = ListNode(4)

    # Link the nodes for l1
    node1_l1.next = node2_l1
    node2_l1.next = node3_l1

    # The head of l1 is node1_l1
    l1 = node1_l1

    node1_l2 = ListNode(1)
    node2_l2 = ListNode(2)
    node3_l2 = ListNode(4)

    # Link the nodes for l1
    node1_l2.next = node2_l2
    node2_l2.next = node3_l2

    # The head of l1 is node1_l1
    l2 = node1_l2
    x =  mergeTwoLists(l1, l2)
    print (x.val)
    while x.next: 
        x = x.next
        print(x.val)