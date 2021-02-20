# 练习: 循环显示每个办公室的信息(人数和老师成员)
teacher_list = [['李四', '赵六', '撒啊'], ['张三', '不知道'], ['王五', '冯七', '是谁']]
num = 1
for teachers in teacher_list:
    print("当前是第%d个办公室，人数为：%d" % (num, len(teachers)))
    num += 1
    for teacher in teachers:
        print(teacher)
