class Info:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.start = None

    def empty(self):
        if self.start is None:
            print('Is empty')

    def push(self, data):
        new_data = Info(data)
        if self.start is None:
            self.start = new_data
            return
        current = self.start
        while current.next:
            current = current.next
        current.next = new_data

    def pop(self, index=None):
        if self.start is None:
            print("Stack is empty.")
            return None

        if index is None:
            index = self.peek()

        current = self.start
        if current.data == index:
            self.start = current.next
            return index

        prev = None
        while current:
            if current.data == index:
                break
            prev = current
            current = current.next

        if current is None:
            print("Element not found in the stack.")
            return None

        prev.next = current.next
        return index

    def peek(self):
        if self.start is None:
            print("Stack is empty.")
            return None

        current = self.start
        while current.next:
            current = current.next
        return current.data

    def display(self):
        if self.start is None:
            print("Stack is empty.")
            return []

        ls = []
        current = self.start
        while current:
            ls.append(current.data)
            current = current.next
        return ls


stack = Stack()
stack.push(213)
stack.push(215)
print(stack.peek())
print(stack.display())
