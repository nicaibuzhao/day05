
# 练习: 定义一个字典，person_dict = {"name": "宋江", "sex": "男", "age": 30}
person_dict = {"name": "宋江", "sex": "男", "age": 30}
# 1.遍历字典中的每一个key  
for key in person_dict.keys():
    print(key)
# 2.遍历字典中的每一个value
for value in person_dict.values():
    print(value)
# 3.遍历字典中的每一项数据(item)
for item in person_dict.items():
    print(item)

# 4.遍历字典中的每一项数据key和value 
for k,v in person_dict.items():
    print(k,v)