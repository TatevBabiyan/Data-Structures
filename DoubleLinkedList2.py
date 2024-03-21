class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            print("Empty!")
            return

    def push_front(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        new_data.next = self.head
        self.head.prev = new_data
        self.head = new_data

    def push_back(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        current = self.head
        while current.next:
            current = current.next
        new_data.prev = current
        current.next = new_data

    def pop_back(self):
        if self.head is None:
            raise IndexError("Empty!")
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def pop_front(self):
        if self.head is None:
            raise IndexError("Empty!")
        current = self.head
        self.head = self.head.next
        current.next = None


    def insert(self, pos, data):
        if isinstance(data, list):
            for i in data:
                return self.insert(pos, i)
        new_data = Node(data)
        if pos == 0:
            new_data.next = self.head
            self.head = new_data
            return

        if self.head is None:
            self.head = new_data
            return
        current = self.head
        count = 0
        while current:
            if count == pos-1:
                new_data.next = current.next
                new_data.prev = current
                current.next = new_data
                return
            current = current.next
            count += 1

    def remove(self, data):
        if self.head is None:
            raise IndexError("Empty!")
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current:
            if current.data == data:
                current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next


    def display(self):
        ls = []
        current = self.head
        while current:
            ls.append(current.data)
            current = current.next
        return ls

dll = DLL()
dll.push_front(123)
dll.push_front(12)
dll.push_front(4)
dll.push_back(1123)
print(dll.display())
dll.remove(4)
print(dll.display())
