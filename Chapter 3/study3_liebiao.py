autocycle = ['wuji','bentian','baoma','chunfeng']
print(autocycle)    #输出列表内容
print(autocycle[3]) #输出列表指定位置的内容
print(autocycle[3].title()) #对输出的内容使用方法
print(autocycle[-1])    #负数表示列表倒数的内容

wish = f"I want a {autocycle[-1].title()}"  #结合变量赋值、f字符串、列表定位输出内容
print(wish)