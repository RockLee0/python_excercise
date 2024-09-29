# due for future work

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,data):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if data == 'both':
         print(prefix + self.data)
         if self.children:
            print(self.get_level())
            for child in self.children:
                child.print_tree(data)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Global")

    India = TreeNode("India")
    Gujrat = TreeNode("Gujrat")
    Gujrat.add_child(TreeNode('Ahemdabad'))
    Gujrat.add_child(TreeNode('Baroda'))
    India.add_child(Gujrat)

    Kalkata = TreeNode("Kalkata")
    Kalkata.add_child(TreeNode('Bangluru'))
    Kalkata.add_child(TreeNode('Mysore'))
    India.add_child(Kalkata)


    USA  = TreeNode("USA")
    NewJersey = TreeNode("New Jersey")
    NewJersey.add_child(TreeNode('Princton'))
    NewJersey.add_child(TreeNode('Trienton'))
    USA.add_child(NewJersey)

    California = TreeNode("California")
    California.add_child(TreeNode('San fransisco'))
    California.add_child(TreeNode('Mountain View'))
    California.add_child(TreeNode('Palo Alto'))
    USA.add_child(California)


    root.add_child(India)
    root.add_child(USA)

    return root

if __name__ == '__main__':
    root_node=build_product_tree()
    root_node.print_tree('both')
