""""Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. 
    Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: 
    Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as:
    Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth(self, n):
        try:
            if self.head is None:
                raise IndexError("Empty List")

            if n <= 0:
                raise ValueError("Invalid index")

            if n == 1:
                print(f"Deleting node: {self.head.data}")
                self.head = self.head.next
                return

            temp = self.head
            for i in range(n - 2):
                if temp.next is None:
                    raise IndexError("Index out of range")
                temp = temp.next

            if temp.next is None:
                raise IndexError("Index out of range")

            print(f"Deleting node: {temp.next.data}")
            temp.next = temp.next.next

        except (IndexError, ValueError) as e:
            print("Error:", e)



ll = LinkedList()
ll.append(34)
ll.append(12)
ll.append(9)
ll.print_list()  


ll.delete_nth(2) 
ll.print_list()  
ll.delete_nth(10) 
empty_ll = LinkedList()
empty_ll.delete_nth(1)  
