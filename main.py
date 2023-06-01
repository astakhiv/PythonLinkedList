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

    def insert(self, index: int, value):
        item = self.__getitem__(index)
        item.val, item.next = value, Node(item.val, item.next)

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return self.head

        item = self.__getitem__(index)
        self[index-1].next = item.next
        return self.head

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        key = 0
        for item in self:
            if key == index:
                return item
            key += 1

    def __setitem__(self, index, value):
        key = 0
        for item in self:
            if key == index:
                item.val = value
                break
            key += 1

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
