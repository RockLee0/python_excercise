class  BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
               self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
           elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
           elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements=[]
        if self.left:
           elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    def find_min(self):
        min=None
        if self.left:
            min=self.left.find_min()
        else:
            min=self.data
        return min

    def find_max(self):
        max=None
        if self.right:
            max=self.right.find_max()
        else:
            max=self.data
        return max
    def Calculate_sum(self):
        sum=0
        if self.left:
           sum+=self.left.Calculate_sum()
        sum+=self.data
        if self.right:
            sum+=self.right.Calculate_sum()
        return sum

    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return  self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return (self.right.search(val))
            else:
                return False

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete(val)
        if val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_value = self.right.find_min()
            self.data=min_value

            self.right=self.right.delete(min_value)

        return self



def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[10,8,2,4,9,3,4,7]
    number_tree=build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.find_min())
    print(number_tree.find_max())
    print(number_tree.Calculate_sum())
    print(number_tree.search(7))
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())
    print(number_tree.delete(7))
    print(number_tree.in_order_traversal())






