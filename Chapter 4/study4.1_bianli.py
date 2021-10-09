#for循环
liebiaos = ['honda','yamaha','suzuki']
for liebiao in liebiaos:
    print(liebiao)

cats = ['yingduan','lanmao','bosi']
dogs = ['bianmu','qiutian','demu']
for cat in cats:
    print(cat)
for dog in dogs:
    print(dog)

#for循环内加入f字符串输出任意组合内容
magicians = ['honda','yamaha','suzuki']
for magician in magicians:
    print(f"{magician.title()},这是魔术师")
    print(f"我们期待你的表演，{magician.title()}.\n")
print('感谢你们的表演！')