# Go

## 目录
1. 初始go
2. 语法概览
3. 并发编程综述
4. Go并发机制
5. 同步
6. 网络爬虫架构设计和实现

### 1. 初始Go

- GOPATH  要设置到有src目录的位置，使用绝对路径
- helo.go
```go
package main

import (
  "bufio"
  "fmt"
  "os"
)

func main() {
  inputReader := bufio.NewReader(os.Stdin) // := 声明局部变量并赋值
  ...
  // 平行赋值规则
  input, err := inputReader.ReaderString('\n')
  // 切片
  input = input[:len(input)-1]
}
```

- 参数
* build
* clean
* doc
* env
* fix
* fmt
* generate
* get
* install
* list
* run
* test
* tool
* vet
* version
* -a
* -n
* -race
* -v
* -work
* -x

- go tool 
* pprof
* trace
* https://github.com/GoHackers/go_command_tutorail 

### 2. 语法概览

2.1 基本构成要素
2.1.1 标识符

error
true false iosta
append cap close complex copy delete imag len make new panic pringln real recover
_ = x // x 未使用不会报错

2.1.2 关键字


语法说明作为，可以先作为速查手册
| 类别           | 关键字      |
|----------------|-------------|
| 程序声明       | import      |
|                | package     |
|----------------|-------------|
| 程序声明与定义 | chan        |
|                | const       |
|                | func        |
|                | interface   |
|                | map         |
|                | struct      |
|                | type        |
|                | var         |
|----------------|-------------|
| 程序流程控制   | go          |
|                | select      |
|                | break       |
|                | case        |
|                | continue    |
|                | default     |
|                | defer       |
|                | else        |
|                | fallthrouth |
|                | for         |
|                | goto        |
|                | if          |
|                | range       |
|                | return      |
|                | switch      |
|----------------|-------------|
2.1.3 字面量
```go
type Name struct {
    Forename string
    Surname string
}
Name{Forename: "Fobert", Surname:"Hao"}
```
struct(结构)
array(数组)
slice(切片)
map(字典)

2.1.4 操作符

2.1.5 表达式
| 示例            | 种类       |
|-----------------|------------|
| context.Speaker | 选择表达式 |
| array[1]        | 索引表达式 |
| slc1[0:2]       | 切片表达式 |
| v1.(I1)         | 类型断言   |
| v1.M1()         | 调用表达式 | 


2.2 基本类型
bool byte int/unit ....
rune //用于存储Unnicode字符

2.3 高级类型
2.3.1 数组 array

```
var ipv4 [4]unit8 = [4]unit8{10,10,8,12}
ipv4 [4]unit8 := {10.18.32.193}

```

2.3.2 切片
```
var ips = []string{"192.168.0.1", "192.168.0.2","10.18.33.192"}

ips[:cap(ips)]

ips = append(ips, "192.168.0.3")
```
nil 切片的0值
len cap 

2.3.3 字典
```
var ipSwitches = map[string]bool{}
```

2.3.4 函数和方法
```
func divide(divident int, divisor int)(int, error) {
}
```



### 3. 并发编程综述

3.1 并发编程基础
3.2 多进程编程 - 这部分很长
3.3 多线程编程
3.4 多线程与多进程
3.5 多核时代的并发编程

