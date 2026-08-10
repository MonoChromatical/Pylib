class _Node:
    def __init__(self, data):
        self.data = data
        self.next: _Node | None = None
        self.prev: _Node | None = None

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def add_data(self, data):
        new_node = _Node(data)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            return

        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node
