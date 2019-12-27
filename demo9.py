import sys

try:
    f = open('demo9.py')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("os error:{0}".format(err))
except ValueError:
    print("could not convert data to an integer")
except:
    print("unexpected error:",sys.exc_info()[0])
    raise


x = 10
if x > 5:
    raise Exception('x不能大于5,x的值为：{0}'.format(x))