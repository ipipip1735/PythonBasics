import collections
import json

# '''
# json模块 JSONEncoder对象
# '''
# dict = {'one':11, 'two':[222, "go"], 'three':'333'}
# encoder = json.JSONEncoder()
# jsonString = encoder.encode(dict)
# print(jsonString)



# '''
# json模块 JSONDecoder对象
# '''
# def hook(arg):
#     print('arg is ', arg)
# decoder = json.JSONDecoder()
# # decoder = json.JSONDecoder(object_hook=hook, parse_float=hook, parse_int=hook, parse_constant=hook, strict=True, object_pairs_hook=hook)
# jsonCode = decoder.decode(jsonString)
# print(jsonCode)




# '''
# json模块 dumps()
# '''
jsonObject = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(jsonObject)

# '''
# json模块 load()
# '''
dict = json.loads(jsonObject)
print(dict)