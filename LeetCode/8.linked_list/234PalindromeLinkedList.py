# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = collections.deque();
            
        if not head:
            return True;
        
        linked_list = head;
        
        while linked_list is not None:
            q.append(linked_list.val);
            linked_list = linked_list.next;
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False;
        
        return True;