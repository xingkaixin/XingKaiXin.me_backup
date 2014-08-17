XingKaiXin.me 主机备份和迁移方案
================================


## 主机备份策略
### VPS备份
定期通过InterServer提供的VPS备份功能备份VPS，目前实现方式是人工备份，期望寻找的定期自动化方案
### WordPress备份
通过WordPress插件BackUpWordPress实现，每天3点执行备份，并把备份结果发送到`xingkaixin@gmail.com`，通过邮件中链接可以下载备份包

## 主机迁移方案
### WordPress文件迁移
```
zip -r wordpress.zip /var/www/html/wordpress //打包Wordpress目录
unzip wordpress.zip -d /var/www/html/wordpress //解压缩Wordpress到新目录
mv  /var/www/html/wordpress/mysql.sql  /var/www/html/mysql.sql  //把SQL命令换个地方
```

### Mysql迁移
```
source /var/www/html/mysql.sql; //导入数据
```

```
rm -rf /var/www/html/mysql.sql //删掉备份文件
```
