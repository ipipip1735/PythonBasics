# '''
# threading模块 Thread对象
# '''
import threading
import time


# 方法一：使用Callable对象
def c():
    t = threading.current_thread()
    while (True):
        print(t, t.is_alive(), sep=' - ')
        time.sleep(1)

def c(a, b, c):
    print(a, b, c)


# thread = threading.Thread(target=c)
thread = threading.Thread(target=c, args=[1, 2, 3])
thread.start()
# thread.run()#直接执行
print("go")
print(thread.is_alive())

# 方法二：重写run()方法
# class OneThread(threading.Thread):
#     def run(self) -> None:
#         t = threading.current_thread()
#         while (True):
#             print(t, t.is_alive(), sep=' - ')
#             time.sleep(1)
#
# thread = OneThread()
# thread.start()
# print("go")


# 守护线程
# def c():
#     t = threading.current_thread()
#     while (True):
#         print(t, t.isDaemon(), sep=' - ')
# threading.Thread(target=c, daemon=True).start()


# 线程ID
# def c():
#     t = threading.current_thread()
#     while (True):
#         print(t, t.ident, t.native_id, sep=' - ')
#         time.sleep(1)
#
# thread = threading.Thread(target=c)
# print(thread.ident)
# thread.start()
# # thread.run()
# print(thread.ident)


# 统计线程总数
# def c():
#     t = threading.current_thread()
#     while (True):
#         time.sleep(1)
#
# threading.Thread(target=c).start()
# threading.Thread(target=c).start()
# threading.Thread(target=c).start()
# print(threading.active_count())
# for t in threading.enumerate():
#     print(t)


# '''
# threading模块 Lock对象
# '''
# def c():
#     global x
#     t = threading.current_thread()
#     while (x < 20):
#         print(threading.current_thread(), x, sep=" - ")
#         lock.acquire()
#         x = x+ 1
#         lock.release()
#         time.sleep(1)
#
# x = 0
# lock = threading.Lock()
# threading.Thread(target=c).start()
# while (x < 20):
#     print(threading.current_thread(), x, sep=" - ")
#     lock.acquire()
#     x = x+1
#     lock.release()
#     time.sleep(1)


# 非阻塞
# def c():
#     time.sleep(1)
#     while (True):
#         print(threading.current_thread())
#         lock.acquire(blocking=False)
#         # lock.acquire()
#         time.sleep(1)
#         # lock.release()
#
#
# lock = threading.Lock()
# threading.Thread(target=c).start()
# while (True):
#     print(threading.current_thread())
#     lock.acquire()
#     time.sleep(1)
#     # lock.release()


# #使用with关键字
# def c():
#     time.sleep(1)
#     while (True):
#         print(threading.current_thread())
#         with lock:
#             time.sleep(1)
#
# lock = threading.Lock()
# threading.Thread(target=c).start()
# while (True):
#     print(threading.current_thread())
#     lock.acquire()
#     time.sleep(1)
#     lock.release()


# '''
# threading模块 RLock对象
# '''
# def c():
#     while (True):
#         time.sleep(6)
#         with lock:
#             print(threading.current_thread())
#
# lock = threading.RLock()
# threading.Thread(target=c).start()
#
# while (True):
#     time.sleep(1)
#     with lock:
#         print(threading.current_thread())

# 使用with关键字
# def c():
#     while (True):
#         time.sleep(1)
#         with lock:
#             print(1)
#             with lock:
#                 print(2)
#
# lock = threading.RLock()
# threading.Thread(target=c).start()
#
# while (True):
#     time.sleep(1)
#     lock.acquire()
#     print(0)
#     lock.release()


# # '''
# # threading模块 Condition对象
# # '''
# def c():
#     with condition:
#         print(2)
#         condition.wait()
#         print(3)
#
# condition = threading.Condition(threading.Lock())
# threading.Thread(target=c).start()
#
# with condition:
#     print(0)
#     # condition.notify()
#     print(1)


# # '''
# # threading模块 Semaphore对象
# # '''
# def c():
#     with semaphore:
#         print(1)
#         time.sleep(6)
#
# semaphore = threading.Semaphore(1)
# threading.Thread(target=c).start()
#
# with semaphore:
#     print(0)


# '''
# threading模块 Event对象
# '''
# def c():
#     print(1)
#     time.sleep(6)
#     event.set()
#
# event = threading.Event()
# threading.Thread(target=c).start()
#
#
# event.wait()
# print(0)


# '''
# threading模块 Timer对象
# '''
# def c():
#     print(0)
#     print(threading.current_thread())
#
# t = threading.Timer(2, c)
# t.start()
# print(t.isDaemon())


# # '''
# # threading模块 Barrier对象
# # '''
# def c(arg):
#     print('cccccc', arg)
#     print(threading.current_thread())
#     # if(arg == 2):
#     #     time.sleep(2)
#     barrier.wait()
#
#
# def b():
#     print('bbbb')
#     print(threading.current_thread())
# barrier = threading.Barrier(3, b)
#
# threading.Thread(target=c, args=[1]).start()
# threading.Thread(target=c, args=[2]).start()
#
#
# time.sleep(2)
# print(barrier.n_waiting, barrier.parties, sep=' - ')
# # barrier.wait()
# # barrier.reset()
# barrier.abort()
