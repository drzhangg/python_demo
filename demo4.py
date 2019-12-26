# coding: UTF8
var = 100
if (var == 100) : print "变量var的值为100"

print 'good bye'



count = 0
while count < 9:
    print 'this count is ' , count
    count += 1

print 'end'


for leterr in 'zhang':
    print '当前字母：' + leterr


fruits = ['banana','apple','orange']
for fruit in fruits:
    print '当前水果：',fruit

print range(len(fruits))

print range(5)

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

# for index in range(len(fruits)):