# 队列清理

- hold mail
postsuper -h ALL 
postsuper -h -

- release queue 
postsuper -H ALL deferred 
postsuper -H Queue_id

- requeue 
postsuper -r ALL 
postsuper -r Queue_id

- del queue
postsuper -d ALL
postsuper -d Queue_id

- find error mail
```shell
find /opt/spool/postfix/deferred -type f -exec ls -l --time-style=+%Y-%m-%d_%H:%M:%S {} \;
```

- del 3 days ago mails
```shell
find /opt/spool/postfix/deferred -type f -mtime +3 -exec rm -f {} \; 

```

- del 5 days ago defer mails
```shell
find /opt/spool/postfix/defer -type f -mtime +5 -exec rm -f {}\;
```

- flush queue
postqueue -f



