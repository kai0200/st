# Glusterfs 简介

Redhat维护、针对大文件建议在1M以上、

# 安装

1、采用源码编译安装

2、服务器10台
10.19.1.129
10.19.1.130
10.19.1.131
10.19.1.132
10.19.1.133
10.19.1.134
10.19.1.135
10.19.1.136
10.19.1.137
10.19.1.138
10.19.1.139

# 配置

## 加入信任主机池

```shell
ssh 10.19.1.129

# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.130
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.131
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.132
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.133
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.134
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.135
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.136
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.137
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.138
# /opt/glusterfs-8.1/sbin/gluster peer probe 10.19.1.139
```

## 创建glusterfs 卷

1. Distributed：分布式卷，文件通过 hash 算法随机分布到由 bricks 组成的卷上。

2. Replicated: 复制式卷，类似 RAID 1，replica 数必须等于 volume 中 brick 所包含的存储服务器数，可用性高。

3. Striped: 条带式卷，类似 RAID 0，stripe 数必须等于 volume 中 brick 所包含的存储服务器数，文件被分成数据块，以 Round Robin 的方式存储在 bricks 中，并发粒度是数据块，大文件性能好。

4. Distributed Striped: 分布式的条带卷，volume中 brick 所包含的存储服务器数必须是 stripe 的倍数（>=2倍），兼顾分布式和条带式的功能。

5. Distributed Replicated: 分布式的复制卷，volume 中 brick 所包含的存储服务器数必须是 replica 的倍数（>=2倍），兼顾分布式和复制式的功能。

/opt/glusterfs-8.1/sbin/gluster volume create gv0 replica 3 transport tcp \
10.19.1.129:/export/sdb1/gv0 \
10.19.1.130:/export/sdb1/gv0 \
10.19.1.131:/export/sdb1/gv0 \
10.19.1.132:/export/sdb1/gv0 \
10.19.1.133:/export/sdb1/gv0 \
10.19.1.134:/export/sdb1/gv0 \
10.19.1.135:/export/sdb1/gv0 \
10.19.1.136:/export/sdb1/gv0 \
10.19.1.137:/export/sdb1/gv0 \
10.19.1.138:/export/sdb1/gv0 \
10.19.1.129:/export/sdc1/gv0 \
10.19.1.130:/export/sdc1/gv0 \
10.19.1.131:/export/sdc1/gv0 \
10.19.1.132:/export/sdc1/gv0 \
10.19.1.133:/export/sdc1/gv0 \
10.19.1.134:/export/sdc1/gv0 \
10.19.1.135:/export/sdc1/gv0 \
10.19.1.136:/export/sdc1/gv0 \
10.19.1.137:/export/sdc1/gv0 \
10.19.1.138:/export/sdc1/gv0 \
10.19.1.129:/export/sdd1/gv0 \
10.19.1.130:/export/sdd1/gv0 \
10.19.1.131:/export/sdd1/gv0 \
10.19.1.132:/export/sdd1/gv0 \
10.19.1.133:/export/sdd1/gv0 \
10.19.1.134:/export/sdd1/gv0 \
10.19.1.135:/export/sdd1/gv0 \
10.19.1.136:/export/sdd1/gv0 \
10.19.1.137:/export/sdd1/gv0 \
10.19.1.138:/export/sdd1/gv0 \
force

gluster volume start gv0

# 问题

1. 安装的是8.1 版本nfs 一直无法挂载所提采用中间服务器nfs，其他服务器挂载方式先测试。


