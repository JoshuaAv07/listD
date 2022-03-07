class Node:

    def __init__(self, data):
        self.data = data


class ListNode(Node):

    def __init__(self,data,next=None):
        super().__init__(data)
        self.next = next
        
class DoubleNode(Node):

    def __init__(self,data,next=None,prev=None):
        super().__init__(data)
        self.next = next
        self.prev = prev