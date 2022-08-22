class node:
    def __init__(self, data=None):
        self.data = data  # Storing past data point
        self.next = None  # Storing pointer to the next node "constructor


class linked_list:
    def __init__(self):
        self.head = node()  # constructor, head node place-holder to allow us to point to the first list

    def append(self, data):  # append function adds an item to the end of the list
        new_node = node(data)
        cur = self.head # current node
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self): # how large data structure is
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_indx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_indx == index: return cur_node.data
            cur_indx += 1

    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
        cur_indx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_indx == index:
                last_node.next = cur_node.next
                return
            cur_indx += 1


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.display()
my_list.erase(2)
my_list.display()
#print("Elments at 2nd index: ", my_list.get(2))
