class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        s = ""
        for _ in range(self._size):
            s += "🍪"
        return s

    def deposit(self, n):
        if n + self._size > self._capacity or n < 0:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self._size or n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
