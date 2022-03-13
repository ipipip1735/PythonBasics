# '''
# 函数装饰器-定义
# '''
# def xx(ff):
#     print("ff =", ff)
#     return lambda: print('go')
#
#
# @xx
# def show():
#     print('show')
# show()
# show()
# show()

# '''
# 函数装饰器-使用工具注解
# '''
# from functools import wraps
# def xx(ff):
#     print("ff =", ff)
#     # @wraps(ff)
#     def kk():
#         print('~~kk~~|go')
#     return kk
#
# @xx
# def show():
#     print('~~show~~')
#
# show()
# print(show.__name__)



# '''
# 函数装饰器-携带参数的目标函数
# '''
# def xx(ff):
#     print("ff =", ff)
#     def TTT(*args, **kw):
#         print('--start--')
#         print('args =', args)
#         print('kw =', kw)
#         ff(*args, **kw)
#         print('--end--')
#     return TTT
#
# @xx
# def show(a, b, c = 33, d = 44):
#     print('show')

# show(1, 2)
# show(1, 2, c = 301)
# show(1, 2, c = 301, d = 491)
# print(show.__name__)

# '''
# 函数装饰器-装饰器参数
# '''
import functools

def xx(k):
    print('~~xx~~|k =', k)
    def yy(fn):
        print('~~yy~~|fn =', fn)
        @functools.wraps(fn)
        def zz(*args, **kw):
            print('~~zz~~|args =', args, 'kw =', kw)
            return fn(*args, **kw)
        return zz
    return yy

# @xx('dddd')
# def show():
#     print('show')
# show()
# show()
# show()

@xx('bbbb')
def see(a, b, c = 33, d = 44):
    print('show')

see(1, 2)
see(1, 2, c = 301)
see(1, 2, c = 301, d = 491)
print(see.__name__)

