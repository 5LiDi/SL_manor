cars = ['bwm','audi','subaru','toyota']
#------使用for循环遍历列表，根据if条件输出相应结果
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())
