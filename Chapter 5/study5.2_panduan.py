#------ != 为不等于
name = "时磊"
if name != "奶娃":
    print("对不起，你不是奶娃")
else:
    print("您好，时磊")
#------判断符号；and（并且）、or（或）的区别
age_0 = 26
age_1 = 24
if age_0 >=27 and age_1 <=24:
    print("年龄正确")
else:
    print("年龄不符合")

if age_0 >=27 or age_1 <=24:
    print("年龄符合要求")
else:
    print("年龄不符合要求")

#使用in 判断该元素是否包含在列表中
pape = ["时磊","王伊梦","时璐阳"]
if "王伊梦" in pape:
    print("王伊梦是时磊家的")
else:
    print("王伊梦不是时磊家的")
#使用not in 判断元素是否不包含在列表中
friend = "奶娃"
if friend not in pape:
    print(f"{friend},你不属于时磊家")