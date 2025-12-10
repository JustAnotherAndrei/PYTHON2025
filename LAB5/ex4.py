class DataStructure:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        raise NotImplementedError("Subclasses must implement pop().")

    def peek(self):
        raise NotImplementedError("Subclasses must implement peek().")

    def is_empty(self):
        return len(self._items) == 0


class Stack(DataStructure):
    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

class Queue(DataStructure):
    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]


if __name__ == "__main__":
    print("~~~~ Stack Example ~~~~")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop on empty:", s.pop())

    print("\n~~~~ Queue Example ~~~~")
    q = Queue()
    q.push("A")
    q.push("B")
    q.push("C")
    print("Peek:", q.peek())
    print("Pop:", q.pop())
    print("Pop:", q.pop())
    print("Pop:", q.pop())
    print("Pop on empty:", q.pop())
