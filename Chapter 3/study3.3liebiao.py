cars = ['bmw','toyota','audi','subaru']
cars.sort()#sort方法对列表元素按首字母进行永久排序
print(cars)
cars.sort(reverse=True)#向sort方法传递参数 reverse=True将列表元素永久性按首字母倒序
print(cars)

#使用函数sorted()在不改变列表本身排序的情况下对列表元素临时按首字母排序
cars1 = ['bmw','toyota','audi','subaru']
print("Hrer is hte original list:")
print(cars1)
print("\n下面对列表元素临时排序:")
print(sorted(cars1))
print("\n下面是列表本身的元素顺序:")
print(cars1)

#使用 reverse()方法可将列表元素按加入时间倒序
cars2 = ['bmw','toyota','audi','subaru']
cars2.reverse()
print("\n下面将列表元素倒序输出：")
print(cars2)

#使用函数len()可获悉列表元素数
print('\n下面获取列表元素数量：')
print(len(cars2))