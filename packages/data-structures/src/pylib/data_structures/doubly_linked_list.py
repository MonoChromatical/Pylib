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
