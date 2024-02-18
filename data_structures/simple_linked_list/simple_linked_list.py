from typing import Optional
from node import Node


class List:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def list_size(self):
        return self.size

    def search(self, data):
        searcher_node = self.head

        while searcher_node is not None:
            if searcher_node.data == data:
                return True
            searcher_node = searcher_node.next_node
        return False

    def insert_head_node(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            new_head = Node(data)
            new_head.next_node = self.head
            self.head = new_head
        self.size += 1

    def insert_tail_node(self, data):
        new_tail = Node(data)

        if self.is_empty():
            self.head = self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self.size += 1

    def insert_node_by_position(self, position: int, data):
        if position > self.size or position < 1:
            return
        if position == 1:
            self.insert_head_node(data)
        else:
            current_node = self.head

            for i in range(1, position - 1):
                current_node = current_node.next_node

            new_node = Node(data, current_node.next_node)
            current_node.next_node = new_node
        self.size += 1

    def reset_list(self):
        self.head = self.tail = None
        self.size = 0

    def delete_head_node(self):
        if not self.is_empty():
            if self.size == 1:
                self.reset_list()
            else:
                self.head = self.head.next_node
            self.size -= 1

    def delete_tail_node(self):
        if not self.is_empty():
            if self.size == 1:
                self.reset_list()
            else:
                if self.size == 2:
                    self.head.next_node = None
                    self.head = self.tail
                else:
                    new_tail = self.head

                    for i in range(1, self.size - 1):
                        new_tail = new_tail.next_node
                    new_tail.next_node = None
                    self.tail = new_tail
            self.size -= 1

    def delete_node_by_position(self, position: int):
        if position > self.size or position < 1:
            return
        if position == 1:
            self.delete_head_node()
        elif position == self.size:
            self.delete_tail_node()
        else:
            previous_node = self.head

            for i in range(1, position - 1):
                previous_node = previous_node.next_node
            previous_node.next_node = previous_node.next_node.next_node
            self.size -= 1

    def delete_node_by_data(self, data):
        if self.is_empty():
            return

        current_node = self.head

        while current_node is not None:
            if current_node == self.tail:
                return
            if current_node.next_node.data == data:
                if current_node.next_node == self.tail:
                    current_node.next_node = None
                    self.tail = current_node
                else:
                    current_node.next_node = current_node.next_node.next_node
                self.size -= 1
                break
            current_node = current_node.next_node

    def print_list(self):
        if self.is_empty():
            return print("Empty list")
        if self.size == 1:
            return print(f"{self.head.data}")

        current_string = ""
        current_node = self.head

        while current_node is not None:
            current_string = f"{current_string}{current_node.data} -> "
            current_node = current_node.next_node
        return print(current_string)
