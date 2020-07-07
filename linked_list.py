class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_middle(self, new_data, start):
        new_node = Node(new_data)
        next_node = self.head

        while next_node.data != start:
            next_node = next_node.next
            if next_node is None:
                return print('The node is not present')
            
        new_node.next = next_node.next   
        next_node.next = new_node

    def remove_node(self, new_data):
        data = self.head
        
        # condition for first node removal
        if data is not None:
            if data.data == new_data:
                self.head = data.next
                data = None
                return

        while data is not None:
            if data.data == new_data:
                break

            prev = data
            data = data.next
        
        # condition for last node removal
        if data is None:
            return
            
        prev.next = data.next
        data = None
            
            

        
    def print_list(self):
        print_val = self.head

        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next

 
week_days = LinkedList()
week_days.head = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')

week_days.head.next = node2
node2.next = node3

print('Before insertion')
week_days.print_list()
print('After insertion (beginning)')
week_days.insert_beginning('Sun')
week_days.print_list()
print('After insertion (end)')
week_days.insert_end('Sat')
week_days.print_list()
print('After insertion (middle)')
week_days.insert_middle('Thu', 'Wed')
week_days.insert_middle('Fri', 'Thu')
week_days.print_list()
print('After removal')
week_days.remove_node('Thu')
week_days.remove_node('Fri')
week_days.remove_node('Sat')
week_days.remove_node('Sun')
week_days.print_list()
