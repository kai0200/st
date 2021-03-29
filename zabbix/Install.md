# Install 

- server: 10.16.78.165

zabbix-server Inistall
======================

## Q1: zabbix 白页
```sh
查看nginx的error_log
grep error /var/opt/rh/rh-nginx116/log/nginx/error.log
"""
...... failed: Permission denied (13) in /usr/share/zabbix/include/classes/core/CSession.php on line 45
PHP Fatal error:  Uncaught Exception: Cannot start session. in /usr/share/zabbix/include/classes/core/CSession.php:46 "
"""

报错发现有"Permission denied" 应该是权限问题，和session有关
grep session /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf 
php_value[session.save_path]    = /var/opt/rh/rh-php72/lib/php/session/

ls -lh 发现权限为 root apache ，而我们使用的是nginx
cd /var/opt/rh/rh-php72/lib/php/
chown -R root:nginx * 

改变配置后zabbix页面正常显示

```


mysql install
=============


php install
===========



