# str1='string'
# str2=str1[:]

# print(len(str1))
# print(len(str2))

# def f(part2,part1):
#     return part2+part1

# print(f(part2=1,2))

# z=2
# y=1
# x= y<z or z>y and y>z or z<y
# print(x)

# str='abcdef'

# def fun(s):
#     del s[2]
#     return s

# print(fun(str))

# x,y,z=3,2,1
# z,y,x=x,y,z
# print(x,y,z)

# def fun(x):
#     return 1 if x%2 != 0 else 2

# print(fun(1))

# print(len((1,)))

# d={1:0,2:1,3:2,0:1}
# x=0

# for y in range (len(d)):
#     x=d[x]

# print(x)

# print("a","b","c",sep="'")

# v=1+1//2+1/2+2
# print(v)

# t=(1,)

# t=t[0]+t[0]

# print(t)

# x=16
# while x>0:
#     print('*',end='')
#     x//=2

# d={'uno':1,'tres':3,'dos':2}

# for k in sorted(d.values()):
#     print(k,end=' ')

# print(len([i for i in range(0,-2)]))

# lt=[1,2,3,4]

# lt=list(map(lambda x: 2*x,1))
# print(lt)

# i=4

# while i>0:
#     i-=2
#     print("*")
#     if i == 2:
#         break
#     else:
#         print("*")

# t=(1,2,3,4)
# t=t[-3:-1]
# t=t[-1]
# print(t)

# d={}
# d['2']=[1,2]
# d['1']=[3,4]

# for x in d.keys():
#     print(d[x][1], end="")


# def fun(d,k,v):
#     d[k]=v

# dc={}
# print(fun(dc,'1','v'))

# ls=[[c for c in range (r)] for r in range (3)]
# for x in ls:
#     if len(x) < 2:
#         print('vacia')


# try:
#     raise Exception
# except BaseException:
#     print("a", end='')
# else:
#     print("b", end='')
# finally:
#     print("c")

# class A:
#     def __init__(self,name):
#         self.name=name

# a = A("class")
# print(a)

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")


# class X:
#     pass

# class Y(X):
#     pass

# class Z(Y):
#     pass

# x=X()
# z=Z()
# print(isinstance(x,z), isinstance(z,X))

# x="""
# """
# print(len(x))

# class A:
#     A = 1
#     def __init__(self, v=2):
#         self.v = v + A.A
#         A.A += 1

#     def set(self, v=2):
#         self.v += v
#         A.A += 1
#         return

# a = A()
# a.set(2)
# print(a.v)

# class A:
#     A = 1
#     def __init__(self, v=2):
#         self.a = 0

# print(hasattr(A, 'A'))

# class A:
#     pass

# class B:
#     pass

# class C(A,B):
#     pass

# print(issubclass(C,A) and issubclass(C,B))

# class A:
#     def __init__(self, v):
#         self._a = v + 1

# a = A(0)
# print(a._a)

# class A:
#     def __init__(self):
#         pass
#     def f(self):
#         return 1
#     def g():
#         return self.f()

# a = A()
# print(a.g())

# class A:
#     def a(self):
#         print('a')
# class B:
#     def a(self):
#         print('b')
# class C(A,B):
#     def c(self):
#         self.a()
# o=C()
# o.c()


# def I(n):
#     s=''
#     for i in range(n):
#         s += '*'
#         yield s
# for x in I(3):
#     print(x,end='')

def a(x):
    def b():
        return x + x
    return b
x=a('x')
y=a('')
print(x()+y())


