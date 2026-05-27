from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        second_half_head = slow_pointer.next
        slow_pointer.next = None

        # reversing the second half
        current = second_half_head
        prev = None
        while current:
            next_nodes = current.next
            current.next = prev
            prev = current
            current = next_nodes

        rev_second_half = prev
        first_half = head

        # Merge intervals
        while rev_second_half:
            first_half_next = first_half.next
            second_half_next = rev_second_half.next

            first_half.next = rev_second_half
            rev_second_half.next = first_half_next

            first_half = first_half_next
            rev_second_half = second_half_next

