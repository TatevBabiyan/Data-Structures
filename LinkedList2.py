class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.arr = []

    def is_empty(self):
        if self.head is None:
            print('Is empty: ')
            return

    def push_front(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        new_data.next = self.head
        self.head = new_data

    def push_back(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        current = self.head
        while current.next:
            current = current.next
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
        tmp = self.head
        self.head = self.head.next
        tmp.next = None


    def insert(self, pos, data):
        if isinstance(data, list):
            for i in data:
                self.insert(pos, i)
            return
        new_data = Node(data)
        if pos == 0:
            new_data.next = self.head
            self.head = new_data
            return

        current = self.head
        count = 0
        while current:
            if count == pos-1:
                new_data.next = current.next
                current.next = new_data
                return
            current = current.next
            count += 1


    def search(self,data):
        if self.head is None:
            raise IndexError("Doesnt exist")
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


    def display(self):
        current = self.head
        while current:
            self.arr.append(current.data)
            current = current.next
        return self.arr


obj = LinkedList()
obj.push_front(32)
obj.push_front(12)
obj.push_back(1213)
obj.push_back(3)
obj.insert(1, 1312)
print(obj.search(3))
print(obj.display())
