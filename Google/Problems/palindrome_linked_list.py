"""
Given the head of a singly linked list, return true if it is a palindrome.

EX: 
Input: head = [1,2,2,1]
Output: true
"""

# This is kind of the cheater way to do it for creating an array
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        left, right = 0, len(nums) - 1
        while right <= left:
            if numms[right] != nums[left]:
                return False
        return True
