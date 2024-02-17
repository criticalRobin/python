from typing import Optional
from node import Node

class List:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self):
        return self.head == None
    
    def list_size(self):
        return self.size
    
    def search(self, data):
        searcher_node = self.head

        while(searcher_node != None):
            if(searcher_node.data == data):
                return True
            searcher_node = searcher_node.next_node
        return False