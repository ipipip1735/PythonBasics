import ctypes
import ctypes.util
import os

# '''
# ctypes.util模块
# C++源码为xx.cpp，编译的动态链接库为xx.dll
# '''
# 查找系统库
# dllPath = ctypes.util.find_library("kernel32")
# print("dllPath is", dllPath)

# 查找自定义库
# dllPath = ctypes.util.find_library("xx")
# print("dllPath is", dllPath)


# '''
# ctypes模块
# C++源码为xx.cpp，编译的动态链接库为xx.dll
# '''
### 加载动态链接库 ###
with os.add_dll_directory(os.getcwd()):  # 增加库目录
    dllPath = ctypes.util.find_library("xx")  # 获取库文件路径
    # dllPath = r'E:\Program\CPP\VisualStudio\cmakeTrail\out\build\x64-Debug\CMakeProject\xx.dll'
    dll = ctypes.CDLL(dllPath) #加载库，返回库对象
    # dll = ctypes.OleDLL(dllPath)
    # dll = ctypes.WinDLL(dllPath)
    # ctypes.PyDLL(dll)


#使用全局变量加载库文件
# with os.add_dll_directory(os.getcwd()): #增加库搜索目录
#     dllPath = ctypes.util.find_library('xx') #获取库文件全名
#     dll = ctypes.cdll.LoadLibrary(dllPath)
#
# print(dll)
# print(dll._name)



### 调用库函数 ###
# print(dll.sum(5, ctypes.c_uint(6)))#参数类型为int

# dll.show(ctypes.c_char_p(bytes('ohoh', 'utf-8'))) #参数类型为char指针
# dll.show(ctypes.c_char_p(b'gogo'))

# buffer = ctypes.create_string_buffer(b'sd')#使用string buffer
# print(buffer.raw)
# print(buffer.value)
# ub = ctypes.create_unicode_buffer(u'opop')
# print(ub.value
# dll.see(buffer, ub)


#成员变量作为库函数参数
# class A:
#     def __init__(self, one):
#         self._two=one
#     @property
#     def two(self):
#         print("~~ " + __class__.__name__ + ".gettwo() ~~")
#         return self._two
#     @two.setter
#     def two(self, value):
#         print("~~ " + __class__.__name__ + ".settwo() ~~")
#         self._two = value
# dll.view(A(b'oooo').two)

# dll.view(A(b'oooo'))
# b = A(b'oooo')
# b.two = b'sod'
# print(b.two)


#设置库函数参数
# dll.combine.argtypes = [ctypes.c_char_p, ctypes.c_float]
# dll.combine(b'beer', 2.3)


#指定库函数返回值类型
# dll.append.restype = ctypes.c_char_p
# s = dll.append(b'tttt')
# print(s)


#设置库函数返回值为回调函数
# def callback(r):
#     print('~~callback~~')
#     print(r)
#
# dll.sum.restype = callback
# dll.sum(1, 27)


###  引用 / 指针 ###
#使用引用传值
# i = ctypes.c_int(10)#创建int变量
# print(i)
# print(ctypes.byref(i))#创建int变量的引用
#
# dll.ref(ctypes.byref(i))
#
# print(i)
# print(ctypes.byref(i))



#使用指针
# i = ctypes.c_int(42)#创建int对象
# print(i)
# pi = ctypes.pointer(i)#创建指针
# print(pi)
# print(pi.contents)


#指针做库函数参数
# i = ctypes.c_int(42)
# pi = ctypes.pointer(i)
# dll.poi(pi)
# print(i)


#指针索引
# i = ctypes.c_int(42)
# pi = ctypes.pointer(i)
# print(pi.contents)
#
# print(pi._type_)
# j = ctypes.c_int(99)
# pi.contents = j
# print(pi[0])




#声明指针类型
# PI = ctypes.POINTER(ctypes.c_int)#声明一个int类型指针
# print(PI)
# print(PI.contents)
#
# p = PI(ctypes.c_int(42))#实例化int类型指针
# print(p)
# print(p.contents)


#函数指针
# def fn(d):
#     print('~~ Python.fn ~~')
#     print(d)
#     d *= 2
#     return d
#
# FNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)#声明函数原型
# fnp = FNTYPE(fn) #创建函数指针
# dll.funp(fnp) #调用库函数

#函数指针,无返回值
# def fn(d):
#     print('~~ Python.fno ~~')
#     print(d)
# FNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
# fnp = FNTYPE(fn)
# dll.funpo(fnp)



#指向数组(使用pointer对象)
# INTS = ctypes.c_int * 5 #声明数组
# arr = INTS(1,2,4,3,1) #数组初始化
# print(arr)
# p = ctypes.pointer(ctypes.c_int(0))#创建指针，并初始化
# p.contents = arr #让指针指向数组
# print(p)
# for i in range(len(arr)):
#     print(p[i])

#指向数组(使用POINTER全局函数)
# arr = (ctypes.c_int * 5)(1,2,4,3,1)
# print(arr)
# p = ctypes.POINTER(ctypes.c_int)
# pInt = p(arr)
# print(pInt)
# for i in range(len(arr)): print(pInt[i])


#指向数组(使用cast全局函数)
# arr = (ctypes.c_int * 5)(1,2,4,3,1)
# print(arr)
# p = ctypes.POINTER(ctypes.c_int)
# print(p)
# pp = ctypes.cast(arr, p)
# print(pp)
# for i in range(len(arr)): print(pp[i])


### 数组 ###
# TenIntegers = ctypes.c_int * 10 #声明数组，分配空间为4
# ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #实例化，并初始化
# for i in ii:
#     print(i, end=" ")

#简化版
# arr = (ctypes.c_int * 10)(1,4,1,2)
# for i in arr: print(i, end=", ")
# dll.ints(arr)#调用库函数，数组做参数是引用传递，库函数可以修改数组元素值
# for i in arr: print(i, end=", ")


#获取数组信息
# arr = (ctypes.c_int * 10)(1,2,3,4)
# print(arr._type_)
# print(arr._length_)
# print(type(arr))



#修改数组尺寸
# arr = (ctypes.c_short * 4)(1,4,2,5)
# arrNew = (ctypes.c_short * 32).from_address(ctypes.addressof(arr))
# print(arrNew[:])






### 结构体 ###
# class Person(ctypes.Structure):
#     _fields_ = [('name', ctypes.c_char_p),
#                 ('age', ctypes.c_int)]
#
# one = Person(age=15, name=b'Tom')
# dll.stru(one)

#结构体数组
# one = Person(age=15, name=b'Tom')
# two = Person(age=54, name=b'bob')
# Persons = Person * 2
# ps = Persons(one, two)
# dll.strus(ps)


### 访问静态常量 ###
# n = ctypes.c_int.in_dll(dll, 'num')
# print(n)
#
# p = ctypes.c_char_p.in_dll(dll, 's')
# print(p)
# print(p.value)
#
# dll.vari(p, n)



class Car(ctypes.Structure):
    _fields_ = [('price', ctypes.c_float),
                ('name', ctypes.c_char_p)]

one = Car(price=50.23, name=b'Toyota')
dll.clas(one)