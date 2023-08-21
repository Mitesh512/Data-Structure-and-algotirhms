class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # The first Node in Linked list is known as head
        # starting point or the entry point to the linked list data structure
        self.head = None

    def append(self, value):
        new_node = Node(value)
        # print("Assigned ", value, " to new node")

        if self.head is None:
            # we are making the first Node as head
            self.head = new_node
        else:
            # print("Head value is ", self.head.value)
            current = self.head
            # print("Assigning Node with aove value to current_node")

            while current.next:
                # print(" in current .next if it exist")
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end= " --> ")
            current = current.next


# Reverse the linked lins
# Step 2: Function to reverse the linked list
def reverse_linked_list(head):
    prev_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next  # Save the next node to prevent losing it during reversal
        current_node.next = prev_node  # Reverse the link to the previous node
        prev_node = current_node
        current_node = next_node

    return prev_node 



if __name__ == "__main__":
    my_ll = LinkedList()
    my_ll.append(1)
    my_ll.append(2)
    my_ll.append(3)
    my_ll.append(4)
    my_ll.append(5)

    my_ll.display()

    print()


    reversed_ll = reverse_linked_list(my_ll.head)


    current = reversed_ll
    while current:
        print(current.value, end= " --> ")
        current = current.next
    print()

    