class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    def reverse(start, end):
        prev, curr = end, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    node = head
    count = 0
    while node and count != k:
        node = node.next
        count += 1
    if count == k:
        reversedHead = reverse(head, node)
        head.next = reverseKGroup(node, k)
        return reversedHead
    return head
