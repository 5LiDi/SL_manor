friend = ["奶娃","范万亮","秀秀","猫","鹏"]
print(friend[0:3])  #输出第1到第3的元素；见-4.4.1
print(friend[1:3])  #输出第2到第3的元素
print(friend[:3])   #没有第一个索引的情况下，将自动从列表0的位置开始输出
print(friend[2:])   #没有第二个索引的情况下，将从第一个索引到列表结尾
print(friend[-2:])  #负数表示从列表倒数第几个数开始
#-----------使用for循环遍历列表切片；见-4.4.2
print('这些是我最好的朋友:')
for friends in friend[0:2]:
    print(friends.title())
#-----------复制列表内容；见-4.4.3
my_food = ['汉堡','包子','洋芋不拉']
f_food = my_food[:]
print('这是我喜欢的食物：')
print(my_food)
print('我朋友也喜欢这份食物：')
print(f_food)
my_food.append('凉皮')
f_food.append('饸烙面')
print(my_food)
print(f_food)

