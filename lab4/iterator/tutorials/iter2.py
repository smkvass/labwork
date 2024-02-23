

#Stop after 20 iterations:
class MyNumbers:
    def __init__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
    
    