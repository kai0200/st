# 第六章Email与DNS

## DNS概论
    - A
    - CNAME
    - MX
    - PTR # 反解

## 决定邮件路由
    MX记录决定
    ```sh
        example.com.    IN      MX  10  mx1.example.com
        example.com.    IN      MX  20  mx2.example.com
        # 10 20 代表优先级范围0-65535
    ```

## Postfix与DNS
    1. DNS对寄信程序的影响
        PTR 反解
        SPF TXT记录

    2. DNS对收信程序的影响
        postfix 可接收的邮件
            - 本地 mydestination
            - 转发 relay_domain
            - 虚拟邮箱 virtual_mailbox_domains
            - 虚拟别名 virtual_alias_domain

## 常见问题
    - "mail for domain loops back to myself" 检查mydestination配置
    - "no MX "
    - "Host not found, try again"
