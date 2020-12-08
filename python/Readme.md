# TIME LINE
|------------|---|
| 2020-10-20 | - |
| 入门       |

numbersList = [0, 1, 2, 3, 4, 5]

max()
min()
list(map(lambda x: x*x range(10)))

### vim 的帮助如何使用
```
可以使用 Ctrl + ] 跳转到光标所在的主题上，如果开启了鼠标，双击左键也可跳转
返回跳转前主题
使用 Ctro + o,可以返回浏览前主题
普通模式命令		:help x
可视模式命令	v_	:help v_u
插入模式命令	i_	:help i_<Esc>
命令行模式命令	:	:help :quit
命令行编辑	c_	:help c_<Del>
Vim 命令参数	-	:help -r
选项	'	:help 'textwidth'
正规表达式	/	:help /[
```

### spacevim 如何单行运行
SPC d e S	执行选中的文本
### vim 如何设置中文帮助 TODO

### mac 配置spacevim gui 字体
let g:spacevim_guifont='Knack\ Nerd\ Font:h12'

### 打开目录树
spc f t

### Vim(call):E900
升级neovim 到最新版
git 上下载最新版本，https://github.com/neovim/neovim/releases/
https://github.com/neovim/neovim/releases/download/nightly/nvim-linux64.tar.gz

```
tar xfzv nvim-linux64.tar.gz
sudo mv /usr/bin/nvim /usr/bin/nvim-backup
sudo cp -rp ./nvim-linux64/bin/nvim /usr/bin/
替换原来的老版本问题解决

```
这个问题发现找了两天的原因后来尝试用vim 启动和nvim启动后发现vim 启动没有问题。
所以升级新nvim发现问题解决

发现的目录有
~/.cache/vimfiles/repos/github.com
~/.local/share/nvim
### spacevim 如何复制到系统剪切 TODO
查了一下需要插件暂时放弃

### wget --no-check-certificate

### spacevim 闪烁屏幕 
此问题应该是增加了
let g:python_host_prog = '/usr/bin/python2'
let g:python3_host_prog = '/usr/bin/python3.8
两项以后需要禁止检查，这个设置查找mac上的设置

### 查找函数定义的位置

### 搜索功能
### nvim -V 开启调试模式

### arguments keywords

### 读写文件
./src/file_test.py

### 数字转字母
chr(69)

###  使用json保存结构化数据
shell: jq
./src/json_save.py
三个函数
dump dumps load

### 错误和异常
./src/error_execption.py

### Class 类
./src/class_start.py
./src/class_t.py      # 继承多个类
./src/class_super.py  # super 测试
类继承super() 为了解决的问题是父类名字修改以后，代码省去修改
继承多个类方法重名先加入的类会覆盖后加入的类的方法
类定义加object 这个要注意super 等依靠
```
def super_get(self, name):
    father.get(name)
    ....
def super_get(self):
    super(son, self).get(name) # python2
    supre().get(name)
```


### Spacevim 指定Python3
Spacevim 读取virtual 环境变量
尝试创建virtal 环境
python3 -m venv /path/to/new/virtual/
再次启动vim 读取的就是当前的环境的python

### dataclass
@dataclass 简单定义类
./src/class_dataclass.py

### virtualenv 
python2.7 -m pip install virtualenv --user
virtualenv venv_python2.7
python3.7 -m venv venv_python3.7

### chrome vim 插件
? 帮助
J prev_tab
K next_tab
j
k
v
f 

### 取消spacevim tmux 插件 or tmux 清除缓存
tmux: clear-history
[[layers]]
  name = "tmux"
  tmux_navigator_modifier = "alt"

自动索引删除一下配置，不再调取tmux
[[custom_plugins]]
  1 #  name = 'wellle/tmux-complete.vim'
  2

### tmux.conf 增加配置
~/.tmux.conf
vim tmux copy-mode 测试
增加键盘设置
M-[hjkl<>]
C-l clear-history


### 类变量和实例变量
类的变量是所有类实例共享的，注意
__ 双下划线定义私有方法
./src/class_value.py

### 类的迭代的实现
./src/class_iter.py

### 生成器yield  
yield 我理解为return，就是节省内存的方式，不会一次性反馈，调用一次吐出一次，对于大行数据应该考拉反使用此方法。
./src/yield_list.py

### 10. 标准库简介

### 2020-12-08 Tue Dec  8 14:04:29 CST 2020
总结一下学习python的路径吧。
1. 先记住框架，然后慢慢自己丰富自己的技能，太难太深的先略过。（有些东西你放在脑子里，自己慢慢自然就会了,再有就是很多模块可能你这辈子可能都用不上，不会就不会了）。

2. 尝试一下常见的模块，难理解的先抛弃掉以后再看。
3. 找一些自己感兴趣的扩展库玩耍一下，可以找找git的awesome 看看有兴趣的看看
4. python-cheatsheet 挺好的，按着代码片段自己输入然后理解理解
5. 尝试自己做点啥
6. 看看专业产品如ansible是如何组织代码和框架的
7. 通过粗略掌握以上内容在去提升自己的思考去看看如‘流畅的python’，或廖雪峰的网站深入理解
8. 还是多实践，多做就会深入理解

战略性的思考：
了解自己的实例，在看看周围环境其他同事，平时多关注一些其他厂商的招聘信息啥的也可以看出自己究竟哪里是短板，能力低就要韬光养晦、合纵连横、技术并不是全部，有了战略眼光才能发现自己的不足，不会闭门造车。有机会就要积极争取，了解自己的实例和缺点，知道自己的目标。并不是你把全部函数都背会了，你就能拿高薪了，技术只是进步的敲门砖，参加这个社会大游戏的多方面中的一个。

- python 总结列表，看看那些库函数是自己需要的，没有必要记录全部默认python的所有库
- python 其他dlc，你需要了解所有增加的程序规则、才能更好的使用
- python 扩展库、搜集常用和自己用的上的扩展库，可以理解为其他mod。
- PEP 是啥？可以理解为dnd，提案建议书
- https://github.com/topics/awesome  非常棒连接
- helogithub https://github.com/521xueweihan/HelloGitHub 中文git月报
- python 代码块备忘录 https://github.com/gto76/python-cheatsheet
