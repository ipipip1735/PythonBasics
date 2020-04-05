
'''
pprint模块 PrettyPrinter()
'''
import pprint, io

# pp = pprint.PrettyPrinter(depth=1)
# # # pp = pprint.PrettyPrinter(width=15)
# # # pp = pprint.PrettyPrinter(sort_dicts=False)
# # # pp = pprint.PrettyPrinter()
# # # list = ['a', ['b', 'c'], 'd']
# # # pp.pprint(list)
# # # dict = {'one':111, 'two':222, 'three':[1,2,3], 'four':444}
# # dict = {'a':111, 'b':222, 'd':[1,2,3], 'c':444}
# # pp.pprint(dict)

# # 深度
# pp = pprint.PrettyPrinter(depth=1)
# dict = {'one':111, 'two':222, 'three':[1,2,3], 'four':444}
# pp.pprint(dict)

# # 宽度
# # pp = pprint.PrettyPrinter(width=80)
# pp = pprint.PrettyPrinter(width=57)
# # pp = pprint.PrettyPrinter(width=56)
# # pp = pprint.PrettyPrinter(width=16)
# # pp = pprint.PrettyPrinter(width=15)
# dict = {'one':111, 'two':222, 'three':[1,2,3], 'four':444}
# pp.pprint(dict)


# # 行缩进
# pp = pprint.PrettyPrinter(indent=5, width=57)
# pp = pprint.PrettyPrinter(indent=5, width=56)
# pp = pprint.PrettyPrinter(indent=5, width=24)
# pp = pprint.PrettyPrinter(indent=5, width=23)
# dict = {'one': 111, 'two': 222, 'three': [1, 2, 3], 'four': 444}
# pp.pprint(dict)

# 输出流
# import io
stream = io.StringIO()
pp = pprint.PrettyPrinter(stream=stream)
dict = {'one': 111, 'two': 222, 'three': [1, 2, 3], 'four': 444}
pp.pprint(dict)
print(stream.getvalue())
stream.close()

# # 格式化
# pp = pprint.PrettyPrinter()
# dict = [1,[2,[3,[4,[5]]]]]
# repr, readable, recursive = pp.format(dict, {}, 5, 0)
# print(repr)
# print('readable is ', readable)
# print('recursive is ', recursive)


# # 同pprint()，底层使用字符串流，速度更快
# # pp = pprint.PrettyPrinter(indent=5, width=57)
# pp = pprint.PrettyPrinter(indent=5, width=56)
# # pp = pprint.PrettyPrinter(indent=5, width=24)
# # pp = pprint.PrettyPrinter(indent=5, width=23)
# dict = {'one': 111, 'two': 222, 'three': [1, 2, 3], 'four': 444}
# print(pp.pformat(dict))


# #快捷方法
# dict = {'one': 111, 'two': 222, 'three': [1, 2, 3], 'four': 444}
# pprint.pprint(dict, width=24, indent=5)