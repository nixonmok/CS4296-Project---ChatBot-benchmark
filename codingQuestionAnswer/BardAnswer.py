Sure, here is the code to finish the function `addTwoNumbers()` in Python3:

```python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the result linked list
        result = ListNode()
        carry = 0

        # Traverse the two linked lists simultaneously
        while l1 is not None or l2 is not None:
            # Get the current digits from the two linked lists
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            # Add the current digits and carry
            sum = x + y + carry

            # Update the carry
            carry = sum // 10

            # Create a new node for the result linked list
            new_node = ListNode(sum % 10)
            new_node.next = result
            result = new_node

            # Move on to the next nodes in the two linked lists
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # If there is still a carry, create a new node for it
        if carry > 0:
            new_node = ListNode(carry)
            new_node.next = result
            result = new_node

        return result
```