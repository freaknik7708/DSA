#hash maps are basically used to give a string as an index to retrieve items from the list. The in-built hashmap for python is dictionary.
# So, first lets create a hashmap without using dictionary

class hash:
    def __init__(self):
        self.max=30
        self.arr=[None for i in range(self.max)]
    def gethash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.max
    
    def additems(self,key,val):
        h=self.gethash(key)
        self.arr[h]=val
    def printl(self):
        print(self.arr)
h=hash()
h.additems('chakri',22)
h.additems('chaithra',15)
h.additems('harshitha',21)
h.printl()

# like this hashmap is created normally. But there is a problem here. That is, unable to insert all elements. Because, some string-elements will have the ord number more than the give size of the array. So, in that case, the array simply ignores those items and stores only upto the number it can fit in it.
'''
for example, if the size is set to 100- then output is
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, None, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
but when the size is set to 10-output is
[None, None, None, None, None, None, 21, None, None, None]

here in this case, 22 and 15 are missing. So, to overcome this problem, the size of the array should be increased.

So, to overcome this, python uses dictionary.
''' 