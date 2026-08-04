class Node:
    """Store a value and a reference to the next node in a linked list."""

    def __init__(self, key):
        """Create a node containing key."""

        self.key = key
        self.next = None


class SLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Create an empty linked list."""

        self.head = None

    def add_key(self, key):
        """Append key to the end of the list."""

        new_node = Node(key)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display_linkedlist(self):
        """Print the values in the list from head to tail."""

        current = self.head

        while current:
            print(current.key, end=" → ")
            current = current.next

        print("None")

    def delete_last(self):
        """Remove the final node from the list if one exists."""

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
        """Remove the first node from the list if one exists."""

        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next