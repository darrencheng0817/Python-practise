#Explain the data structures and algorithms that you would use to design an in-mem- ory file system.
#Illustrate with an example in code where possible

#define three classes, Entry(base class), file and directory
#Entry, parent of current entry, name
#----------function, delete entry and get the full path of current file of directory

#file, content of file, size 

#directry, --> new list of entries in the current directory 
#this way 
#adding files and directory
#check the size of the directory
#number of file


#how delete works ????????????
class Entry:
    def __init__ (self, parent, name):
        self.__parent = parent
        self.__name = name
    
    def delete(self):
        if self.__parent != None:
            def __del__(self):
                pass
            return True
        else: 
            return False
        
    def get_full_path(self):
        list1 = []
        while self != None:
            list1 = [self.__name] + list1
            self = self.__parent
        
        return list1
        
    def get_name(self):
        return self.__name
    
    def get_parent(self):
        return self.__parent
    
class file(Entry):
    def __init__ (self, parent, name, size, content):
        Entry.__init__(self, parent, name)
        self.size = size
        self.content = content
   

class direc(Entry):
    def __init__(self, parent, name, size):
        Entry.__init__(self, parent, name)
        self.entryList = []
        self.size = size
    
    def addEntry(self, file):
        self.entryList = self.entryList + [file]
        
    def size_all(self):
        size = 0
        for i in self.entryList:
            size += i.size
        return size
            
    def num_files(self):
        counter = 0
        for i in self.entryList:
            if i.__class__ == direc:
                counter += 1
                counter += i.num_files()
            else:
                counter += 1
        return counter

def main():
    #testing part 1
    f1 = file(None, "f1", 2, "he1")
    f2 = file(f1, "f2", 3, "he2")
    f3 = file(f2,"f3", 4, "he3")
    print f3.get_full_path()
    
    #testing part 2
    d1 = direc(None, "d1", 1)
    d2 = direc(d1, "d2", 1)
    d2.addEntry(f1)
    
    d1.addEntry(d2)
    d1.addEntry(f1)
    d1.addEntry(f2)
    d1.addEntry(f3)
    print d1.size_all()
    print d1.num_files()
        
    

if __name__ == "__main__":
    main()
  		  