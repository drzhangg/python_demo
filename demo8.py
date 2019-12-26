# coding: UTF8
def printstr(str):
    '打印传入的字符串到标准显示屏上'
    print (str)
    return


printstr('zhang')
printstr("调用函数")


def changme(mylists):
    mylists.append([1, 2, 3])
    print ('函数内取值：', mylists)
    return


mylist = [11, 12, 13]
changme(mylist)
print (mylist)


def printInfo(name, age):
    print ('Name:', name)
    print ('Age:', age)
    return


printInfo(age=24, name='zhang')


def printinfo (arg1,*vartuple):
    print ("输出：")
