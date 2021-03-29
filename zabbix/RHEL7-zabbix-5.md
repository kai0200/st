# RHEL7 offline install zabbix 5

## 1. rhel 更换centos源

```shell
cd /etc/yum.repos.d/
wget -e"http_proxy=http://10.18.32.193:3128"  http://mirrors.163.com/.help/CentOS7-Base-163.repo

vi CentOS7-Base-163.repo #替换错误变量为7 rhel就可以使用centos的源了
%s/$releasever/7/g
yum clean all
yum makecache
```

## 2. 
rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm
sed -i 's#http://repo.zabbix.com#https://mirrors.aliyun.com/zabbix#' /etc/yum.repos.d/zabbix.repo
yum clean all


## 3.
yum install zabbix-server-mysql zabbix-agent -y

## 4.
yum install centos-release-scl -y

## 5. 

启用 zabbix 前端源，修改/etc/yum.repos.d/zabbix.repo,将[zabbix-frontend]下的 enabled 改为 1

## 6. 
yum -y install zabbix-web-mysql-scl zabbix-nginx-conf-scl

## 7.
yum -y install mariadb mariadb-server
systemctl enable --now mariadb
mysql_secure_installation

--------------------------------------------------------
## 准备yum 自定义yum原需要的rpm包
1. 解决执行yum命令后总是自动又生成redhat.repo的问题
```
/etc/yum/pluginconf.d/subscription-manager.conf
enabled=0
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

