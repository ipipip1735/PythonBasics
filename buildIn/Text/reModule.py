# # '''
# # re模块 match对象
# # '''
# import re
# match = re.search('a', 'abcd')
# print(match[0])
#
#
# # match = re.search('b.*f', 'abcdefg')
# # print(match.start())
# # print(match.end())
# # print('abcdefg'[1:6])
#
# match = re.search('(23).*(56).*(89)', '1234567890')
# # print(match.span(0))
# # print(match.span(1))
# # print(match.span(2))
# # print(match.span(3))
# print(match.string)
# print(match.pos)
# print(match.endpos)
# print(match.lastindex)
# print(match.lastgroup)
# print(match.re)


# '''
# re模块 findall()
# '''
# import re
# match = re.findall('(2)345(6)', '12345678901234567890')
# print(match)

# '''
# re模块 split()
# '''
import re
match = re.split('a', '12a34a56')
print(match)


#################################################



# '''
# string模块 BufferedReader对象
# '''
# import string
# t = string.Template('a is $a.')
# a = 'aaa'
# print(t.substitute(a=a))
# d = {'a':111}
# print(t.substitute(d))

from string import Template
print(Template('a is $a').substitute({'a':111}))