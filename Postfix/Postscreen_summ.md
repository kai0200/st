# Postscreen

## SMTP Server Overload
    ```sh
        postconf default_process_limit
    ```

## 测量
    - 预先测试
    - 实时黑名单检查
    - 深度协议测试

## Step 1: Enable Postscreen in Postfix
    ```sh
    postconf mail_version # 查看postfix 版本

    vim /etc/postfix/master.cf # 增加以下配置
    smtp      inet  n       -       y   -       1       postscreen
    smtpd     pass  -       -       y   -       -       smtpd
    dnsblog   unix  -       -       y   -       0       dnsblog
    tlsproxy  unix  -       -       y   -       0       tlsproxy

    vim /etc/postfix/main.cf
    postscreen_access_list = permit_mynetworks cidr:/etc/postfix/postscreen_access.cidr
    postscreen_blacklist_action = drop

    vim /etc/postfix/postscreen_access.cidr
    #permit my own IP addresses.
    23.254.225.226/32             permit
    2a0d:7c40:3000:b8b::2/128     permit
    12.34.56.78/32                reject

    postconf postscreen_cache_map #查看配置
    ```

## Step 2: Pregreet Test (预弯曲测试)
    ```sh
    vim /etc/postfix/main.cf
    postscreen_greet_action = enforce # 预测试 grep PREGREET /var/log/maillog
    postscreen_greet_action = drop

    # restart postfix
    ```

## Step 3: Using Public Blacklists & Whitelists
    ```sh

    main.cf # 此配置文件，删除smtp reject_rbl_client or permit_dnswl_client配置
    postscreen_dnsbl_threshold = 3
    postscreen_dnsbl_action = enforce
    postscreen_dnsbl_sites =
        zen.spamhaus.org*3
        b.barracudacentral.org=127.0.0.[2..11]*2
        bl.spameatingmonkey.net*2
        bl.spamcop.net
        dnsbl.sorbs.net

    postscreen_dnsbl_sites =
        zen.spamhaus.org*3
        b.barracudacentral.org=127.0.0.[2..11]*2
        bl.spameatingmonkey.net*2
        bl.spamcop.net
        dnsbl.sorbs.net
       swl.spamhaus.org*-4,
       list.dnswl.org=127.[0..255].[0..255].0*-2,
       list.dnswl.org=127.[0..255].[0..255].1*-4,
       list.dnswl.org=127.[0..255].[0..255].[2..3]*-6
    ```
    使用自己的dns服务器8.8.8.8等都有查询限制

## Step 4: Enable Deep Protocol Tests
    ```sh

    # 拒绝多次发送Rcpt to
    postscreen_pipelining_enable = yes
    postscreen_pipelining_action = enforce

    # 非 smtp命令拒收
    postscreen_non_smtp_command_enable = yes
    postscreen_non_smtp_command_action = enforce

    # 裸换行符测试使Postscreen可以检测以<LF>（而不是标准<CR> <LF>）结尾的SMTP客户端
    postscreen_bare_newline_enable = yes
    postscreen_bare_newline_action = enforce
    ```

## 深度协议测试的灰名单效应
    ```sh
    # delete 
    check_policy_service inet：127.0.0.1：10023
    ```

## 如何最大程度地减少不良用户体验
    - 创建第二个指向相同IP地址的MX记录。
    - 如果SMTP客户端的IP地址在公共白名单上，请跳过深度协议测试。
    - 使用Postwhite将已知的正确IP地址添加到Postscreen白名单中。
    ```sh
    
    # 以忽略分数等于或小于-2的客户端
    postscreen_dnsbl_whitelist_threshold = -2
    ```
