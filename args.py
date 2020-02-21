#什么是*args
# def add(*args):
#     for name in args:
#         print("i love "+name)
#
# add('魏颖','许蕊','盛含章')

#什么是**kwargs
# def m1(*args,**kwargs):
#     print('the type of args is',type(args))
#     print('the type of kwargs is',type(kwargs))
# m1()
#可以看到args的类型是元组
#而kwargs的类型是字典
# dic_huxun={'age':'22 years old','height':'182cm','name':'崔虎巡','weight':'75kg'}
# for k,v in dic_huxun.items():
#     print(k,':',v)
#
def somebody_dic(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)

somebody_dic(name='魏颖',age='22 years old')
