"""
19. 删除链表的倒数第 N 个结点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    链表问题考虑使用dummy_node作为头节点，可以避免一些特殊情况的判断
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        list记录链表元素，遍历一遍后确定需要删除的元素位置
        时间复杂度O(n)，空间复杂度O(n)
        """
        dummy_node = ListNode(0, head)
        cur = dummy_node
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next
        l = len(stack)
        index = l - n
        if index == l - 1:
            stack[index - 1].next = None
        else:
            stack[index - 1].next = stack[index + 1]
        return dummy_node.next

    def removeNthFromEnd_doubleIndex(self, head: ListNode, n: int) -> ListNode:
        """
        使用两个指针first和second同时对链表进行遍历，并且first比second超前n个节点。
        当first遍历到链表的末尾时，second就恰好处于倒数第n个节点。
        时间复杂度O(n)，空间复杂度O(1)
        """
        dummy_node = ListNode(0, head)
        first, second = dummy_node, dummy_node
        gap = 0
        while first.next:
            if gap < n:
                first = first.next
                gap += 1
            else:
                first = first.next
                second = second.next
        second.next = second.next.next
        return dummy_node.next

if __name__ == '__main__':
    solution = Solution()
    v5 = ListNode(5)
    v4 = ListNode(4, v5)
    v3 = ListNode(3, v4)
    v2 = ListNode(2, v3)
    v1 = ListNode(1, v2)
    head = solution.removeNthFromEnd_doubleIndex(v1, 2)
    while head:
        print(head.val)
        head = head.next
