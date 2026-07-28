class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_key(self, key):
        new_node = Node(key)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display_linkedlist(self):
        current = self.head

        while current:
            print(current.key , end=" → ")
            current = current.next

        print("None")

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next