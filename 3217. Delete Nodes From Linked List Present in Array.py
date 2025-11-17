# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums, head):
        res = ListNode()
        current = res
        while head:
            if head.val in nums:
                head = head.next
                continue
            else:
                current.next = head
                current = head
                head = head.next
        return res.next

