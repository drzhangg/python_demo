class myClass:
    """一个简单的类示例"""

    i = 12345
    def f(a):
        return 'hello'

# 实例化类
x = myClass()

print(x.i)
print(x.f())


class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.a = imagpart

x = Complex(3.0,-4.5)
print(x.r,x.a)



class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s 说：我%d岁了' %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    #复写父类的方法
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级"%(self.name,self.age,self.grade))

#另一个类
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s,我的工作是%s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)


#实例化类
p = people('zhang',23,150)
p.speak()


s = student('jerry',10,60,3)
s.speak()


test = sample('tom',25,70,5,'golang')
test.speak()



class Parent:
    def Method(self):
        print('父类方法')

class Children(Parent):
    def Method(self):
        print('重写子类方法')

ch = Children()
ch.Method()
super(Children,ch).Method()