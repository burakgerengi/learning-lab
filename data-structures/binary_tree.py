class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            temp_list = [self.root]
            while temp_list:
                current_node = temp_list.pop(0)
                if not current_node.left:
                    current_node.left = Node(data)
                    return
                elif current_node.left:
                    temp_list.append(current_node.left)

                if not current_node.right:
                    current_node.right = Node(data)
                    return
                elif current_node.right:
                    temp_list.append(current_node.right)

    def search(self, data):
        temp_list = self.in_order_traversal()
        return temp_list.__contains__(data)

    def in_order_traversal(self):
        traversal_list = []
        self._in_order_helper(self.root, traversal_list)

        return traversal_list

    def _in_order_helper(self, current_node, traversal_list):
        if current_node is None:
            return

        self._in_order_helper(current_node.left, traversal_list)

        traversal_list.append(current_node.data)

        self._in_order_helper(current_node.right, traversal_list)

    def find_max(self):
        traversal_list = self.in_order_traversal()
        return max(traversal_list)

    def fin_min(self):
        traversal_list = self.in_order_traversal()
        return min(traversal_list)
