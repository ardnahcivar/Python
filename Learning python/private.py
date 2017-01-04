class A:
    def __init__(self,a,b,c):
        self.__a = a
        self._b = b
        self.c = c

    def disp(self):
        #print('Value of a is {}, b is {}, c is {}'.format(self.__a,self._b,self.c))
        print('value of private variable a is ',self.a)

class B(A):
    def __init__(self,a,b,c,d):
        A.__init__(self,a,b,c)
        self.d = d

    def show(self):
        pass
        #print('Value of c is',self.__a)
    
a = A(2,4,6)
a.disp()
b = B(12,14,16,18)
b.show()



