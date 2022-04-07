'''Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40'''

#class for holding the data, defaults to empty node if no data is given
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None #pointer to the next node

# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1 #always update the size to prevent costly iterations to get the size

    #defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''
    Exercise Part 1,2 and 3:

    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values
    '''

    def clear(self):
        return

    def get_data(self, data):
        return

    def delete(self, data):
        return


    '''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).
    '''

class NodeDLL:
    '''Implement your node for the doubly linked list here'''

class DoublyLinkedList:
    '''Implement your code for the doubly linked list here'''


    '''Exercise Part 5 and 6:
    Complete the classes below to implement a stack and queue data structure. You are free to use built-in
    methods but you have to complete all methods below. Always return the correct data type according
    to the exercise sheet'''

class MyStack:

    def push(self, element):
        return

    def pop(self):
        return

    def top(self):
        return

    def size(self):
        return


class MyQueue:

    def push(self,element):
        return

    def pop(self):
        return

    def show_left(self):
        return

    def show_right(self):
        return

    def size(self):
        return