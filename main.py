class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, vals):
        self.len = len(vals)
        vals[len(vals) - 1] = Node(vals[len(vals) - 1])
        for i in range(len(vals) - 1, 0, -1):
            vals[i-1] = Node(vals[i-1])
            vals[i-1].next = vals[i]
        self.head = vals[0]

    def insert(self, key: int, value):
        index = 0
        for item in self:
            if index == key:
                item.val, item.next = value, Node(item.val, item.next)
                break
            index += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return self.head
        i = 0
        for item in self:
            if i == index:
                self[i-1].next = item.next
            i += 1
        return self.head

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        index = 0
        for i in self:
            if index == item:
                return i
            index += 1

    def __setitem__(self, key, value):
        index = 0
        for i in self:
            if index == key:
                i.val = value
                break
            index += 1

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        node = self.node
        if self.node is not None:
            self.node = self.node.next
            return node
        else:
            raise StopIteration

