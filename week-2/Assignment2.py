""""Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. 
    Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: 
    Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as:
    Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  


    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            print("List is empty.")
            return
        if n <= 0:
            print("Invalid position.")
            return
        if n == 1:
            self.head = self.head.next  
            return

        current = self.head
        for i in range(n - 2):
            if not current.next:
                print("Position out of range.")
                return
            current = current.next

        if not current.next:
            print("Position out of range.")
            return

        current.next = current.next.next  

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original list:")
ll.print_list()

print("\nAfter deleting 2nd node:")
ll.delete_nth_node(2)
ll.print_list()

print("\nAfter deleting 1st node:")
ll.delete_nth_node(1)
ll.print_list()

