class TreeNode:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None



# there is a bug in get_level() ....fix it later ----------
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

#-----------------------------------------------------------


    def print_tree(self):
        print(self.data)
        if self.child:
            for children in self.child:
                children.print_tree()

    def add_child(self,child):
        self.child.append(child)
        self.parent=self

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

    return root


if __name__=='__main__':
    root=print_electronics()
    root.print_tree()


