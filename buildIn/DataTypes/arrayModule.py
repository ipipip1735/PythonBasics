import array
import os

# '''
# array模块 array对象
# '''
#创建数组
## arr = array.array('h')
# arr = array.array('H', [4000, 10, 700, 22222])
# for e in arr:
#     print(e)
# print('typecode is ', arr.typecode)#获取数据类型
# print('itemsize is ', arr.itemsize)#获数据类型所占字节

#字符串数组
# arr = array.array('u', 'abc')
# for e in arr:
#     print(e)
# print(arr)




#增加元素
# arr = array.array('H')
# arr.append(32)
# for e in arr:
#     print(e)


#获取buffer信息
# arr = array.array('H', [4000, 10, 700, 22222])
# print('address is ', arr.buffer_info()[0])
# print('length is ', arr.buffer_info()[1])


#统计元素出现次数
# arr = array.array('H', [1,2,3,1,4])
# for i in range(5):
#     print(i, ' is ', arr.count(i))


#批量增加元素
# arr = array.array('H')
# arr.extend([1,5,3])
# for i in arr:
#     print(i)



#读取文件
# with open('temp', 'rb') as file:
#     size = os.stat(file.name).st_size #获取文件字节数
#     print('size is ', size)
#     arr = array.array('b')
#     arr.fromfile(file, size)
#     print(arr)

#写入文件
# with open('temp', 'wb') as file:
#     arr = array.array('u', 'abc')
#     arr.tofile(file)


#写入字节
# arr = array.array('u', 'abc')
# bytes = arr.tobytes()#保存到字节对象
# print(bytes)
# arr.frombytes(bytes)#读取字节对象到数组
# print(arr)


#读取字节
# b = bytes(b'a\x00')
# print(b)
# arr.frombytes(bytes([97,98]))
# print(arr)

# arr.frombytes(bytes('abcd', 'utf-8'))
# print(arr)


#读写List
# # arr = array.array('h')
# # arr.fromlist([1,2,3])
# # print(arr)
#
# arr = array.array('u', 'abc')
# list = arr.tolist()
# print(list)




#读写字符串
# arr = array.array('u')
# arr.fromunicode('abc')
# print(arr)
#
# s = arr.tounicode()
# print(s)



#访问元素
# nums = array.array("i", [1, 2, 1, 3, 20])
# print(nums.index(1))
# print(nums.index(2))
# print(nums.index(20))



#出栈
array_num = array.array('i', [1,3,5])
i = array_num.pop()
# i = array_num.pop(1)
print(i)
print(array_num)


#插入
# array_num = array.array('i', [1,3,5])
# array_num.insert(1, 9)
# print(array_num)



#删除
# array_num = array.array('i', [1,3,5])
# array_num.remove(1)
# print(array_num)



#反序
# array_num = array.array('i', [1,3,5,7,9,10,15,10])
# array_num.reverse()
# print(array_num)