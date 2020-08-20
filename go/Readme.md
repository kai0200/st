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
