__author__ = 'hamed1soleimani'


class DualNode:
    def __init__(self, p, e, n):
        self.prev = p
        self.element = e
        self.next = n

    def __str__(self):
        return str(self.element)


class Node:
    def __init__(self, e, n):
        self.element = e
        self.next = n

    def __str__(self):
        return str(self.element)


class DualLinkedList:

    def __init__(self):
        self.current = self.head = self.tail = None
        self.size = 0

    def push_front(self, e):
        if self.size == 0:
            self.head = self.tail = DualNode(None, e, None)
            self.size = 1
        else:
            self.head = DualNode(None, e, self.head)
            self.head.next.prev = self.head
            self.size += 1

    def push_back(self, e):
        if self.size == 0:
            self.push_front(e)
        else:
            self.tail = DualNode(self.tail, e, None)
            self.tail.prev.next = self.tail
            self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.size -= 1
            return temp.element

    def pop_back(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.size -= 1
            return temp.element

    def insert(self, i, e):
        if i < 0 or i > self.size:
            raise IndexError('index out of bound!')
        temp = None
        if self.size == 0 or i == 0:
            self.push_front(e)
        elif i == self.size:
            self.push_back(e)
        elif i > self.size // 2:
            j = self.size - 1
            temp = self.tail
            while j != i:
                temp = temp.prev
                j -= 1
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
            elem = DualNode(temp.prev, e, temp)
            elem.prev.next = elem
            elem.next.prev = elem

    def delete(self, i):
        if self.size == 0:
            raise IndexError('list is empty!')
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if i == 0:
            return self.pop_front()
        elif i == self.size - 1:
            return self.pop_back()
        elif i > self.size // 2:
            j = self.size - 1
            temp = self.tail
            while j != i - 1:
                temp = temp.prev
                j -= 1
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = temp.next = None
        self.size -= 1
        return temp.element

    def remove(self, e):
        if self.size == 0:
            raise IndexError('list is empty!')
        if e is self.head.element:
            return self.pop_front()
        elif e is self.tail.element:
            return self.pop_back()
        else:
            x = self.head
            while not x is self.tail:
                x = x.next
                if e is x.element:
                    x.prev.next = x.next
                    x.next.prev = x.prev
                    x.next = x.prev = None
                    self.size -= 1
                    return
        raise KeyError('not found!')

    def get_front(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            return self.head.element

    def get_back(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            return self.tail.element

    def get(self, i):
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if self.size == 0:
            raise IndexError('list is empty!')
        if i == 0:
            return self.get_front()
        elif i == self.size - 1:
            return self.get_back()
        elif i > self.size // 2:
            j = self.size - 1
            temp = self.tail
            while j != i:
                temp = temp.prev
                j -= 1
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
        return temp.element

    def set(self, i, e):
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if self.size == 0:
            raise IndexError('list is empty!')
        elif i > self.size // 2:
            j = self.size - 1
            temp = self.tail
            while j != i:
                temp = temp.prev
                j -= 1
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
        temp.element = e

    def find(self, e):
        if self.size == 0:
            raise IndexError('list is empty!')
        if e is self.head.element:
            return 0
        if e is self.tail.element:
            return self.size - 1
        temp = self.head.next
        i = 0
        while not temp is None:
            if e is temp.element:
                return i
            temp = temp.next
            i += 1
        raise KeyError('not found!')

    def clear(self):
        if self.size != 0:
            temp = self.head
            temp1 = temp.next
            while not temp1 is None:
                temp.next = temp.prev = temp.element = None
                temp = temp1
                temp1 = temp1.next
            self.size = 0
        self.head = self.tail = None

    def __str__(self):
        if self.size == 0:
            return '[]'
        else:
            output = '['
            temp = self.head
            while not temp is None:
                output += (str(temp.element) + ', ')
                temp = temp.next
            output = output[:-2]
            output += ']'
            return output

    def __getitem__(self, item):
        if item > 0:
            return self.get(item)
        else:
            return self.get(item + len(self))

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __bool__(self):
        return self.size != 0

    def __contains__(self, item):
        try:
            self.find(item)
            return True
        except KeyError:
            return False
        except IndexError:
            return False

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.element
        self.current = self.current.next
        return data

    def __add__(self, other):
        assert isinstance(other, DualLinkedList)
        for o in other:
            self.push_back(o.element)

    def __eq__(self, other):
        assert isinstance(other, DualLinkedList)
        if len(self) != len(other):
            return False
        for i in range(len(other)):
            if not self[i] is other[i]:
                return False
        return True


class LinkedList:

    def __init__(self, circular=False):
        self.circular = circular
        self.current = self.head = self.tail = None
        self.size = 0

    def push_front(self, e):
        if self.size == 0:
            self.head = self.tail = Node(e, None)
            self.size = 1
        else:
            temp = Node(e, self.head)
            self.head = temp
            self.size += 1
        if self.circular:
            self.tail.next = self.head

    def push_back(self, e):
        if self.size == 0:
            self.head = self.tail = Node(e, None)
            self.size = 1
        else:
            temp = Node(e, None)
            self.tail.next = temp
            self.tail = temp
            self.size += 1
        if self.circular:
            self.tail.next = self.head

    def pop_front(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            if self.circular:
                self.tail.next = self.head
            self.size -= 1
            return temp.element

    def insert(self, i, e):
        if i < 0 or i > self.size:
            raise IndexError('index out of bound!')

        temp0 = None
        if self.size == 0 or i == 0:
            self.push_front(e)
        else:
            j = 0
            temp = self.head
            while j != i:
                temp0 = temp
                temp = temp.next
                j += 1
            elem = Node(e, temp)
            temp0.next = elem
        if self.circular:
            self.tail.next = self.head

    def delete(self, i):
        if self.circular:
            i %= len(self)
        if self.size == 0:
            raise IndexError('list is empty!')
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if i == 0:
            return self.pop_front()
        else:
            j = 0
            temp = self.head
            while j != i:
                temp0 = temp
                temp = temp.next
                j += 1
            temp0.next = temp.next
            temp.next = None
            self.size -= 1
            if i == len(self):
                self.tail = temp0
            if self.circular:
                self.tail.next = self.head
            return temp.element

    def remove(self, e):
        if self.size == 0:
            raise IndexError('list is empty!')
        if e is self.head.element:
            return self.pop_front()
        else:
            x = self.head
            while not x.next is None:
                y = x
                x = x.next
                if e is x.element:
                    y.next = x.next
                    x.next = None
                    self.size -= 1
                    if self.circular:
                        self.tail.next = self.head
                    return
        raise KeyError('not found!')

    def get_front(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            return self.head.element

    def get_back(self):
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            return self.tail.element

    def get(self, i):
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if self.size == 0:
            raise IndexError('list is empty!')
        if i == 0:
            return self.get_front()
        elif i == self.size - 1:
            return self.get_back()
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
        return temp.element

    def set(self, i, e):
        if i < 0 or i > self.size - 1:
            raise IndexError('index out of bound!')
        if self.size == 0:
            raise IndexError('list is empty!')
        else:
            j = 0
            temp = self.head
            while j != i:
                temp = temp.next
                j += 1
        temp.element = e

    def find(self, e):
        if self.size == 0:
            raise IndexError('list is empty!')
        if e is self.head.element:
            return 0
        if e is self.tail.element:
            return self.size - 1
        temp = self.head.next
        i = 0
        while not temp is None:
            if e is temp.element:
                return i
            temp = temp.next
            i += 1
        raise KeyError('not found!')

    def clear(self):
        if self.size != 0:
            temp = self.head
            temp1 = temp.next
            while not temp1 is None:
                temp.next = temp.element = None
                temp = temp1
                temp1 = temp1.next
            self.size = 0
        self.head = self.tail = None

    def __str__(self):
        if self.size == 0:
            return '[]'
        else:
            output = '['
            temp = self.head
            while not temp is self.tail:
                output += (str(temp.element) + ', ')
                temp = temp.next
            output += (str(self.tail.element) + ', ')
            output = output[:-2]
            output += ']'
            return output

    def __getitem__(self, item):
        if item > 0:
            if not self.circular:
                return self.get(item)
            else:
                return self.get(item % len(self))
        else:
            return self.get(item + len(self))

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __bool__(self):
        return self.size != 0

    def __contains__(self, item):
        try:
            self.find(item)
            return True
        except KeyError:
            return False
        except IndexError:
            return False

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.element
        self.current = self.current.next
        return data

    def __add__(self, other):
        assert isinstance(other, DualLinkedList)
        for o in other:
            self.push_back(o.element)

    def __eq__(self, other):
        assert isinstance(other, DualLinkedList)
        if len(self) != len(other):
            return False
        for i in range(len(other)):
            if not self[i] is other[i]:
                return False
        return True
