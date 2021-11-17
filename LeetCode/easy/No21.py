# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class No21:
    def mergeTwoLists_iteration(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        利用一个虚拟的头节点，同时循环两个链表，将值小的接在当前链表后面。
        利用一个虚拟头节点可以避免处理真正头节点的麻烦，最后virtual_node.next即可。
        最后有一个链表为空以后，只需要将不为空的链表接在后面。
        时间复杂度：O(n+m)，空间复杂度：O(1)
        """
        virtual_head = ListNode()
        pre_node = virtual_head
        while l1 and l2:
            if l1.val <= l2.val:
                pre_node.next = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                l2 = l2.next
            pre_node = pre_node.next
        pre_node.next = l1 if l1 else l2
        return virtual_head.next

    def mergeTwoLists_recursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        利用循环的方式从前往后拼接较为麻烦的是最后获取到头节点，
        采用递归的方式从后往前赋值，最后拿到的即头节点。
        时间复杂度：O(n+m)，空间复杂度：O(n+m)
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_recursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recursion(l1, l2.next)
            return l2


if __name__ == '__main__':
    no21 = No21()
    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(4)
    x1.next = x2
    x2.next = x3
    y1 = ListNode(1)
    y2 = ListNode(3)
    y3 = ListNode(4)
    y1.next = y2
    y2.next = y3
    merge = no21.mergeTwoLists_recursion(x1, y1)
    while merge:
        print(merge.val)
        merge = merge.next
