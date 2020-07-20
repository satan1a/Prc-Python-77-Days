print("Hello")

## The different division
num = 10/3

num_1 = 10//3

print(num)
print(num_1)

## Method about unicode
## Python的字符串类型是str，在内存中以Unicode表示
unicode_char = ord("A")
print(unicode_char)

char_unicode = 66
print(chr(char_unicode))

## str vs. bytes
## Python的字符串类型属于str，一个字符对应若干个字节。但在网络或者本地磁盘中，数据是以字节流的形式存在，可以看作是一个个byte，
## 所以，在处理网络数据流或者本地数据流时，要对字符进行encode，表示为b前缀

str_var = "ABC"
bytes_var = b"ABC"

print(str_var)
print(bytes_var)

## Method about for formatting

print("{0} is a big boy, he is {1} years old, his hight is {2:.2f}".format("Tom", 20, 175.5555))


## List vs. tuple vs. dict

### list is a orderd collection, u can insert, delete, modify at anytime

names = ['Tom', 'Jack', 'Lucy']

print(len(names))

print(names[0])

names.append('Alen')

names.insert(1, "Jerry")

names.append('Jason')

names.pop()

for name in names:
    print(name)

mix_list = ["name", True, 123, 3.1415926, ["CC", "LL"]]

print("{0}".format("="*20))

for element in mix_list:
    print(element)

print("{0}".format("="*20))

print(mix_list[4][1])

### tuple is a permanent ordered collection, u can't insert or delete or modify

logic_words = (True, False)
print("{0}".format("="*20))
print(logic_words[1])
print(logic_words.index(True))


print("{0}".format("="*20))
one_num = (1)
print(type(one_num))

one_num_tuple = (1,)
print(type(one_num_tuple))
print(one_num_tuple)

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))



## Condition Judgement
print("{0}".format("="*20))

### if遇到符合的条件后，自动忽略之后（同级）的判断
for name in ["Tom", "CC", "Wisconsion"]:
    len_name = len(name)
    if len_name > 5:
        print("Long Name")
    elif len_name >= 3:
        print("Standard Name")
    else:
        print("Short Name")



## Method input()
print("{0} \nPlease input a number:".format("="*20))

### 注意，input方法输入数字等都是str类型
number_string = input()
print("The number is {0}, the type is {1}".format(number_string, type(number_string)))


## dict
print("{0}".format("="*20))

name_dict = {"Tom":20, "Jerry":18, "Lucy":16}

### add
name_dict["Jason"] = 38
print(name_dict["Jason"])

### delete
name_dict.pop("Jason")
for key in name_dict:
    print(name_dict[key])

### modify
name_dict["Tom"] = 21

### read
print(name_dict.get("Tom"))


print("{0}".format("="*20))

### none
print(name_dict.get("xiba"))

### dict的注意点

"""
优点：
- 查找和插入的速度快
缺点：
- 内存占用大
注意：
- key必须是不可变对象，建立字典索引是靠对key的hash算法的
"""

## set
## 等同于数学上的不重合、无需的集合概念，因此也可以做交集、并集等操作
print("{0}".format("="*20))

### define 1
name_set_1 = set(["Tom", "Jerry", "Alen", "Alen"])
### define 2
name_set_2 = {"Alen", "Buddy"}
print(name_set_1)
print(name_set_2)

### add
name_set_2.add("Amy")
name_set_2.add("Jason")
print(name_set_2)

### delete
name_set_2.remove("Jason")
name_set_2.discard("No One")
print(name_set_2)


### modify
### 没有索引形式的修改，因为其具有无序的性质

