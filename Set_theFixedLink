WordPress 固定链接设置会遇到的问题和解决方法
==========================


## 设置固定链接时显示无法更新`.htaccess`
- 可以选择手工更新`.htaccess`来解决
- 你可以检查`httpd.conf`中的`LoadModule rewrite_module`是否被注释了

## 打开文章显示*Internal Server Error*
- 检查`.htaccess`内容是否正确

## `.htaccess`可以更新时打开文章，*404*错误的处理
- 更新`httpd.conf`

```
<Directory />
    Options FollowSymLinks
    AllowOverride None
</Directory>
#这里不需要修改
<Directory "/var/www/html">

#
# Possible values for the Options directive are "None", "All",
# or any combination of:
#   Indexes Includes FollowSymLinks SymLinksifOwnerMatch ExecCGI MultiViews
#
# Note that "MultiViews" must be named *explicitly* --- "Options All"
# doesn't give it to you.
#
# The Options directive is both complicated and important.  Please see
# http://httpd.apache.org/docs/2.2/mod/core.html#options
# for more information.
#
    Options Includes ExecCGI FollowSymLinks

#
# AllowOverride controls what directives may be placed in .htaccess files.
# It can be "All", "None", or any combination of the keywords:
#   Options FileInfo AuthConfig Limit
#
    AllowOverride All
#此处修改为ALL
#
# Controls who can get stuff from this server.
#
    Order allow,deny
    Allow from all
#此处修改我饿Allow
</Directory>
```

