Here's the code to solve the given problem statement:

```
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            sum += carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
        return dummy.next
```

This code creates a dummy node, initializes a current node to the dummy node, and initializes a carry variable to 0. Then, it loops through both linked lists and adds the values of the nodes at the corresponding positions along with the carry value. It then calculates the carry value for the next addition and creates a new node with the sum modulo 10. Finally, it advances the current node and returns the next node after the dummy node.