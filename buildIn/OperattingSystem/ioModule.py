import os

# '''
# io模块 FileIO对象
# '''

#获取文件指针
# with open('../res/temp', 'r') as file:
#     if(file.seekable()):
#         print("tell is ", file.tell())
#         print("position is ", file.seek(2))


#读取一个字节
# with open('../res/temp', 'r') as file:
#     while file.readable():
#         chunk = file.read(1)
#         if chunk == '':
#             break
#         print(chunk)

#读取一行
# with open('../res/temp', 'r') as file:
#     while file.readable():
#         chunk = file.readline(1)
#         if chunk == '':
#             break
#         print(chunk)
#读取所有行
# with open('../res/temp', 'r') as file:
#     for line in file:
#         print(line, end='')

# print("fileNo is ", file.fileno())


#写字节
# with open('../res/temp', 'a') as file:
#     if(file.writable()):
#         file.write("go go go")




# '''
# io模块 StringIO对象
# '''
# import io
# output = io.StringIO()
# output.write('First line.\n')
# print('Second line.', file=output)
# contents = output.getvalue()
# print(contents)
# output.close()


# '''
# io模块 BufferedReader对象
# '''
# with open('res/temp', 'rb', buffering=1024) as file:
#     pass


