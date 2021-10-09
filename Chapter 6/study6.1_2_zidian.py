alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"你刚才赚到{new_points}分数")

#使用一下代码在指定字典中添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#在空字典中添加键值对
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

#修改字典中的值
alien_2 = {'color':'green'}
print(f"外星人的当前颜色为{alien_2['color']}")
alien_2['color'] = 'yellow'
print(f"外星人现在为{alien_2['color']}")

#更有意思的联系
alien_3 = {'x_position': 1,'y_position': 25,'speed': 'medium'}
print(f"原始的x_position:{alien_3['x_position']}")
#更改字典中speed的值
alien_3['speed'] = 'fast'
#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed']  == 'medium':
    x_increment = 2
else:
    #这个外星人的移动速度肯定很快
    x_increment = 3
#新位置为旧位置加上移动距离
alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"新的x_position为：{alien_3['x_position']}")

#使用del删除字典中的键值对
alien_4 = {'color': 'green','points':3}
print(alien_4['color'])
del alien_4['points']
print(alien_4)

#由类似对象组成的字典
favorite_man = {
    '奶娃':'李艳',
    '阿哲':'谢佳璇',
    '时磊':'王伊梦',
    '范逼':'西瓜妹妹'
}
print(favorite_man)
man = favorite_man['范逼']
print(f"范逼 最喜欢的是{man}")

alien_5 = {'color': 'green','points':3}
#print(alien_5['speed']) #输出字典中不存在的键会报错
speed_value = alien_5.get('speed','这个键不存在')
print(speed_value)