# tmux

<prefix> : Ctrl+B
- 锁屏 
增加以下配置，[prefix] + L 锁屏。
测试发现archlinux 上有些问题，redhat linux 上配置正常,应该是用户权限问题。


.zshrc 文件增加配置,为了锁屏以后显示英文Password，中文显示有点丑
```zshrc
export LANG=en_US.utf-8
```


```conf
set -g lock-command vlock
set -g lock-after-time 0 # Seconds; 0 = never
bind l lock-client
bind L lock-session
```

- 关闭当前面板 [prefix] + x



