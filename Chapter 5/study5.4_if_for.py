pisas = ["土豆","番茄","青椒"]
for pisaing in pisas:
    print(f"添加{pisaing}")
print("遍历列表")
print("\n")

for pisaing3 in pisas:
    if pisaing3 == "青椒":
        print("对不起，青椒售完了")
    else:
        print(f"添加{pisaing3}")
print("\n")

#----------------见第77页
zaocan = []
if zaocan:
    for zaocan1 in zaocan:
        print(f"您点了：{zaocan1}")
    print("请等待制作完成")
else:
    print("您确定不点吃的吗？")
print("\n")

#-----------------见第78页
available_toppings = ["蘑菇","橄榄","青椒","意大利香肠","菠萝","外星人"]
requested_toppings = ["蘑菇","炸薯条","外星人"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"您点了：{requested_topping}")
    else:
        print("抱歉，没有您点的配料")
print("正在为您制作")