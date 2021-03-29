# zabbix5.2.1 install in CentOS7
注意操作系统建议使用CentOS7

### Disable firewall
```shell
systemctl stop firewalld.service
systemctl disable firewalld.service
```

### Disable selinux
```sh
setenforce 0
vi /etc/selinux/config
#把SELNUX=enforcing换成SELINUX=disabled
```

### Add user zabbix
```
useradd zabbix  
su - zabbix
```

### Download pkg
```
wget -e "https_proxy=http://10.18.32.193:3128" https://cdn.zabbix.com/zabbix/sources/stable/5.2/zabbix-5.2.1.tar.gz
```

### 编译环境
```
echo "proxy=http://10.18.32.193:3128"  >> /etc/yum.conf

yum -y install gcc gcc-c++ unixODBC-devel httpd mysql-devel libcurl libcurl-devel libevent libevent-devel fping curl-devel libxml2  libxml2-devel snmpd net-snmp-devel net-snmp
```

### 编译
```
./configure --prefix=/home/zabbix/zabbix-server --enable-server --enable-agent --with-mysql --with-net-snmp --with-libcurl --with-libxml2 --with-unixodbc --enable-java && make && make install
```

### 安装mysql
```sh
yum -y install mariadb mariadb-server
systemctl start mariadb
mysql_secure_installation
--为root用户设置密码
--删除匿名账号
--取消root用户远程登录
--删除test库和对test库的访问权限
--刷新授权表使修改生效

# 设置密码
mysqladmin -u root -p password sohu.com
```


### mysql 安装后初始话
```
mysql> create database zabbix character set utf8 collate utf8_bin;
mysql> create user zabbix@localhost identified by 'password';
mysql> grant all privileges on zabbix.* to zabbix@localhost;
mysql> quit;

mysql-uroot -pmysql zabbix < /home/zabbix/zabbix-5.2.1/database/mysql/schema.sql # 表结构
mysql-uroot -pmysql zabbix < /home/zabbix/zabbix-5.2.1/database/mysql/images.sql # 图片相关数据
mysql-uroot -pmysql zabbix < /home/zabbix/zabbix-5.2.1/database/mysql/data.sql   # 模版相关数据
```

### 更换目录权限
```
cd /home/zabbix
chown -R zabbix *
chgrp -R zabbix *
```

### 修改配置文件
```
vi /home/zabbix/zabbix-server/etc/zabbix_server.conf
DBHost=localhost
DBName=server
DBUser=root
DBPassword=xxxx
DBSocket=/usr/local/mysql/mysql.sock
DBPort=3306
```

### 启动服务
```
/home/zabbix/zabbix-server/sbin/zabbix_server -c  /home/zabbix/zabbix-server/etc/zabbix_server.conf
```

### Add epel-release
```
yum install epel-release
```

## Install WLNMP
```
rpm -ivh http://mirrors.wlnmp.com/centos/wlnmp-release-centos.noarch.rpm --httpproxy=https://10.18.32.193:3128
yum clean all
yum install wphp74
```
## Change conf
```sh
vim /usr/local/php/etc/php-fpm.conf
# 增加一下代码
[zabbix]                                          
listen.owner = zabbix                             
listen.group = zabbix                             
listen = /tmp/php-fpm74.sock                      
listen.backlog = -1                               
listen.allowed_clients = 127.0.0.1                
listen.mode = 0666                                
user = zabbix                                     
group = zabbix                                    
pm = dynamic                                      
pm.start_servers = 10                             
pm.min_spare_servers = 10                         
pm.max_spare_servers = 20                         
pm.max_children = 20                              
pm.max_requests = 1000                            
php_value[max_input_time] = 300                   
;pm = static                                      
request_terminate_timeout = 100                   
request_slowlog_timeout = 0                       
slowlog = /var/log/php_slow.log
# 还有一个ldap报交警PHP LDAP off没有处理
```

## Start php-fpm
```
/etc/init.d/php-fpm74 restart
```

