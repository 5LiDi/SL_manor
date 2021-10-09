magicians = ['honda','yamaha','suzuki']
for magician in magicians:
    print(magician)#如果此行未缩进，会提示expected an indented block：需要一个缩进块

for magician in magicians:
    print(f"{magician.title()},这是魔术师")
    print(f"我们期待你的表演，{magician.title()}.\n")


massage = ['我是时磊']
print(massage)#如果此行缩进，就会导致多余的缩进报错

for magician in magicians:
    print(f"{magician.title()},这是魔术师")
    print(f"我们期待你的表演，{magician.title()}.\n")
print('感谢你们的表演！')#如果此行缩进，会导致逻辑错误，但是可能不会报错

for magician in magicians:#如果for循环语句后缺少冒号，会报错：invalid syntax（无效的语法）
    print(f"{magician.title()},这是魔术师")