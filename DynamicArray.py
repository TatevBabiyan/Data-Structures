class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.arr = self.make_array(self.capacity)

    def is_empty(self):
        if self.n == 0:
            print("Is Empty")
            return

    def size(self):
        return self.n

    def shrink(self):
        if self.n < self.capacity // 4:
            new_sized = max(self.n // 2, 1)
            self.resize_arr(new_sized)

    def insert(self, pos, value):
        if self.n == self.capacity:
            self.resize_arr(2 * self.capacity)
        if pos <= self.n:
            for i in range(self.n, pos, -1):
                self.arr[i] = self.arr[i - 1]
        self.arr[pos] = value
        self.n += 1

    def remove(self, pos):
       if self.n == 0:
            raise IndexError("Can't pop from an empty array!")
       for i in range(pos, self.n-1):
            self.arr[i] = self.arr[i+1]
       self.n -= 1


    def push_back(self, value):
        if self.n == self.capacity:
            self.resize_arr(2 * self.capacity)
        self.arr[self.n] = value
        self.n += 1

    def pop_back(self):
        if self.n == 0:
            raise IndexError("Can't pop from an empty array!")
        self.n -= 1

    def push_front(self, value):
        if self.n == self.capacity:
            self.resize_arr(2 * self.capacity)
        for i in range(self.n, 0, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[0] = value
        self.n += 1

    def pop_front(self):
        if self.n == 0:
            raise IndexError("Can't pop from an empty array!")
        for i in range(1, self.n):
            self.arr[i - 1] = self.arr[i]
        self.n -= 1

    def resize_arr(self, new_capacity):
        new_arr = self.make_array(new_capacity)
        for i in range(self.n):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def make_array(self, capacity):
        return [None] * capacity

    def display(self):
        return self.arr[:self.n]



dyn_array = DynamicArray()
dyn_array.is_empty()
dyn_array.push_back(1)
dyn_array.push_back(2)
dyn_array.push_back(3)
dyn_array.push_back(23)
dyn_array.push_back(12)
dyn_array.insert(2, 1123)
print(dyn_array.display())
dyn_array.remove(3)
print(dyn_array.display())

