# 安装 Ubuntu 系统
Ubuntu Server 14.04 LTS
user: ubuntu
password: xxx
（用户名密码，自己设置）

# 更新 ubuntu 软件源
sudo apt-get update
sudo apt-get upgrade

# 安装 nginx, MySQL, Pip, Supervisor
sudo apt-get install nginx mysql-server python-pip supervisor

## ubuntu 软件仓库中的版本是 1.4 的，如果需要新的 1.8 的，按照下面说明安装。
下载 nginx 签名文件
wget http://nginx.org/keys/nginx_signing.key
安装签名
sudo apt-key add nginx_signing.key
编辑 apt 配置文件
sudo vi /etc/apt/source.list
末尾添加两行
deb http://nginx.org/packages/ubuntu/ trusty nginx
deb-src http://nginx.org/packages/ubuntu/ trusty nginx
更新源
sudo apt-get update
安装 Nginx
sudo apt-get install nginx

# 安装 MySQL-python 包的依赖
sudo apt-get install libmysqld-dev python-dev zlib1g-dev 
# 安装 MySQL-python
sudo pip install mysql-python
# 安装 tornado 的依赖
sudo pip install certifi

# 创建网站目录
sudo mkdir /var/www
# 修改网站目录所有者（我不太确定，这么做有没有问题，先这样了）
sudo chown -R ubuntu:ubuntu /var/www

# 在本地 git clone 代码
git clone https://github.com/xzm920/tornado-demo.git

# 把代码部署到服务器
rsync -avz tornado-demo ubuntu@example.com:/var/www

# 创建 log 目录
sudo mkdir /var/log/nginx/tornado-demo
sudo chown -R www-data:www-data /var/log/nginx/tornado-demo

# Nginx 和 Supervisor 的配置文件在 tornado-demo/conf 下面
# 配置 Nginx
用 tornado-demo/conf/nginx/nginx.conf 替换 /etc/nginx/nginx.conf
把 tornado-demo/conf/nginx/tornado-demo.conf 添加到 /etc/nginx/conf.d 目录（如果没有目录 conf.d 自己创建一个）
reload Nginx 使配置文件生效
sudo nginx -s reload

# 配置 Supervisor
把 tornado-demo/conf/supervisor/tornado-demo.conf 添加到 /etc/supervisor/conf.d
重启 supervisor
sudo /etc/init.d/supervisor restart
进入 supervisor 管理工具
sudo supervisorctl
启动 tornado 应用
start app
退出 supervisor 管理工具
exit

# 在本地访问服务器 http://example.com (或者 ip 地址访问)

# 后面会继续更新。。。
## 作者：许志铭
