# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        self.size = 0
        while current_node:
            current_node = current_node.next
            self.size += 1

        if self.size == 1:
            return None
        elif self.size == n:
            head = head.next
            return head

        position = self.size - n + 1
        current_position = 1
        current_node = head
        while current_node:
            if current_position == position - 1:
                current_node.next = current_node.next.next
                return head
            current_node = current_node.next
            current_position += 1
