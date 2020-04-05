import abc


# '''
# 类声明
# 声明私有成员、公有成员、静态成员
# '''
# # 声明外部全局变量，给静态成员函数引用
# def oFn():
#     print("~~ oFn ~~")
#
# # 声明类
# class One:
#     a = 0 #静态成员变量
#     oFn = oFn #静态成员函数
#
#     def __init__(self, b, c):  #构造函数
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         self.b = b #公有成员变量
#         self.__c = c  #私有成员变量，以__开头
#
#     def fn(self):  #公有成员函数
#         print("~~ " + __class__.__name__ + ".fn ~~")
#
#     def __pFn(self): #私有成员函数
#         print("~~ " + __class__.__name__ + ".__pFn ~~")
#
# a = One(111, 222) #实例化
# print(One.a) #访问访问静态变量
# print(a.b) #访问公有成员变量
# # print(a.__c) #报错，访问私有成员变量，但可以使用_One__c访问
#
# One.oFn() #调用静态函数
# a.fn() #调用公有成员函数
# # a.__pFn() #报错，调用私有成员函数，但可以调用_One__pFn()


# '''
# 类的继承
# '''
# class Aa:
#     one = 1
#
#     def __init__(self):
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         self.two = 22
#         self.__ppp = 3
#
#     def show(self):
#         print("++ " + __class__.__name__ + ".show() ++")
#         print(self.two)
#         print(self.__ppp)
#
#     def __ppShow(self):
#         print("++ " + __class__.__name__ + ".__ppShow() ++")
#
# class Bb(Aa):
#     three = 3
#
#     def __init__(self):
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         super().__init__() #调用父类构造函数
#         # Aa.__init__(self) #使用类名是等价的
#         self.four = 44
#
#     def see(self):
#         print("++ " + __class__.__name__ + ".see() ++")
#         print(self.two) #访问父类构造
#         self.show() #访问父类成员函数
#         # self.__ppp
#         # self.__ppShow()
#
# bb = Bb()
# bb.see()
# # bb.show()


# '''
# 多继承
# '''
# class Aa:
#     one = 1
#
#     def __init__(self):
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         self.two = 22
#
#     def show(self):
#         print("++ " + __class__.__name__ + ".show() ++")
#
#     def see(self):
#         print("++ " + __class__.__name__ + ".see() ++")
#         # super().see()
#
#
# class Bb:
#     three = 3
#
#     def __init__(self):
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         self.four = 44
#
#     def see(self):
#         print("++ " + __class__.__name__ + ".see() ++")
#
# # 继承两个父类
# class Cc(Aa, Bb):
#     five = 5
#
#     def __init__(self):
#         print("++ " + __class__.__name__ + ".__init__ ++")
#         Bb.__init__(self)
#         Aa.__init__(self)
#         self.six = 66
#
#     def view(self):
#         print("++ " + __class__.__name__ + ".view() ++")
#         # print(self.six)
#         # super().show()
#     def see(self):
#         print("++ " + __class__.__name__ + ".see() ++")
#         # super().see()
#         # print(self.six)
#
# ccc = Cc()
# # print(Cc.mro())
# # ccc.view()
# # ccc.see()
# # ccc.show()


# '''
# 多态
# '''
# class A:
#     def cc(self, one="111"):
#         print("one is " + one)
# aa = A()
# aa.cc()
# aa.cc("222")


# '''
# 对象遍历
# '''
# class FE:
#     def __iter__(self):
#         print("++ " + __class__.__name__ + ".__iter__() ++")
#         self.index = 3
#         return self
#
#
#     def __next__(self):
#         print("++ " + __class__.__name__ + ".__next__() ++")
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.index
#
# fe = FE()
# for e in fe:
#     print(e)


# '''
# toString
# '''
# class A:
#     def cc(self, one="111"):
#         print("one is " + one)
#     def __str__(self):
#         print("++ " + __class__.__name__ + ".__str__() ++")
#         return "cccccc"
# aa = A()
# s = str(aa)
# print(s)


# '''
# 类方法
# '''
# class A:
#     @classmethod
#     def f(cls):
#         print(cls)
# A.f()


# '''
# 静态方法
# '''
# class A:
#     @staticmethod
#     def f():
#         print("go")
# A.f()


# '''
# 对象属性
# '''
# # class C:
# #     def __init__(self):
# #         self._x = None
# #
# #     def getx(self):
# #         print("++ " + __class__.__name__ + ".getx() ++")
# #         return self._x
# #
# #     def setx(self, value):
# #         print("++ " + __class__.__name__ + ".setx() ++")
# #         self._x = value
# #
# #     def delx(self):
# #         print("++ " + __class__.__name__ + ".delx() ++")
# #         del self._x
# #
# #     x = property(getx, setx, delx, "I'm the 'x' property.")
# #     # x = property(getx, None, delx, "I'm the 'x' property.") #只读属性
#
# class C:
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#         print("++ " + __class__.__name__ + ".getx() ++")
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         print("++ " + __class__.__name__ + ".setx() ++")
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         print("++ " + __class__.__name__ + ".delx() ++")
#         del self._x
#
# c = C()
# c.x = 5
# c.x
# del c.x


# '''
# 子类判断
# '''
# class A:
#     pass
#
# class B(A):
#     pass
# print(issubclass(A, object))
# print(issubclass(B, (A)))
# print(issubclass(B, (A, object)))



# '''
# 抽象方法
# '''
class A(abc.ABC):

    def show(self):
        print("++ " + __class__.__name__ + ".show() ++")

    @abc.abstractmethod
    def see(self):...

class B(A):
    def see(self):...


print(issubclass(B, A))


b = B()
b.see()
b.show()

