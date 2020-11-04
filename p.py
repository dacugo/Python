""" try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")


print(chr(ord('p')+2))

print (float("1.3"))


class A:
    def __init__(self, v=2):
        self.v = v
    
    def set(self, v=1):
        self.v += v
        return self.v

a = A()
b = a
b.set()
print(a.v)



class A:
    A = 1
    def __init__(self):
        self.a = 0
    
print(hasattr(A,'a'))

class A:
    pass

class B:
    pass

class C:
    pass

print(issubclass(A,C))




class A:
    def __init__(self,v):
        self.__a = v + 1

a = A(0)
print(a.__a)


class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a,'A'))



class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()



try:
    raise Exception (1,2,3)
except Exception as e:
    print(len(e.args))

 

def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in I(2):
    print(x, end='')



class I:
    def __init__ (self):
        self.s='abc'
        self.i=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i==len(self.s):
            raise StopIteration
        v=self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x, end='')

"""
def o(p):
    def q():
        return '*'*p
    return q

r = o(1)
s = o(2)

print(r() + s())

















