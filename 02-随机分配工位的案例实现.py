# 练习：把给老师随机分配工位的案例实现
# 一个学校，有三个办公室，现在有八位老师等待工位的分配，请编写程序，完成随机分配

# 每个办公室都是一个小列表，为了管理三个小列表更加方便，可以使用列表嵌套
import random
office_list = [[], [], []]
teachers = ["张三","李四","王五","赵六","冯七","不知道","是谁","撒啊"]

for teacher in teachers:
    # 随机生成小办公室的下标 index
    index = random.randint(0,2)
    # 根据随机生成的小办公室下标，添加教师
    office_list[index].append(teacher)

print(office_list)