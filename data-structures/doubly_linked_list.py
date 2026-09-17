from typing import Literal


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node

    def display(self, options: Literal["forward", "back"]):
        if options == "back":
            current = self.tail
            while current:
                print(current.data)
                current = current.prev
        if options == "forward":
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def delete(self, key):
        if self.head == None and self.tail == None:
            print("List is empty.")
            return
        elif self.head.data == key and self.tail.data == key:
            self.tail = None
            self.head = None
        elif self.head.data == key and self.tail.data != key:
            self.head.next.prev = None
            self.head = self.head.next
        elif self.tail.data == key and self.head.data != key:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            current = self.head
            while current:
                if current.data == key:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    break
                else:
                    current = current.next
