class Stack:
    def __init__(self) -> None:
        self.items = []
        self.max_size = 8

    def push(self, item) -> None:
        if not len(self.items) == self.max_size:
            self.items.append(item)

    def pop(self) -> None:
        if len(self.items):
            return self.items.pop()
        return None

    def peek(self):
        """View the top element without removing it"""
        if len(self.items):
            return self.items[-1]
        else:
            return None

    def is_empty(self) -> bool:
        if not len(self.items):
            return True
        else:
            return False

    def is_full(self):
        if len(self.items) == self.max_size:
            return True
        else:
            return False
