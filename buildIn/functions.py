# '''
# 打印
# '''
# a, b, c = 10, 72, "ccc"
# print(a, b, c, sep="|", end="--")

# a, b, c = "aa", "bb", "cc"
# print(a + ", " + b + ", " + c)

# a,b = 356.08977, 85.55
# # print("%-10.3e" % a, b, sep=" - ", end="***")
# print("%-20.3e5" % a)



# '''
# 取绝对值
# '''
# # print(abs(-11))

# '''
# Boolean类型转换
# '''
# print(bool())
# print(bool(""))
# print(bool("ggg"))
# print(bool(0))
# print(bool(1))



# '''
# 创建为字节数组
# '''
# a = "abcd" #使用String创建字节数组
# arr = bytearray(a, 'utf-8')
# for e in arr:
#     print(e)

# arr = bytearray(2)
# print(len(arr))
# for e in arr:
#     print(e)


# '''
# 遍历
# '''
# def m(e):
#     print("e")
#     return 1
# list = [1,2,4]
# map(m, list)


# '''
# 打开文件
# '''
# 读文件
# file = open("../res/temp", 'r')
# print(dir(file)) #打印file对象
# s = file.read()
# print(s)
# file.close()  # 关闭
# print(file.closed)  # 判断是否关闭
#
#
# # 使用with关键字打开文件
# # with open('../res/temp') as file:
# #     data = file.read()
# #     print(data)
# #     print(file.closed)
# # print(file.closed)
#
#
# # 写文件
# # with open('../res/temp', 'w') as file:
# # with open('../res/temp1', 'x') as file:
# # with open('../res/temp', 'a') as file:
# #     s = file.write('oooo\n')
# #     print(s)
