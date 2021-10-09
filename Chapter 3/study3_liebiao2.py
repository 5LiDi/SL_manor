motorbike = ['honda','chunfeng','BWM','wuji']
print(motorbike[1])
motorbike[-1] = 'dihao' #修改列表中的元素
print(motorbike)

print('\n')
#.append('元素名')给列表后面添加元素
motorbike.append('ducati')
print(motorbike)

print('\n')
#.append('元素名')给空列表添加元素
tooto = []
tooto.append('日式')
tooto.append('传统')
tooto.append('卡布其字体')
print(tooto)

print('\n')
#.insert（元素位置,'元素名'）给列表任意位置添加元素
motorbike.insert(0,'ducati')
print(motorbike)

print('\n')
#del 语句删除列表内任意位置的元素 [数字代表元素位置]
del motorbike[-1]
print(motorbike)

print('\n')
#pop()是将列表中最后一个元素顶出去，可以将该元素赋值给其他变量（该方法不同于del方法，并没有将元素彻底删除，只是将元素从列表中移出
car = ['奔驰','宝马','法拉利','保时捷']
print(car)
pop_car = car.pop()
print(car)
print(pop_car)

print('\n')
#利用pop方法+f字符串方法输出内容
motuoche = ['honda','chunfeng','BWM','wuji']
last_shop = motuoche.pop()
print(f"最后购买的摩托车是{last_shop.title()}")
#利用pop方法输出任意位置的元素
motu = ['honda','chunfeng','BWM','wuji']
suiyi = motu.pop(1)
print(f"我这辈子买的第一辆摩托车是{suiyi.title()}250的")
