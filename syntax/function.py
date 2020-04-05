# def fn(n):
#     "ddd"
#     print(fn.__doc__)
# fn(12)


# def fn():
#     return
#
# a = fn()
# print(a)


# def no_return(x,y):
#     c = x + y
#
# res = no_return(4,5)
# print(res)


# def mul_return():
#     return 1,4

# a = mul_return()
# print(a)
# for t in a:
#     print(t)
# s,t = mul_return()
# print(s,t)


# def mul_return(**k):
#     print(k.keys())
#     print(k.values())
#     print(k['a'], k['b'])
#
# mul_return(a=1, b=2)


'''
函数注解
'''
#参数注解
# def foo(a: 'xxx', b: 'yyy' = 2, *args:'sss', **kwargs:'ttt'):
#     print("~~foo~~")
#     print('a is ', a)
#     print('b is ', b)
# foo(111)

#返回值注解
# def foo(a:'one') -> 'xx':
#     print("~~foo~~")
#     print('a is ', a)
# foo(111)
# print(foo.__annotations__)

def a(): ...
