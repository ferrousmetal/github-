"""
正则表达式：
re 模块
re.match(pattern,string,flags=0)
pattern:匹配的规则
string：要匹配的字符
flags：匹配的方式，是否区分大小写或者多行匹配等
方式有：
    1.re.I忽略大小写
    2.re.M多行匹配，影响^和$
    3. re.match必须从头匹配,不好用
    4. re.search,全部查找但是只匹配第一个
    5. re.findall()找所有，把找到的元素全部存储到一个列表中。

"""
import re
# 从头开始匹配hello，大写也不行
print(re.match("hello","hello world"))
#忽略大小写
print(re.match("hello","Hello world",re.I))
print("————————————————————————————————————")
#匹配整个字符串，返回第一次找到的，
print(re.search("hello","Hello world",re.I))
print(re.search("he","ahello......world"))
print(re.search("he","ahello......heworld"))
#匹配所有的元素，返回一个列表
print(re.findall("he","aHello......world",re.I))
print(re.findall("he","ahello......world\naache"))#默认多行匹配
"""
匹配单个字符或数字
1. ".",匹配除了换行以外的仍以一个字符，
2. [内容]，字符集合，匹配括号中所包含的任意一个字符
3. [a-z]匹配a-z中的任意一个
4. [A-Z]匹配A-Z中的任意一个
5. [0-9]匹配任意一个数字
6. [0-9a-zA-Z]匹配任意的数字和字母
7. [0-9a-zA-Z_]匹配任意的数字和字母和下划线
8. [^hello]匹配除hello以外的任意字符
9. [^0-9] 匹配所有的非数字
10.\d 匹配数字效果更0-9
11.\D 匹配非数字
12.\w 匹配数字子母和下划线
13.\W 匹配非数字字母和下划线
14.\s 匹配的任意的空白符\t \n \r
15.\S 匹配任意的非空白符
"""
#任意一个字符串
print(re.match(".","hello....world"))
print(re.search(".","hello....world"))
print(re.findall(".","hello....world"))
print(re.match("[hello]","hello....world"))
print(re.search("[hello]","ahello....world"))
print(re.findall("[hello]","hello....world"))
print(re.match("[a-z]","hello...word"))
r"""
锚字符，边界字符
^匹配每一行的开头，和[]不是一个意思
$ 匹配每一行的结尾
\A只匹配每个字符的开头
\Z只匹配每个字符串的结尾
\b 匹配一个单词，也就是指单词和空格间的位置
"""
#^匹配每一行开头
print(re.search("^hello","hello 123 ... word"))
print(re.findall("^hello","hello 123 ... word",re.M))
#匹配每一行的结尾
print(re.search("hello$","hello 123 ... word hello\nhello"))
print(re.findall("hello$","hello 123 ... word \nhello",re.M))
#只匹配开头，re.M也不管用
print(re.search("\Ahello","hello 123 ... word hello\nhello",re.M))
#只匹配真个字符串，re.M也不管用
print(re.search("hello\z","hello 123 ... word hello\nhello"))
#匹配非单词
print(re.search("hello\B","hello 123 ... word hello\nhello"))
#多个字符
# 1.（xyz）匹配小括号内的x,y,z作为整体去匹配
# 2.x?匹配0个或任意一个x
# 3.x*匹配0个或者任意多个，换行除外
# 4.x+匹配至少一个x
# 5.x{n}匹配n个x
# 6.x{n,}匹配至少n个
# 7.x{n,m}匹配至少n个x，最多m个x
# 8.x|y 匹配X或Y
print(re.findall("l?","hello...world"))
print(re.findall("l*","hello...world"))
print(re.findall("l+","hello...world"))
print(re.findall("l{1,2}","hello...world"))
print(re.findall("l|h","hello...world"))
