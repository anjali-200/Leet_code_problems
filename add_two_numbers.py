# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) ->[ListNode]:
        head = ListNode(0)
        root = head
        carry = 0 

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return root.next  
# Helper function to create linked list from list
# and to print linked list as list for easy verification
# of the result
# Converts a list to a linked list
# Input: [2,4,3]
# Output: 2 -> 4 -> 3
#  Converts a linked list to a list
# Input: 7 -> 0 -> 8
# Output: [7,0,8]
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
def list_to_linkedlist(lst):      
    head = ListNode(0)
    current = head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return head.next

# Expected Result: 7 -> 0 -> 8
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])

sol = Solution()
result_node = sol.addTwoNumbers(l1, l2)

print(f"Resulting List: {linkedlist_to_list(result_node)}")