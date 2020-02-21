# file=open('huxun.txt')
# text=file.read()
# print(text)
# file.close()

with open('C:/Users/cuihuxun/Desktop/201907.txt')as f:
    print(f.read())

#使用with open xx(path) as xx(name),不需要在最后加入file.close()
#当前版本的主流是使用with open写法
#with open('document','r')第二个参数默认是r，即read，如果将参数改为‘w’，那么就是写入（write），‘w’会覆盖文档之前的内容
#如果第二个参数是‘a’，那么就将是额外添加，a对应append，下一行一般都是f.write(),括号内就是你要写入的内容，如果希望换行，
#不要忘记在最后加上'/n'