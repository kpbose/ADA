class Table:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0;
        for char in key:
         h+=ord(char)
        return h% self.max; 
    def setvalue(self,key,val):
        h=self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found =True
                break;
        if not found:
           self.arr[h].append((key,val))
    def getvalue(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                print(element[1])
    def delete_ele(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]
    def dis_table(self):
        print(f'\n {self.arr}')


if __name__ == '__main__':
    t1=Table()
    t1.setvalue('6 august','koushal')
    t1.setvalue('7 august','raja')
    t1.setvalue('27 june','ram')
    t1.getvalue('6 august')
    t1.dis_table()

    