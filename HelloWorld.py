print("Hello,World!")

# 单行注释与多行注释
'''
行与缩进
   python中使用缩进来表示代码块，不需要使用大括号
   缩进的空格数可变，但是同一个代码块中的语句必须包含相同的缩进空格数
'''
if True:
    print("True")
else:
    print("False")


'''
python中的基本数据类型:
    数字（Number）类型：int bool float complex(复数)
    字符串(string):单引号和双引号完全一样 转义符 \ 
                   使用r可以让反斜杠不发生转义
                   按照字面意义级联字符串 "this""is""string" 会被自动转换为this is string
                   可以用+运算符连接字符串 用*运算符重复字符串
                   字符串索引 从左往右以0开始 从右往左以-1开始
                   字符串不可变
                   没有单独的字符类型
                   字符串截取如下

'''
# python文件类型
# 源代码：以py为扩展名，由Python程序解释，不需要编译
# 字节代码:Python源文件经编译后生成的扩展名为pyc的文件   编译方法-- import py_compile    py_compile.compile("hello.py")
# 优化代码：经过优化的源文件，扩展名为".pyo"  python -O -m py_compile hello.py;

'''
python中的多行语句用反斜杠\来实现
## 在[] {} ()中的多行语句不需要使用反斜杠
total = item_one + \
        item_two + \
        item_three

'''
# python中的字符串基本操作
str = 'GoodLuck'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + '你好')
print('-----------------')
print('hello\ngoodluck')
print(r'hello\ngoodluck')

