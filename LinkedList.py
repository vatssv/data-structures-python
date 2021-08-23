class Node(object):
    def __init__(self, val: int = 0, next = None) -> None:
        """Initialize Node Object"""

        self.val = val
        self.next = next

    def update(self, val: int) -> None:
        """Update Node Object"""

        self.val = val

    def __repr__(self) -> str:
        return f"Node object: Node: {self.val}, Next: {self.next}"

    def __str__(self) -> str:
        return f"Node: {self.val}, Next: {self.next}"

class ListNode(object):
    def __init__(self, *args: Node) -> None:
        """Initialize Linked List"""

        self.head = args[0]
        if len(args) > 1:
            for i in range(1, len(args)):
                self.insert_at_beg(args[i])

    @property
    def len(self) -> int:
        """Returns length of linked list"""

        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        return count

    def insert_at_beg(self, node: Node) -> None:
        """Insert node at beginning of linked list. Needs a node argument"""

        node.next = self.head
        self.head = node
        return

    def insert_at_mid(self, ind: int = None, node: Node = None) -> None:
        """Insert node in middle of linked list. Needs either a node or position argument."""

        if node == None and ind == None:
            raise ValueError("No position selected for insertion.")

        if ind != None:
            if ind > self.len or ind < 0:
                raise IndexError

        prev = self.head
        curr = self.head.next
        for i in range(0, self.len):
            if i == ind:
                node.next = curr
                prev.next = node
                break
            prev = prev.next
            curr = curr.next
        return

    def insert_at_end(self, node):
        """Insert at end of linked list."""

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return

    def del_from_beg(self):
        """Delete from beginning of linked list."""

        if self.len >= 1:
            self.head = self.head.next
        else:
            raise Exception("No nodes in the list.")

    def del_from_mid(self, ind: int = None, node: Node = None):
        """Delete from the middle of linked list. Needs node or position argument."""

        if node == None and ind == None:
            raise ValueError("No node selected for deletion.")

        if ind != None:
            if ind > self.len or ind < 0:
                raise IndexError
        
        if ind == 0:
            return self.del_from_beg()
        
        if ind == self.len - 1:
            return self.del_from_end()

        prev = None
        curr = self.head
        # nex = self.head.next

        for i in range(0, self.len):
            if node:
                if node.val == curr.val:
                    if prev:
                        prev.next = curr.next
                        return
                    else:
                        return self.del_from_beg()
                else:
                    prev = curr
                    curr = curr.next
                    # nex = nex.next
            elif ind:
                if i == ind:
                    prev.next = curr.next
                    return
                else:
                    prev = curr
                    curr = curr.next
            else:
                continue

        raise Exception("Node not found in list")

    def del_from_end(self):
        """Delete from end of linked list."""

        temp = self.head
        if self.len == 0:
            raise Exception("No nodes in the list")
        if self.len == 1:
            return self.del_from_beg()
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def update(self, new_val: int, ind: int = None, node: Node = None) -> None:
        """Update a node in linked list. Needs node or position argument."""

        if node == None and ind == None:
            raise ValueError("No node selected for updation.")
        
        temp = self.head

        if ind != None:
            if ind > self.len or ind < 0:
                raise IndexError

        for i in range(0, self.len):
            if node:
                if temp.val == node.val:
                    temp.update(new_val)
                    return
                else:
                    temp = temp.next
            else:
                if i == ind:
                    temp.update(new_val)
                    return
                else:
                    temp = temp.next
            
        raise Exception("Node not found in list")


    def __repr__(self) -> str:
        temp = self.head
        out = f"List: {temp.val}"
        while temp.next:
            temp = temp.next
            out = out +  " -> " + str(temp.val)  
        return out

def main():
    new_node = Node(10)
    print(new_node)
    head = ListNode(new_node)
    another_node = Node(20)
    head.insert_at_beg(another_node)
    print(head)
    print(another_node)
    third_node = Node(30)
    head.insert_at_end(third_node)
    print(head)
    head.del_from_mid(2)
    head.del_from_beg()
    print(head)
    head.del_from_end()

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    print(node_1)
    print(node_2)
    node_list = ListNode(node_1)
    print(node_list)
    node_list.insert_at_beg(node_2)
    print(node_list)
    node_list.insert_at_mid(1, node_3)
    print(node_list)

    node_4 = Node(1)
    node_5 = Node(2)
    node_6 = Node(3)

    node_list_2 = ListNode(node_4, node_5, node_6)
    print(node_list_2)
    node_list_2.update(10, node=node_5)
    print(node_list_2)
    print(node_6)
    node_list_2.del_from_mid(node=node_4)
    print(node_list_2)
    node_list_2.insert_at_end(node_4)
    node_list_2.del_from_mid(ind=1)
    print(node_list_2)

if __name__ == "__main__":
    main()
