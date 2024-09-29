class TreeNode:
    def __init__(self, data,designation):
        self.data = data
        self.designation=designation
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
         print(prefix + self.data + ' ( '+ self.designation + ' ) ')
         if self.children:
            for child in self.children:
                child.print_tree(data)

        elif data == 'name':
          print(prefix + self.data)
          if self.children:
            for child in self.children:
                child.print_tree(data)
        elif data=='designation':
            print(prefix + self.designation )
            if self.children:
                for child in self.children:
                    child.print_tree(data)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Nilupul",'CEO')

    Chinmay = TreeNode("Chinmay",'CTO')
    Vishwa = TreeNode("Vishwa",'Infrustucture Head')
    Vishwa.add_child(TreeNode('Dhaval','Clound Manager'))
    Vishwa.add_child(TreeNode('Abhijit', 'App Manager'))
    Chinmay.add_child(Vishwa)


    Gels  = TreeNode("Gels",'HR Head')
    Gels.add_child(TreeNode("Peter",'Recrutemnet Manager'))
    Gels.add_child(TreeNode("Wakas", 'Policy Manager'))

    root.add_child(Chinmay)
    root.add_child(Gels)

    return root

if __name__ == '__main__':
    root_node=build_product_tree()
    root_node.print_tree('designation')
    root_node.print_tree('name')
    root_node.print_tree('both')
