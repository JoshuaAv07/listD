from node import DoubleNode as Node
from structure import Structure


class DoublyLinkedList(Structure):
    ''' Class that define a singly linked list '''

    def __init__(self):
        super().__init__()

    def append(self, data):
        node = Node(data)

        if self._tail == None:
            self._front = node

            if self._front != None:
                self._tail = node
            else:
                self._front.prev = node
                self._front = node
        else:
            self._tail.next = node
            self._tail = node
        
        self._size+=1

    def delete(self,data):
        current = self._front
        __next = self._front
        __prev = self._tail

        while current.next:
            if current.next.data == data:
                if current.next == self._tail:
                    current.next = None
                else:
                    __prev = current
                    __next = current.next.next
                    __prev.next = __next#

                self._size-=1
                return True
            else: 
                current = current.next

        return False

    def insertAfter(self, data, next_to, prev_to):
        if prev_to == None:
            print("Cannot be NULL")
            return

        new_node = Node(data)

        new_node.next = prev_to.next

        prev_to.next = new_node

        new_node.prev = prev_to

        if new_node.next:
            new_node.next.prev = new_node


    def insert(self, data , next_to, prev_to):
        current = self.search(next_to)
        current = self.search(prev_to)
        
        if current:
            new_node = Node(data)

            if current == self._tail:
                current.next = new_node

                if current == self._front:
                    current.prev = new_node
            
                else:
                    new_node.prev = current.prev
                    current.prev = new_node

            else:
                new_node.next = current.next
                current.next = new_node

            self._size += 1
        else:
            raise ValueError("Positional element is not in the list")

    def search(self,data):
        current = self._front

        while current:
            if current.data == data:
                return current
            else:
                current = current.next

        return False