# '''
# 只有类Unix系统才能os.fork，Windows无法fork，下面的代码必须在Linux上执行
# '''
'''分叉'''
# #!/usr/bin/env python3
# import os
# import time
#
# print('os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))
#
# if (os.fork() == 0):  # 子进程中执行
#     print('son|os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))
#     for i in range(4):
#         print('go')
#         time.sleep(1)
#
# else:  # 当前进程（即父进程）中执行
#     print('father|os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))
#     os.wait()
#     for i in range(4):
#         print('come')
#         time.sleep(1)


'''孵化'''
## ! /usr/bin/env python3
# import time, os
# from multiprocessing import Process, set_start_method
#
# def fn():
#     time.sleep(2)
#     print('os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     print('start|os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))
#     p = Process(target=fn)
#     set_start_method('spawn')
#     p.start()
#     p.join()
#     print('end|os.getpid() = %d, os.getppid() = %d' % (os.getpid(), os.getppid()))


# '''
# Windows上使用Process
# '''
# import time
# from multiprocessing import Process, Pool
# import os
#
# def runnable(arg):
#     time.sleep(1)
#     print('~~Run~~|arg=%s, os.getpid()=%s, os.getppid()=%s' % (arg, os.getpid(), os.getppid()))

# 方法一
# if __name__ == '__main__':
# r = lambda: print('~~Run~~')
# p = Process(target=runnable, args=('one',))
# p.start()
# print('os.getpid()=%s, os.getppid()=%s' % (os.getpid(), os.getppid()))


# 方法二：使用进程池
# if __name__ == '__main__':
#     r = lambda: print('~~Run~~')
#     p = Pool(4)
#     for i in range(3):
#         p.apply_async(runnable, args=(1,))
#     p.close()
#     p.join()
#     # time.sleep(4)
#     print('os.getpid()=%s, os.getppid()=%s' % (os.getpid(), os.getppid()))


# 方法三：使用进程池
import time, multiprocessing, os

def runnable(arg):
    time.sleep(1)
    print('~~Run~~|arg=%s, os.getpid()=%s, os.getppid()=%s' % (arg, os.getpid(), os.getppid()))
    return arg + 1

if __name__ == '__main__':
    p = multiprocessing.get_context('spawn').Pool()
    r = p.map(runnable, [1,3,5])
    print(r)


# '''
# 进程间通信
# '''

# 使用Queue
# import os
# from multiprocessing import Process, Queue, Pipe
# def runnable(q):
#     q.put([42, None, 'hello'])
#     print('~~Run~~|q=%s, os.getpid()=%s, os.getppid()=%s' % (q, os.getpid(), os.getppid()))
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=runnable, args=(q,)).start()
#     print('q.get() =', q.get())
#     print('os.getpid()=%s, os.getppid()=%s' % (os.getpid(), os.getppid()))


# 使用Pipe
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     print(parent_conn)
#     print(child_conn)
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     p.join()
