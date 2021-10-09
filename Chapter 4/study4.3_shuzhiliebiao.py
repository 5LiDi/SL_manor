for value in range(1,6):#使用range函数可以生成一系列数值
    print(value)

for value2 in range(6):#range函数内输入一个参数6代表输出的长度
    print(value2)

num = list(range(5))#将range函数作为函数list的参数，输出的内容将为列表
print(num)

o_num = list(range(2,11,2))#第一个参数表示从2开始，第二个参数表示到11结束，第三个参数表示每次加2
print(o_num)

kong = []#创建空列表
for value3 in range(1,11):#遍历1-10内容
    square = value3 ** 2 #将遍历内容赋值给square
    kong.append(square) #在空列表后面附加上面算出来的内容；append：附加
print(kong)
#---------------下方代码简略了上面的赋值步骤，见-4.3.2
kk = []
for kks in range(1,16):
    kk.append(kks ** 2)
print(kk)
#---------------下面代码对列表内数值统计计算，见-4.3.3
digits = [1,2,3,4,5,6,7,8,11,9,10]
print(max(digits))
print(min(digits))
print(sum(digits))
#---------------下面代码为列表解析（更简化的代码），见-4.3.4
square2 = [value4 ** 2 for value4 in range(1,11)]
print(square2)