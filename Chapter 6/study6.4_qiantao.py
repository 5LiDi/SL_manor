#嵌套-将字典嵌套在列表中
user_0 = {'name':'奶娃','age':24,'sex':'男'}
user_1 = {'name':'静哥','age':25,'sex':'女'}
user_2 = {'name':'范逼','age':25,'sex':'男'}
user_3 = {'name':'小可爱','age':23,'sex':'女'}
users = [user_0,user_1,user_2,user_3,]
for user in users:
    print(user)
print("\n")

#使用range()方法自动创建指定数量的内容
#创建一个外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_num in range(30):
    new_alien = {'姓名':'siri','颜色':'绿色','分数':3}
    aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("....")
#显示创建了多少外星人
print(f"总共出现了{len(aliens)}个外星人")