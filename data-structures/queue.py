class Queue:
    def __init__(self) -> None:
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.pop(0)

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return not self.elements

    def sort(self, reverse_choice: bool = False):
        self.elements.sort(reverse=reverse_choice)

    def search(self, term):
        index = 0
        for _ in self.elements:
            if _ == term:
                print(f"{term} found at index: {index}")

            else:
                index += 1

    def __str__(self) -> str:

        queue_print = "Queue: "

        index = 0

        for _ in self.elements:

            if index == len(q) - 1:
                queue_print += str(_)

            else:
                queue_print += str(_) + " <- "
            index += 1

        return queue_print


# test suite

q = Queue()

q.enqueue("Celal")
q.enqueue("Aziz")
q.enqueue("Samet")

print(q)

q.sort()
print(q)

q.enqueue("Celal")
print(q)
q.search("Celal")

q.dequeue()
print(q)
