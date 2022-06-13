# 1290. Convert Binary Number in a Linked List to Integer

'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.


Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0

Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        self.head = None # head variable which points to head of the linked list

    def getDecimalValue(self, head: ListNode) -> int:
        base_ten = 0
        bin_list = ''
        iter = head
        while iter:
            bin_list += str(iter.val)
            iter = iter.next
        exp = 0
        for i in range(len(bin_list)-1,-1,-1):
            base_ten = base_ten + int(bin_list[i]) * (2**exp)
            exp +=1
        return base_ten
    
    def getDecimalValue2(self, head: ListNode) -> int:
        res=[]
        while head: #Iterate over the linked list using while loop
            res.append(str(head.val))
            head=head.next
        x=''.join(res)  #The join() method takes all items in an iterable and joins them into one string.
        return int(x,2)  #convert binary to decimal
    
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
        print("Binary representation", llstr)
        print("Decimal Value: ", self.getDecimalValue2(self.head))


if __name__ == '__main__':
    ll = Solution()
    ll.insert_values([1,0,1])
    # ll.insert_values([1,0,0,1,0])
    ll.getDecimalValue(ll.head)
    ll.print()


