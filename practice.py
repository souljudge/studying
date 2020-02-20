
#my_list uses square bracket列表使用方括号

#list is mutable while tuple is inmutable
#列表可变而元组不可变

#Dictionary
myDic={"key":"value","key2":"value2"}
myPhones={"iphone X":"1000$","HUAWEI MATE 20":"600$"}
#how to acquire data in the dictionary
iphone_price=myPhones["iphone X"]
print(iphone_price)
print("iphpne X price:"+iphone_price)
# and if the iphone X depreciate,you want to change its price，what should you do
#如果说iPhoneX 贬值了，你想改变它的价格，你该怎么做？
#change key value
myPhones["iphone X"]="900$" #you can assign a string to the varaible in the dictionary directly
print(myPhones)

#clear the dictionary
myPhones.clear()
print(myPhones)