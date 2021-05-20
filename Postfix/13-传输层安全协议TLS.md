# 第十三章 传输层安全协议TLS
    保证传输过程加密、不给串改，客户端收取等其他操作还是有可能被串改和窃取。
## Postfix与TLS
    需要包含patch

## TLS证书
    1. TLS证书、CA数字签名
    2. 自主生成证书openssl

## 安装CA证书
    文件扩展名pem

## 设定Postfix/TLS
    - smtpd_user_tls
    - smtpd_tls_key_file
    - smtpd_tls_cert_file
    - smtpd_tls_CAfile
    - smtpd_tls_CApath

## Postfix/TLS的设定过程整理
    安装tls证书、编辑main.cf 文件、postfix reload

## 取得客户证书
    用户使用客户端加密传输TLS

## TLS/SMTP client的设定过程
    smtp使用smtpd相同证书
    smtp_user_tls = yes
    smtp_tls_key_file = /etc/postfix/mailkey.pem
    smtp_tls_cert_file = /etc/postfix/mail_signed_cert.pem
    smtp_tls_CAfile = /etc/postfix/cacert.pem

    postfix reload
