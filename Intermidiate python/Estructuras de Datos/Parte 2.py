class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def push_right(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("Deque vacío")
            return None

        removed_data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return removed_data

    def pop_right(self):
        if self.head is None:
            print("Deque vacío")
            return None

        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data

        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        removed_data = self.tail.data
        self.tail = current_node
        self.tail.next = None

        return removed_data

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

deque = Deque()

deque.push_left("B")
deque.push_left("A")
deque.push_right("C")
deque.push_right("D")

deque.print_structure()