# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        x=ListNode()
        m=x

        #compare 1 from list 1 and 1 from list 2 
        # put min in the linked list 
        # again compare next in the list to the current pointer 
        while head1 and head2:            
            if head1.val>head2.val:
                x.next=head2
                x=x.next
                head2=head2.next
            else:
                x.next=head1
                x=x.next
                head1=head1.next
        if head1:
            x.next=head1
        if head2:
            x.next=head2
        return m.next

            

            


        