## install nginx
```
su - zabbix
wget -e"http_proxy=http://10.18.32.193:3128" http://nginx.org/download/nginx-1.19.4.tar.gz
tar -zxvf nginx-1.19.4.tar.gz
cd nginx-1.19.4
./configure --prefix=/home/zabbix/nginx && make && make install
```


## conf nginx
```sh
vim /home/zabbix/nginx/conf/nginx.conf
http {
    include       mime.types;
    ...
    #gzip  on;
    include /home/zabbix/nginx/conf/conf.d/*.conf; # 增加此行

cp  -rf zabbix-5.2.1/ui/   /home/zabbix/zabbix-server/share/
cd /home/zabbix/zabbix-server/share/
chown -R zabbix:zabbix ui

vim /home/zabbix/nginx/conf/conf.d/zabbix.conf
server {
        listen          80;
        server_name     zabbix.mail.sohu.com;

        root    /usr/share/zabbix;

        index   index.php;

        location = /favicon.ico {
                log_not_found   off;
        }

        location / {
                try_files       $uri $uri/ =404;
        }

        location /assets { access_log      off;
                expires         10d;
        }

        location ~ /\.ht {
                deny            all;
        }

        location ~ /(api\/|conf[^\.]|include|locale) {
                deny            all;
                return          404;
        }
        # PHP 脚本请求全部转发到 FastCGI处理. 使用FastCGI协议默认配置.
        # Fastcgi服务器和程序(PHP,Python)沟通的协议.
        location ~ [^/]\.php(/|$){
            fastcgi_pass    unix:/tmp/php-fpm74.sock;
            fastcgi_index   index.php;
            include         fastcgi.conf;

        }
}


```

## Start nginx
```
/home/zabbix/nginx/sbin/nginx -c /home/zabbix/nginx/conf/nginx.conf
# nginx的一些常用管理命令
启动：/home/zabbix/nginx/sbin/nginx 直接执行就是启动
重启：/home/zabbix/nginx/sbin/nginx -s reload
停止：/home/zabbix/nginx/sbin/nginx -s stop 或者是通过kill nginx进程号
查看版本：/home/zabbix/nginx/sbin/nginx –V
```

## 访问
http://ip/
Admin
zabbix

## Add rc.local
```
vim /etc/rc.local
# mysql 
systemctl restart mariadb

# zabbix 
/home/zabbix/zabbix-server/sbin/zabbix_server -c  /home/zabbix/zabbix-server/etc/zabbix_server.conf  

# php
/etc/init.d/php-fpm74 restart# nginx/home/zabbix/nginx/sbin/nginx -c /home/zabbix/nginx/conf/nginx.conf -s stop
sleep 1;
/home/zabbix/nginx/sbin/nginx -c /home/zabbix/nginx/conf/nginx.conf 
```

## Install zabbix-agent2
https://repo.zabbix.com/zabbix/5.2/rhel/7/x86_64/  # RHEL7
https://repo.zabbix.com/zabbix/5.2/rhel/6/x86_64/  # RHEL6
rpm -ivh 

## add start with system
systemctl enable --now zabbix-agent2

## 中文问题
yum -y install kde-l10n-Chinese
yum -y reinstall glibc-common
localedef -c -f UTF-8 -i zh_CN zh_CN.utf8


## 重启以后报告DB error
```shell 
出错情况是安装中文支持以后发现登录报告Database error
Database error
No such file or directory
错误原因是php找不到socket文件

确保/etc/my.cnf存在
方法1. ln -s /var/lib/mysql/mysql.sock  /tmp/
方法2. 修改my.cnf文件socket=/tmp/mysql.sock

说明：
php 配置连接本地mysql的时候尝试使用sock文件方式，默认配置目录在/tmp目录下
# php -r 'echo phpinfo();'  | grep mysql.sock
pdo_mysql.default_socket => /tmp/mysql.sock => /tmp/mysql.sock

```
