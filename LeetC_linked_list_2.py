# 876. Middle of the Linked List

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self):
        self.head = None # head variable which points to head of the linked list

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_end(self, data):
        # if linked list is empty
        if self.head is None:
            self.head = ListNode(data, None)
            return 
        # if linked list not empty iterate to the end of the linked list
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = ListNode(data, None)    

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.val) + '-->'
            itr = itr.next
        print(llstr)
        # print("Decimal Value: ", self.getDecimalValue2(self.head))

    def middleNode(self, head: ListNode) -> ListNode:
        mid = head
        while (head and head.next):
            mid = mid.next
            head = head.next.next
        return mid

    def middleNode2(self, head: ListNode) -> ListNode:
        # temp=head
        # c=0
        # while temp:
        #     temp=temp.next
        #     c+=1
        m=self.get_length()//2
        for i in range(m):
            head=head.next
        return head
    
    def print_from(self, head: ListNode):
        temp = head
        llstr = ''
        while temp:
            llstr += str(temp.val) + '-->'
            temp = temp.next
        print(llstr)
        


if __name__ == '__main__':
    ll = Solution()
    ll.insert_values([1,2,3])
    # ll.insert_values([1,0,0,1,0])
    # ll.middleNode2(ll.head)
    ll.print_from(ll.middleNode2(ll.head))
    # ll.print()
