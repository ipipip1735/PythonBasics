'''
weaker模块 ref对象
'''
import weakref

class A:
    def __init__(self, n):
        print("++ " + __class__.__name__ + ".__init__() ++")
        self.n = n
    def __del__(self):
        print("++ " + __class__.__name__ + ".__del__() ++")
    def see(self):
        print('see - ', self.n)
# 创建弱引用
# a = A(99)
#
# wRef = weakref.ref(a, lambda ref: print(ref, ' die'))
# aOne = wRef()

# print(a is aOne)
# a.see()
# aOne.see()

# del a

# print(wRef)
# print(aOne)
# del aOne
#
# aTwo = wRef()
# print(aTwo)





#创建多个弱引用
a = A(0)
wRef = weakref.ref(a, lambda ref: print(ref, ' die'))
one = wRef()
two = wRef()

del a, one
print(two)

del two
