class Node:
    def __init__(self, data: object, next_node = None, previous_node = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
