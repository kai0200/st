# RHEL7 install zabbix 5.0

5.0 现在（2021-03-29）为TLS支持版本，选择rhel7（现有系统都在此系统版本）

安装过程
========

## 1. rhel更换centos源
```shell
# 增加yum代理模式
echo "proxy=http://10.18.32.193:3128" >> /etc/yum.conf 

# 配置全局代理
export https_proxy=http://10.18.32.193:7890 http_proxy=http://10.18.32.193:7890 all_proxy=http://10.18.32.193:7890

# 配置163 Centos yum
cd /etc/yum.repos.d/
wget -e"http_proxy=http://10.18.32.193:3128"  http://mirrors.163.com/.help/CentOS7-Base-163.repo

# 替换错误变量为7 rhel就可以使用centos的源了
 sed -i '%s/$releasever/7/g' /etc/yum.repos.d/CentOS7-Base-163.repo 

# 禁用掉rhel提示注册
sed -i 's/enable=1/enable=0/g' /etc/yum/pluginconf.d/subscription-manager.conf
rm -f /etc/yum.repos.d/redhat.repo
```

## 2. 配置阿里源
```bash
rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm
sed -i 's#http://repo.zabbix.com#https://mirrors.aliyun.com/zabbix#' /etc/yum.repos.d/zabbix.repo
yum clean all
yum makecache
yum repolist
```

## 3. 安装 zabbix-server and zabbix-agent
```bash
yum install zabbix-server-mysql zabbix-agent -y
```

## 4. 使用scl，yum默认安装的php版本过低采用scl安装php72，配置文件路径较长，可以ln -s /etc/单独目录方便vi
```bash
yum install centos-release-scl -y
```

## 5. enable zabbix-frontend
启用 zabbix 前端源，修改/etc/yum.repos.d/zabbix.repo,将[zabbix-frontend]下的 enabled 改为 1

## 6. 安装zabbix frontend
```bash
yum -y install zabbix-web-mysql-scl zabbix-nginx-conf-scl
ln -s /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf  /etc/zabbix/php/
ln -s /etc/opt/rh/rh-nginx116/nginx/conf.d/zabbix.conf  /etc/zabbix/nginx/
ls /etc/my.cnf
# 日志ln到tmp下，为调试方便
ln -s /var/opt/rh/rh-nginx116/log/nginx/error.log /tmp/nginx_err.log
ln -s /var/opt/rh/rh-php72/log/php-fpm/error.log  /tmp/php_err.log
```

## 7. 安装mysql
yum -y install mariadb mariadb-server

## 8. 开机启动
systemctl enable --now mariadb rh-php72-php-fpm rh-nginx116-nginx

## 8. 初始化mysql设置权限
```bash
mysql_secure_installation
--1 为root用户设置密码
--2 删除匿名账号 - y
--3 取消root用户远程登录 -y
--4 删除test库和对test库的访问权限 -y
--5 刷新授权表使修改生效 -y

# Q：机器重启后可能报错“Database error”？
  A：1. ln -s /var/lib/mysql/mysql.sock  /tmp/
     2. 修改my.cnf文件socket=/tmp/mysql.sock
```
## 9. 修改php配置文件
grep error /etc/opt/rh/rh-php72/php-fpm.conf  # 默认配置文件位置
vim   /etc/zabbix/php/zabbix.conf  
/etc/zabbix/php/zabbix.conf -> /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf
```conf
; php配置文件";"为注射
[zabbix]
user = nginx     
group = nginx

listen = /var/opt/rh/rh-php72/run/php-fpm/zabbix.sock
listen.acl_users = apache,nginx
; 注释掉此行 listen.allowed_clients = 127.0.0.1
listen.allowed_clients = any

pm = dynamic
pm.max_children = 50
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 35

php_value[session.save_handler] = files
php_value[session.save_path]    = /var/opt/rh/rh-php72/lib/php/session/
; 以上php/ 目录下如果使用nginx (chown -R root:nginx *)，如果使用apache改为apache

php_value[max_execution_time] = 300
php_value[memory_limit] = 128Mphp_value[post_max_size] = 16M
php_value[upload_max_filesize] = 2M
php_value[max_input_time] = 300php_value[max_input_vars] = 10000
php_value[date.timezone] = Asia/Shanghai
```

