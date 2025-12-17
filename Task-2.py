class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node to the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        """Print all elements in the list"""
        if not self.head:
            print("List is empty.")
            return

        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index should be a positive integer (1-based).")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(n - 2):
            if not curr.next:
                raise IndexError("Index out of range.")
            curr = curr.next

        if not curr.next:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {curr.next.data}")
        curr.next = curr.next.next


# === Sample Test ===
if __name__ == "__main__":
    ll = LinkedList()

    # Add sample nodes
    for val in [10, 20, 30, 40, 50]:
        ll.append(val)

    print("Original list:")
    ll.print_list()

    try:
        ll.delete_nth_node(3)
        print("After deleting 3rd node:")
        ll.print_list()

        ll.delete_nth_node(1)
        print("After deleting 1st node:")
        ll.print_list()

        ll.delete_nth_node(10)  # This should raise an error
    except Exception as e:
        print(f"Error: {e}")
