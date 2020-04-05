import collections

# '''
# collections模块 ChainMap对象
# '''
# dictOne = {'one':111, 'two':222}
# dictTwo = {'two':999, 'three':333}
# chainMap = collections.ChainMap(dictOne, dictTwo)
# list = list(chainMap)#导出key
# print(list)
# dict = dict(chainMap)#导出map
# print(dict)

#复制
# dictOne = {'one':111, 'two':222}
# dictTwo = {'two':999, 'three':333}
# chainMap = collections.ChainMap(dictOne, dictTwo)
# print(chainMap)
#
# s = chainMap.new_child({'four':444})
# print(s)
# print(chainMap)


#父节点
# chainMap = collections.ChainMap({'one':111},  {'two':222, 'three':333}, {'four':444})
# # chainMap = collections.ChainMap({'one':111},  {'two':222, 'three':333}, {'four':444})
# print(chainMap.parents) #返回除首dict以外所有dict




#更新
# dictOne = {'one':111, 'two':222}
# dictTwo = {'two':999, 'three':333}
# chainMap = collections.ChainMap(dictOne, dictTwo)
# print(chainMap)
# d = dictOne.update({'one':888})
# print(chainMap)

#转化为List
# dictOne = {'one':111, 'two':222}
# dictTwo = {'two':999, 'three':333}
# chainMap = collections.ChainMap(dictOne, dictTwo)
#
# list = chainMap.maps #maps属性就是本对象的List版本
# print(chainMap.maps)
# print(list)
#
# dictOne.update({'four':444})
#
# print(chainMap.maps)
# print(list)




# '''
# collections模块 dequeue对象
# '''
# q = collections.deque([11])
# q.append(12)
# print(q)
#
# q.extend([23,28])
# print(q)
#
# q.extendleft([31,32])
# print(q)
#
# print(q.pop())
# print(q)
# print(q.popleft())
# print(q)

# q.rotate(1)
# print(q)
# q.rotate(2)
# print(q)