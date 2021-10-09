age = 17
#if语句
if age >= 18:
    print(f"{age}这个年龄符合条件")
#if-else语句
if age >= 18:
    print(f"{age}这个年龄符合条件")
else:
    print("对不起，你的年龄不符合规定")
#if-elif-else多重判断语句
age2 = 33
if age2 < 4:
    print("免费")
elif age2 >=4 and age2 <= 18:
    print("收费25元")
else:
    print("收费40元")

#if-elif-else简洁用法
age3 = 70
if age3 < 4:
    price = 0
elif age3 <= 18:
    price = 25
elif age3 < 65:
    price = 40
else:
    price = 20
print(f"您应付{price}元")
