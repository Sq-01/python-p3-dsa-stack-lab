class Stack:

    def __init__(self, items = None,  max_size=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.max_size = max_size

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.max_size is not None and self.size() == self.max_size

    def search(self, target):
        for index, item in enumerate(self.items):
            if item == target:
                return self.size() - 1 - index
        return -1
