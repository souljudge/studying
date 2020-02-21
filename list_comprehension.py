#list comprehension 列表解析式
#list生成新list的过程就是list comprehension的一种
#我的需求：从0-10的数字分别乘以2，然后放到新的列表里

# newlist=[]
# for i in range(11):
#     newlist.append(i*2)
#
# print(newlist)

# print([i*2 for i in range(11)])
# #这个就是列表解析式写法，将4行代码浓缩为1行

list=['崔虎巡','崔建军','罗乃霞','罗小凡','罗乃将']
# emptylist=[]
# for name in list:
#     if name.startswith('崔'):
#         emptylist.append(name)
# print(emptylist)
print([name for name in list if name.startswith('崔')])
