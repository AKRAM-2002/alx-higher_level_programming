class Node:
    """
    Class Node that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node with the given data and an optional reference to the next node.

        :param data: The data to be stored in the node.
        :param next_node: A reference to the next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        :return: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        :param value: The new data to be stored in the node (must be an integer).
        :raises TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Get a reference to the next node in the linked list.

        :return: A reference to the next node, or None if it's the end of the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set a reference to the next node in the linked list.

        :param value: A reference to the next node (must be a Node object or None).
        :raises TypeError: If the provided value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object or None')
        self.__next_node = value


class SinglyLinkedList():
    """
    Implementation of a singly-linked list using Python classes.
    """

    def __init__(self):

        """
        Initialize a new empty singly-linked list.
        """
        self.__head = None

    
    def sorted_insert(self, value):
        """
        Insert a new node into the linked list while maintaining its order based on the data values.
        :param value: The data for the new node.
        """
        # Create a new node with the given data
        new_node = Node(value)
        # Special case when inserting at head
        if self.__head is None:
            new_node.next_node = None
            self.__head =  new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            current_node = self.__head
            while (current_node.next_node is not None and current_node.next_node.data < value):
                current_node = current_node.next_node
            
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

       
    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
            return ('\n'.join(values))
            

            

