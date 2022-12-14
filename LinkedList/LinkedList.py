class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def print(self):
        cur_node = self.head
        output = ''
        while cur_node is not None:
            output += str(cur_node.get_data()) + '--->'
            cur_node = cur_node.get_next()

        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_last(self):
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_first(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.remove_first()
                return
            elif count + 1 == index:
                node_remove = cur_node.get_next()
                node_after_removing = node_remove.get_next()
                cur_node.set_next(node_after_removing)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range')

    def reverse(self):
        cur_node = self.head
        prev = None
        next = None
        while cur_node is not None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev
