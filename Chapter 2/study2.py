#.title方法将首字母大写
name = "address lovewym"
print(name.title())
name1 = "SHILEI LOVE WANGYIMENG"
print(name1.title())

name = "Shilei Love WANGYIMENG"
print(name.upper()) #upper方法将所有字母大写
print(name.lower()) #lower方法将所有字母小写

first_name = "时"
last_name = "磊"
full_name = f"{first_name}{last_name}"  #f字符串：可以拼接变量
print(full_name)
print(f"王伊梦，喜欢{first_name}{last_name}")
print(f"Hello,{name.title()},{name1.lower()}")  #f字符串：可以字符+变量.方法

print("我是时磊:\n\t我需要告诉你一件事情\n\t代表换行代表制表符")   #\t制表符 \n换行

kongbai = "'python '         "
print(kongbai)
print(kongbai.rstrip())     #.rstrip()去除末尾空格
d_kongbai = kongbai.rstrip()
print(d_kongbai)

kongbai2 = "   python   "
kongbai3 = kongbai2.rstrip()
print(kongbai3)
kongbai4 = kongbai2.lstrip()    #.lstrip()去除前面空格
print(kongbai4)
kongbai5 = kongbai2.strip()     #.strip()去除首尾空格
print(kongbai5)

test1 = "hello eric"
test2 = "woule you like to learn some Python today"
print(f"{test1.title()},{test2}?")

a_name = "shi LEI"
print(f"{a_name.lower()}\n{a_name.title()}\n{a_name.upper()}")
print('Albert Einstein once said,"A person who never made a mistake never tried anything new"')