## 10. conf nginx
grep error_log  /etc/opt/rh/rh-nginx116/nginx/nginx.conf  # 默认配置文件位置
ls -l  /etc/zabbix/nginx/zabbix.conf  
/etc/zabbix/nginx/zabbix.conf -> /etc/opt/rh/rh-nginx116/nginx/conf.d/zabbix.conf
```conf
server {
    listen         80;
    server_name    _;  
    root           /opt/rh/rh-nginx116/root/usr/share/nginx/html/zabbix;

    index   index.php;
    autoindex on;

    location = /favicon.ico {
        log_not_found   off;
    }
    location / {
        try_files       $uri $uri/ =404;
    }
    location /assets {
        access_log      off;        expires         10d;
    }
    location ~ /\.ht {
        deny            all;
    }
    location ~ /(api\/|conf[^\.]|include|locale) {
        deny            all;
        return          404;
    }

    location ~ [^/]\.php(/|$) {
        fastcgi_pass    unix:/var/opt/rh/rh-php72/run/php-fpm/zabbix.sock;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_index   index.php;

        fastcgi_param   DOCUMENT_ROOT   /usr/share/zabbix;
        fastcgi_param   SCRIPT_FILENAME /usr/share/zabbix$fastcgi_script_name;
        fastcgi_param   PATH_TRANSLATED /usr/share/zabbix$fastcgi_script_name;

        include fastcgi_params;
        fastcgi_param   QUERY_STRING    $query_string;
        fastcgi_param   REQUEST_METHOD  $request_method;
        fastcgi_param   CONTENT_TYPE    $content_type;
        fastcgi_param   CONTENT_LENGTH  $content_length;

        fastcgi_intercept_errors        on;
        fastcgi_ignore_client_abort     off;
        fastcgi_connect_timeout         60;
        fastcgi_send_timeout            180;
        fastcgi_read_timeout            180;
        fastcgi_buffer_size             128k;
        fastcgi_buffers                 4 256k;
        fastcgi_busy_buffers_size       256k;
        fastcgi_temp_file_write_size    256k;
    }
}

chown nginx:nginx /etc/zabbix/web  # zabbix 安装向导保存配置文件在此目录
/etc/zabbix/web/zabbix.conf.php
```
## 11. 增加开机启动方法2
```bash
chmod +x /etc/rc.local
echo "systemctl restart mariadb rh-php72-php-fpm rh-nginx116-nginx" >> /etc/rc.local
```

## 12. 页面配置
- 浏览器http://ip/ "Next step"
- "Check of pre-requisites"  every one is "OK" -> "Next step"
- "Configure DB connection" -> "Password: xxxxxx" # localhost 改127.0.0.1会报错
- "Zabbix server details" -> "Name: ~~~~~" # 写IP地址或定义一个域名
- "Pre-installation summary" -> #报错看权限 chown nginx:nginx /etc/zabbix/web 
- Admin:zabbix登录
- 配置中文，图形下字符

## 13. 中文乱码
```
cd /usr/share/zabbix/assets/fonts
wget https://raw.githubusercontent.com/chenqing/ng-mini/master/font/msyh.ttf
wget https://github.com/chenqing/ng-mini/tree/master/font/
ln -s msyh.ttf  graphfont.ttf
```
简单更换个字体文件可以解决



--------------------------------------------------------
## 准备yum 自定义yum原需要的rpm包
1. 解决执行yum命令后总是自动又生成redhat.repo的问题
```
/etc/yum/pluginconf.d/subscription-manager.conf
enabled=0
rm -f /etc/yum.repos.d/redhat.repo
```

### 尝试下载所有需要的rpm包 <此步骤参考需要执行>
```shell
cd /etc/yum.repos.d/
wget -e"http_proxy=http://10.18.32.193:3128"  http://mirrors.163.com/.help/CentOS7-Base-163.repo

vi CentOS7-Base-163.repo #替换错误变量为7 rhel就可以使用centos的源了
%s/$releasever/7/g
yum clean all
yum makecache

yum -y install <pkgname> --downloadonly --downloaddir=/opt/pkg/

yum -y install mariadb-server mariadb php php-mysql php-gd libjpeg* php-ldap php-odbc php-pear php-xml php-xmlrpc php-mhash zabbix-server-mysql zabbix-web-mysql zabbix-agent  --downloadonly   --downloaddir=/data/down/

https://repo.zabbix.com/zabbix/<version>/rhel/7/x86_64/ 下载下面全部包文件
```

## 把rpm文件放到/data/zabbix里，执行createrepo ./，会生成一个repodata 文件夹.

## 在/var/www/html 下面，建立一个软连接.：   ln -s   /data/zabbix    zabbix_yum
