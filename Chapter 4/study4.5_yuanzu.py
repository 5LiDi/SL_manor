yuanzu = (9,11)
print(yuanzu[0])
print(yuanzu[1])
#yuanzu[0] = 83  #--------以下验证元组不支持赋值
print(yuanzu)

yuanzu2 = (9,)  #---------创建元组时，无论有几个元素，元素后面都必须带逗号
print(yuanzu2)
#---------下面使用for循环遍历元组
yuanzu3 = (2,3,45,23)
for yuanzu3s in yuanzu3:
    print(yuanzu3s)

#练习
fandian = ('凉拌黄瓜','宫保鸡丁','红烧茄子')
for fandians in fandian:
    print(fandians)
print("\n")
fandian = ('鲍鱼','鱼翅')#-----------此位置输出有误，待解决
for fandian2 in fandian:
    print(fandian2)
    print(fandians)
