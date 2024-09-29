class TreeNode:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None
    def add_child(self,child):
        self.child.append(child)
        self.child=self
    def print(self):
        print(self.data)
        for eachChild in self.child:
            print(eachChild.data)


def print_electronics():
    root = TreeNode('Electronics')
    laptop = TreeNode('laptop')
    televisions = TreeNode('televisions')
    cellphones = TreeNode('cellphones')

    laptop.add_child(TreeNode('MackBook'))
    laptop.add_child(TreeNode('Microsoft'))
    laptop.add_child(TreeNode('Think pad'))

    televisions.add_child(TreeNode('Samsung'))
    televisions.add_child(TreeNode('Lg'))

    cellphones.add_child(TreeNode('Iphone'))
    cellphones.add_child(TreeNode('pixel'))
    cellphones.add_child(TreeNode('vivo'))

    root.add_child(laptop)
    root.add_child(televisions)
    root.add_child(cellphones)

    return root.print()

print_electronics()



