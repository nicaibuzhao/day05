# 练习1：定义一个元组类型的变量, 分别使用for循环和while循环遍历元组。
tup = (1, 2, 3, 5)
for i in tup:
    print(i)

num = 0
while True:
    if num < len(tup):
        print(tup[num])
        num += 1
