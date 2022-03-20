class Node:
    def __init__(self, value: int):
        self.left: Node | None = None
        self.value: int = value
        self.right: Node | None = None
        self.is_root: bool = False
        self.is_parent = False

    def __str__(self) -> str:
        return f"Node(value={self.value}, is_root={self.is_root})"


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node | None = None
        self.traversal_path: list[int] = []

    def reset_traversal_path(self) -> None:
        self.traversal_path = []

        return None

    def create_node(self, value: int) -> Node:
        return Node(value)

    def insert_node(self, current_node: Node | None, value: int) -> None:
        if current_node is None:
            self.root = self.create_node(value)
            # Satisfy mypy.
            assert self.root is not None
            self.root.is_root = True

            return None

        if value < current_node.value:
            if current_node.left is None:
                current_node.left = self.create_node(value)

            else:
                current_node.is_parent = True
                self.insert_node(current_node.left, value)

        if value > current_node.value:
            if current_node.right is None:
                current_node.is_parent = True
                current_node.right = self.create_node(value)

            else:
                self.insert_node(current_node.right, value)

        return None

    def visit(self, node: Node) -> None:
        self.traversal_path.append(node.value)

    def traverse_preorder(self, current_node) -> list[int]:
        if current_node is not None:
            self.visit(current_node)
            self.traverse_preorder(current_node.left)
            self.traverse_preorder(current_node.right)

        return self.traversal_path

    def traverse_inorder(self, current_node) -> list[int]:
        if current_node is not None:
            self.traverse_inorder(current_node.left)
            self.visit(current_node)
            self.traverse_inorder(current_node.right)

        return self.traversal_path

    def traverse_postorder(self, current_node) -> list[int]:
        if current_node is not None:
            self.traverse_postorder(current_node.left)
            self.traverse_postorder(current_node.right)
            self.visit(current_node)

        return self.traversal_path

    def is_internal_node(self, current_node: Node) -> bool:
        """A node that is neither root nor a leaf node."""

        return not current_node.is_root and not current_node.is_parent

    def is_leaf_node(self, current_node: Node):
        """A node that has no children."""

        return not current_node.left and not current_node.right


def main():
    tree = BinaryTree()
    tree.insert_node(None, 6)
    root = tree.root

    tree.insert_node(tree.root, 3)
    tree.insert_node(root, 5)
    tree.insert_node(root, 1)
    tree.insert_node(root, 2)

    print("PreOrder tree traversal->")
    print(tree.traverse_preorder(root))
    print()
    print("inorder tree traversal->")
    tree.reset_traversal_path()
    tree.traverse_inorder(root)
    print(tree.traversal_path)
    print()
    print("postorder tree traversal->")
    tree.traverse_postorder(root)
    print(tree.traversal_path)


if __name__ == "__main__":
    main()
