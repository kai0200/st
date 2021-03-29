# Zabbix

- 

自动化运维
1. cobbler
2. Ansible
3. kubernetes
4. zabbix
5. elastic
6. jenkins

zabbix 是Alexei Vladishev 的一家银行内部项目

1998年开始 2020年5月12日 5.0 LTS发布

包含单元
1. Zabbix Server
2. Zabbix 代理
3. Zabbix 前端


## zabbix server 安装
基本上安装一次以后不会反复安装、采用代理方式使用yum安装。
- yum 方式安装

- 1. 安装软件仓库配置包
```sh 
rpm --httpproxy=https://10.18.32.193:3128 -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm

rpm --httpproxy=https://10.18.32.193:3128 -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm

```


- server 升级


## zabbix agent 自动化部署
由于部署需要，采用源码编译方式编译出RHEL6/7的模式ansible 拷贝方式安装，外加需要编辑自启动命令systemctrl 调用

- 源码编译方式


## zabbix_get 使用


## 配置自动发现


## 自定义监控项目



## zabbix 资产管理


## 报警配置邮件、电话、微信


## 配置哪些监控项预防故障

- 防止黑客攻击 
1. 记录用户登陆的IP地址和操作命令
2. 
