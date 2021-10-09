user_0 = {
    'name':'奶娃',
    'age': 24,
    'sex': '男',
}
for key,value in user_0.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")

favorite_man = {
    '奶娃':'李艳',
    '阿哲':'谢佳璇',
    '时磊':'王伊梦',
    '范逼':'西瓜妹妹'
}
for name,man in favorite_man.items():
    print(f"{name}最喜欢的人是：{man}")

#.keys()方法可以只遍历字典中的所有键
for name2 in favorite_man.keys():
    print(name2)
print("\n")

friends = ['奶娃','秀秀']
for name3 in favorite_man.keys():
    print(f"哈喽，{name3}")
    if name3 in friends:
        gril = favorite_man[name3]
        print(f"\t{name3} 我知道你喜欢的是{gril}")
#使用.keys()确定某个人是否在遍历中
if '钩子' not in favorite_man.keys():
        print("钩子，不在字典中")
print("\n")

#使用sorted()方法对字典中的元素进行排序
favorite_man2 = {
    'nw':'李艳',
    'az':'谢佳璇',
    'sl':'王伊梦',
    'fb':'西瓜妹妹',
    'fb':'东瓜妹妹',
}
#遍历键
for name4 in sorted(favorite_man2.keys()):
    print(f"{name4},这是排序后的")
#遍历值
for girl in favorite_man2.values():
    print(f"{girl}是他们的女朋友")

