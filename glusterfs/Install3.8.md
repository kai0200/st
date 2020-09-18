# 安装

先测试源码安装的glusterfs8.1，发现的主要问题是，其他RHEL6，mount的时候需要再编译还是很麻烦，现在看稳定版本为7。
https://download.gluster.org/pub/gluster/glusterfs/7/LATEST/，设置的版本考虑一下其他应用服务器的版本，查看Centos的rpm包看只支持RHEL6 或7。
配置yum方式安装还是比较方便，源码安装gluster8.1 以后发现mount -t glusterfs 或mount -t nfs 配置主服务都不方便挂载，所以尝试glusterfs7。

### yum 配置yum源，配置proxy代理
```
# filename gluster-epel.repo 
[gluster]

name=gluster
#baseurl=https://buildlogs.centos.org/centos/7/storage/x86_64/gluster-3.8/
#baseurl=https://buildlogs.centos.org/centos/6/storage/x86_64/gluster-7/
baseurl=https://buildlogs.centos.org/centos/7/storage/x86_64/gluster-7/
gpgcheck=0
enabled=1
```

```
# filename: yum.conf 配置代理
proxy=http://IPAddress:3128
```

### yum install glusterfs

由于服务器较多，采用ansible 方式安装
1. 清理服务器配置
```shell
# umount 掉原有的mount
fuser  -u /gv1 
lsof | grep /gv1 

# stop gv1
gluster volume stop

fuser -km /mnt   # umount force
umount -f /mnt   # umount nfs
sed -i.bak /glusterfs-8.1/d /etc/profile
```

2. yum 脚本
```

```
