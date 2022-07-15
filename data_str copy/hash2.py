##hash table by linear probing
class Table:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0;
        for char in key:
            h+=ord(char)
        return h % self.max
    def setvalue(self,key,value):
        h=self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h]=(key,value)
        else:
            new_h=self.search_index(h)
            self.arr[new_h]=(key,value)
    def get_range_index(self,h):
        l=[*range(h,len(self.arr))]+ [*range(0,h)]
        return l
    def search_index(self,h):
        range_index=self.get_range_index(h)
        for element in range_index:
            if self.arr[element] is None:
                return element
            if self.arr[element][0]==h:
                return element
        raise Exception("Hash Table Full")
    def getvalue(self,key):
        h=self.get_hash(key)
        if self.arr[h] is None:
            return
        range_index= self.get_range_index(h)
        for prob_index in range_index:
            element=self.arr[prob_index]
            if element is None:
                return
            if element[0]==key:
                print(element[1])
    def get_arr(self):
        print(self.arr)
if __name__ =='__main__':
    t1=Table()
    t1.setvalue('6 august','koushal')
    t1.setvalue('7 august','raja')
    t1.setvalue('6 august','aayush')
   
    t1.setvalue('27 june','ram')
    t1.getvalue('6 august')
    t1.get_arr()


