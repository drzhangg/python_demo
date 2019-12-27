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


def printinfos (arg1,*var):
    print('输出：')
    print(arg1)
    print(var)

printinfos(10,20,30)


def printinfoss(arg1,**avr):
    print("输出：")
    print(arg1)
    print(avr)

printinfoss(1,a=2,b=3)

print('{}网址："{}!"'.format('菜鸟教程','www.baidu.com'))

print('{0}和{1}'.format('google','apple'))
print('{1}和{0}'.format('google','apple'))
print('{name}网址：{site}'.format(name='菜鸟教程',site='www.baidu.com'))


table = {'google':1,'runoob':2,'baidu':3}
for name,number in table.items():
    print('{0:10} ==> {1:20d}'.format(name,number))


# str = input("请输入：")
# print("你输入的内容：",str)

file = open("demo1.py","r")
file.write()
print(file)


fileread = file.read()
print(fileread)

