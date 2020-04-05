import logging
import logging.handlers
import logging.config
import io

# '''
# logging模块
# '''
# 创建Logger
# logger = logging.getLogger()
# # logger.setLevel(logging.DEBUG)
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')

# 增加处理器
# logger = logging.getLogger()
# fileHandler = logging.FileHandler('a.log')
# formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
# fileHandler.setFormatter(formatter)#增加格式化对象
# logger.addHandler(fileHandler)#增加处理器
# logger.addHandler(logging.StreamHandler())
# logging.error('xxx')


# 增加Logger级别过滤器
# logger = logging.getLogger()
# logger.addFilter(logging.Filter('A'))#增加内置过滤器，如果返回False，则所有处理器都将被过滤
# logger.addHandler(logging.FileHandler('a.log'))
# logger.addHandler(logging.StreamHandler())
# logging.error('[error]xxx')


# 增加Handler级别过滤器
# logger = logging.getLogger()
# handler = logging.FileHandler('a.log')
# handler.addFilter(logging.Filter('A'))#此过滤器仅作用域本Handler，不会影响其他Handler
# logger.addHandler(handler)
# logger.addHandler(logging.StreamHandler())
# logging.error('[error]xxx')


# 过滤链，链中只要有一个返回False，所有处理器都将被过滤
# class OneFilter(logging.Filter): #自定义Filter对象
#     def filter(self, record: logging.LogRecord) -> int:
#         print(record)
#         return True
#
# logger = logging.getLogger()
# logger.addFilter(OneFilter())#增加自定义过滤器
# logger.addFilter(logging.Filter('A'))#增加内置过滤器
# logger.addHandler(logging.FileHandler('a.log'))
# logger.addHandler(logging.StreamHandler())
# logging.error('[error]xxx')


# 日志继承
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[root] %(message)s'))
logging.getLogger().addHandler(handler)#给根Logger增加处理器

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[A1] %(message)s'))
logging.getLogger('A').addHandler(handler)#给父Logger增加处理器
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[A2] %(message)s'))
logging.getLogger('A').addHandler(handler)#给父Logger增加处理器

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[A.B] %(message)s'))
logging.getLogger('A.B').addHandler(handler)#给子Logger增加处理器
# logging.getLogger('A.B').propagate = False
logging.getLogger('A.B').error('go')


# '''
# logging.handlers模块
# '''
# 控制台日志
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# # logger.addHandler(logging.StreamHandler())
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')


# 内存日志
# logger = logging.getLogger()#获取根Logger
# logger.setLevel(logging.DEBUG)#设置根Logger的日志级别
#
# stringIO = io.StringIO() #创建字符串输出流
# logger.addHandler(logging.StreamHandler(stringIO))#增加控制器
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')
#
# print(stringIO.getvalue())#取出输出流中的内容，并打印


# 文件日志
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.FileHandler('a.log'))
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')


# 日志滚动
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.handlers.RotatingFileHandler('a.log', maxBytes=1024, backupCount=2))
# for i in range(1024):
#     logging.debug('[debug]' + str(i))
#     logging.info('[info]' + str(i))
#     logging.warning('[warning]' + str(i))
#     logging.error('[error]' + str(i))
#     logging.critical('[critical]' + str(i))


# 根据时间间隔滚动日志
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.handlers.TimedRotatingFileHandler('a.log', when='s', interval=2, backupCount=2))
# for i in range(1024):
#     logging.debug('[debug]' + str(i))
#     logging.info('[info]' + str(i))
#     logging.warning('[warning]' + str(i))
#     logging.error('[error]' + str(i))
#     logging.critical('[critical]' + str(i))


# 配置根Logger
# 方式一
# logging.basicConfig(handlers=[logging.StreamHandler()], level=logging.DEBUG, datefmt='%Y-%m-%d', format='{asctime} - {name} - [{levelname}] - {message}', style='{')
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')

# 方式二
# logging.basicConfig(level=logging.DEBUG, filename='a.log')
# logging.debug('[debug]xxx')
# logging.info('[info]xxx')
# logging.warning('[warning]xxx')
# logging.error('[error]xxx')
# logging.critical('[critical]xxx')


# 方式三
# with io.StringIO()as stream:
#     logging.basicConfig(level=logging.DEBUG, stream=stream)
#     root = logging.getLogger()
#     logging.debug('[debug]xxx')
#     logging.info('[info]xxx')
#     logging.warning('[warning]xxx')
#     logging.error('[error]xxx')
#     logging.critical('[critical]xxx')
#     print(stream.getvalue())

# '''
# logging模块 Formatter对象
# '''
# 创建格式化工具
# logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='XX', args=None, pathname=None, lineno=None, exc_info=None)
# fmt = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
#
# # logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='XX', args=None, pathname='onePath/xx', func='oneFun', lineno=999, exc_info=None)
# # fmt = logging.Formatter('%(process)d - %(thread)d - %(threadName)s - %(lineno)d - %(pathname)s - %(filename)s - %(funcName)s')
# log = fmt.format(logRecord)
# print(log)

# 使用参数
# logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='arg is %d', args=(1,), pathname=None, lineno=None, exc_info=None)
# fmt = logging.Formatter('%(message)s')
# log = fmt.format(logRecord)
# print(log)


# 使用格式化风格
# # logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='go go go', args=None, pathname=None, lineno=None, exc_info=None)
# logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='%d X %d', args=(1,2), pathname=None, lineno=None, exc_info=None)
# fmt = logging.Formatter('[{levelname}] - {message}', style='{') #风格为{，代表String.format()方法格式化
# log = fmt.format(logRecord)
# print(log)


# 使用模板风格
# logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='%d X %d', args=(1,2), pathname=None, lineno=None, exc_info=None)
# fmt = logging.Formatter('[$levelname] - $message', style='$')
# log = fmt.format(logRecord)
# print(log)


# 使用时间格式
# logRecord = logging.LogRecord(name='one', level=logging.ERROR, msg='%d X %d', args=(1,2), pathname=None, lineno=None, exc_info=None)
# fmt = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d')
# log = fmt.format(logRecord)
# print(log)




# '''
# logging.config模块
# '''
# logging.config.fileConfig('logging.conf')#加载配置文件
# logger = logging.getLogger("A")
# logger.debug('[debug]xxx')
# logger.info('[info]xxx')
# logger.warning('[warning]xxx')
# logger.error('[error]xxx')
# logger.critical('[critical]xxx')
