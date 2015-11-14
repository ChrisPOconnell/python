class TreeNode:
    def __init__(self, a_name, a_parent, some_children):
        self.name = a_name
        self.parent = a_parent
        self.children = some_children

    def add_child(self, a_child):
        self.children.append(a_child) 

    def print_pre_order(self):
        print(self.name)
        if len(self.children) > 0:
            for child in self.children:
                child.print_pre_order()

sample_tree = TreeNode("-- A --", None, [])
node_1 = TreeNode("-- B --", sample_tree, [])
node_2 = TreeNode("-- C --", sample_tree, [])
node_3 = TreeNode("-- D --", sample_tree, [])
node_4 = TreeNode("-- E --", sample_tree, [])
node_5 = TreeNode("-- F --", sample_tree, [])
sample_tree.add_child(node_1)
sample_tree.add_child(node_2)
sample_tree.add_child(node_3)
node_1.add_child(node_4)
node_1.add_child(node_5)

sample_tree.print_pre_order()
print("\n\n\n")
node_1.print_pre_order()


