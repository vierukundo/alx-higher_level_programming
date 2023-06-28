#!/usr/bin/python3
# 100-singly_linked_list.py
"""Definition of node class"""


class Node:
    """represents singly linked list node"""
    def __init__(self, data, next_node=None):
        """Initialization of every instance of node
        args:
            data(int): an integer
            next_node(Node): class object
        raises:
            TypeError: If data is not an integer
            or next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """returns data"""
            return self.__data

        @data.setter
        def data(self, value):
            """sets data"""
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            """returns next_node"""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """sets the next_node"""
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = value


"""Definition of class SinglyLinkedList"""


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """Initialization
        args:
            head(obj): head object
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """this prints content of list"""
        output = ""
        current = self.__head
        while current.next_node is not None:
            output += str(current.data) + "\n"
            current = current.next_node
        output += str(current.data)
        return output
