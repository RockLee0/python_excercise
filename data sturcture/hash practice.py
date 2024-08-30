class hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def getHash(self,key):
        h=0
        for char in key:
            h+=ord(char) #gives the askii value for each
        return h%self.max
    def __setitem__(self,key,value):
        h=self.getHash(key)
        self.arr[h]=value
    def __getitem__(self,key): #standerd function of get.
        h=self.getHash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h=self.getHash(key)
        self.arr[h]=None
t=hashtable()
t['ipo'] = 99  # Set value with key 'ipo'
print(t['ipo'],t.arr)


