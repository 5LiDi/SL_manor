motuoche = ['honda','chunfeng','BWM','wuji']
#.remove()方法是根据值删除元素
motuoche.remove('BWM')
print(motuoche)

print('\n')
#将要删除的内容赋给新的变量，使用remove方法删除时用变量名，可以在后续输出删除的值
motuoche1 = ['honda','chunfeng','BWM','wuji']
too_motuo = 'BWM'
motuoche1.remove(too_motuo)
print(motuoche1)
print(f"{too_motuo.title()}摩托车太贵了，把它去掉。")

print('\n')
#课后练习
friend = ['奶娃','兴','小王王','范逼']
print(f"有机会请{friend[0]}吃饭")
friends = friend[0] + friend[1] + friend[2] + friend[3]
print(f"有机会请{friends}吃饭")
notfood = friend.pop(-1)
print(f"{notfood}不能来了 准备换个人")
friend.insert(0,"秀秀")
print(friend)
