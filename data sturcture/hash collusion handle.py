# the problem is in the hash function, what if the different key gives the same index,then how store two diffent value for the keys which have same array index?? let's learn
"""
two methods to handle this. Chaining,Linear probbing.
chaining: in this method, you store multiple value at the same index and they will be touples side by side
probbing: here you don't store the value at the same index, you linearly search the available indexes which are emply and take the first location

let's implement chaining
"""

#rewrite previous code:

class hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def getHash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max

    def __setitem__(self,key,value):
        h=self.getHash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                found=True
        if not found:
            self.arr[h].append((key,value))
    def __getitem__(self, key):
        h=self.getHash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self, key):
        h=self.getHash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[idx]





t=hashtable()





"""
    def __setitem__(self, key, value):
        h=self.getHash(key)
        self.arr[h]=value
    def __getitem__(self, key):
        h=self.getHash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.getHash(key)
        self.arr[h]=None
"""
