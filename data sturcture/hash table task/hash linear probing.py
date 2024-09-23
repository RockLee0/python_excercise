#due: use linear probbing 



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


