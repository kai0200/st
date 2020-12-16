# 操作说明
$ cp *pdf files
$ cd pdf2xlsx_table
$ sh run.sh
$ cd text
$ ls out.txt

# 安装 pdf2xlsx_table

1. 安装python3
yum install python3
或参考官网安装说明

2. 安装bs4 pdftotree, 实现pdf 转html
$ python3 -m pip install pdftotree
$ which pdftotree   # 确认是否可以找到pdftotree
$ python3 -m pip install bs4
需要BeautifulSoup 支持

3. 安装java
pdftotree 在运行期间可能需要java支持

4. 安装其他python需要的包
如果运行期间遇到缺少其他包
$ python3 -m pip install [包的名字]


# 使用

1. 把需要一次性导出的pdf文件放入files文件目录

2. 运行run.sh
$ cd pdf2xlsx_table  # 注意一定要在这个目录下运行命令
$ sh -x run.sh

3. files 目录说明
- 放入的文件名不能有空格
- run.sh 运行结束以后会在files 目录里生成同名的.html文件
- out.xlsx 为最后的结果文件

4. xlsx 目录
- out.html 为合并后的html文件
- out.xlsx 为输出的xlsx文件，这是最后想要的结果文件


5. 更换下一批文件就把files 放入pdf文件即可，原files 文件改名
