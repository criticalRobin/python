from node import Node

class List:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def list_size(self):
        return self.size
    
    def search(self, data):
        if self.is_empty():
            return False
        
        searcher = self.head

        while searcher is not None:
            if searcher.data == data:
                return True
            searcher = searcher.next_node
        return False

    def insert_head_node(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            new_head = Node(data, self.head)
            self.head.previous_node = new_head
            self.head = new_head
        self.size += 1

    def insert_tail_node(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            new_tail = Node(data, None, self.tail)
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

            for i in range(1, position):
                current_node = current_node.next_node
            new_node = Node(data, current_node, current_node.previous_node)
            current_node.previous_node.next_node = new_node
            current_node.previous_node = new_node
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
                self.head.previous_node = None
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
                    self.tail = self.tail.previous_node
                    self.tail.next_node = None
                self.size -= 1

    def delete_node_by_position(self, position: int):
        if position > self.size or position < 1 or self.is_empty():
            return
        
        if position == 1:
            self.delete_head_node()
        elif position == 2:
            self.delete_tail_node()
        else:
            current_node = self.head

            for i in range(1, position):
                current_node = current_node.next_node
            current_node.next_node.previous_node = current_node.previous_node
            current_node.previous_node.next_node = current_node.next_node
            self.size -= 1

    def delete_node_by_data(self, data):
        if self.is_empty():
            return
        
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                if current_node == self.tail:
                    self.delete_tail_node()
                elif current_node == self.head:
                    self.delete_head_node()
                else:
                    current_node.next_node.previous_node = current_node.previous_node
                    current_node.previous_node.next_node = current_node.next_node
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
            current_string = f"{current_string}<- {current_node.data} -> "
            current_node = current_node.next_node
        return print(current_string)
