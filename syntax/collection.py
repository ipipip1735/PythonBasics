import typing

# '''
# 元组
# '''
# t = () #空元组
# for i in t:
#     print(i)


# '''
# 字典
# '''
# dict = {'one':111, 'two':222}
# dict1 = dict.copy()#复制
#
# dict.clear()
# print(dict)
# print(dict1)



# '''
# 类型判断
# '''

dict = {'one':111}
if(isinstance(dict, typing.Iterable)):
    print('dict is ', typing.Iterable)

#实现了多个接口
if(isinstance(dict, (typing.Iterable, typing.Iterator))):
    print('dict is', typing.Iterable, 'and', typing.Iterator)



# '''
# del关键字
# '''
# a = [1,2,3,4]
# del a[0]
# del a
# for e in a:
#     print(e)


# '''
# 枚举器
# '''
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# enum = enumerate(seasons)
# for i, e in enum:
#     print(i, e)


# '''
# 过滤
# '''
# def f(e):
#     print(e)
#     return False
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# f = filter(f, [1,2,3])
# list = list(f)
# print(list)


# '''
# 反序
# '''
# # for string
# seq_string = 'Python'
# print(list(reversed(seq_string)))
#
# # for tuple
# seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
# print(list(reversed(seq_tuple)))
#
# # for range
# seq_range = range(5, 9)
# print(list(reversed(seq_range)))
#
# # for list
# seq_list = [1, 2, 4, 3, 5]
# print(list(reversed(seq_list)))


# '''
# 映射
# '''
# def m(e):
#     print(e)
#     return 1
# map = map(m, [1,21,36,4])
#
# list = list(map)
# print(list)
#
# # set = set(map)
# # print(set)


# '''
# 切片
# '''
# s = slice(1)
# print(s)
#
# arr = [1,2,3]
# print(arr[s])
# print(arr)


# '''
# 排序
# '''
# # list = [1,2]
# # list1 = sorted(list, reverse=True)
# # print(list)
# # print(list1)
#
# #使用key函数的返回值排序
# # 例一：
# # def s(a):
# #     print(a)
# #     return a[1]
# #
# # tuple = (1,2), (1,3), (1,1)
# # print(sorted(tuple, key=s, reverse=False))
#
# # 例二：
# list = ['a', 'b', 'c', 'd']
# def k(item):
#     print(item)
#     if item == 'a':
#         return 1
#     elif item == 'b':
#         return 4
#     elif item == 'c':
#         return 3
#     else:
#         return 2
# print(sorted(list, key=k, reverse=False))


# # '''
# # 归并
# # '''
# # x = [1, 2, 3]
# # y = [4, 5, 6]
# # z = zip(x, y)
# # list = list(z)
# # print(list)
#
# list = [(1, 4), (2, 5), (3, 6)]
# x, y = zip(*list)
# print(x)
# print(y)
