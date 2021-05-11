# 第三章 Postfix的结构

## Postfix组件
模块化管理 多数组件dameon的形式存在 master daemon主导邮件处理流程

主要配置文件
- main.cf
- master.cf

处理流程
- 接收邮件
- 将邮件排入队列
- 投递邮件

```sh
[In]                      [Queue]      [Out]
Local submissions                      smtp, relay, lmtp,
Network submissions    -> Queue   ->   local, virtual, pipe
Local forwarding          manager
Notifications
```

## 邮件如何进入Postfix系统 [In]
进入队列前cleanup daemon 清理邮件，Queue Manager 收到队列有新的信件以后，使用trivial-rewrite来决定邮件的路由信息，包括传输方法、下一站以及收件人地址。

Queue Manager 维护队列

- incoming 收件
- active 活动
- deffered 延迟
- corrupt 故障

## Postfix的队列管理 [Queue]

- 进入队列之前的关卡cleanup daemon
- Queue Manager
    1. incoming  - 第一站收件队列
    2. active - Queue发现资源空闲移入
    3. deferred - Queue检查投递失败
    4. corrupt - Queue检查耽搁太久 协调bounce与defer daemons产生退信

注：hold队列目录-管理员管理用

## 投递操作 [Out]

- local 本地 local MDA、mydestination参数、先检查.forward
- virtual alias 虚拟别名 virtual_alias_domains 参数
- virtual mailbox 虚拟邮箱 virtual_mailbox_domains 参数
- relay 转发 relay_domains 参数

## 实际追踪Postfix的邮件处理流程 [总结]

### 发送邮件到其他MTA
```sh
    mail sender
        |
        v
    postdrop
        |
        v        [Queue manager]
    maildrop        incoming    ->   active -> smtp ->
        |               |                       ^
        v               v                       |
    pickup  ->       cleanup                    v
                        ^                      DNS Server
                        |
                        v
                    trivial-rewrite
```
MUA -> sendmail(程序) -> maildrop(目录) -> pickup daemon(程序) -> cleanup daemon(程序) -> queue manager -> smtp MDA

### 从其他MTA接收邮件再转发寄出
```sh
         incoming      -> active -> local
            ^                         ^
            |                         |
smtpd -> cleanup <--------------------|
            |                         v
            v                       aliase
        trivial rewrite
```

### 从其他MTA接收邮件并存入邮箱

```sh

         incoming      -> active -> local
            ^                         ^
            |                         |
smtpd -> cleanup                      |
            |                         v
            v                       Message store
        trivial rewrite

```
