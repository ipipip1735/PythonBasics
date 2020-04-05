# def do_local():
#     # global spam
#     nonlocal spam
#     spam = "local spam"
#
# do_local()
# print(globals())

spam = "111"
def do_local():
    spam = "22"
    def do_nonlocal():
        nonlocal spam
        spam = "3"
    do_nonlocal()
    print(spam)

do_local()
print(spam)