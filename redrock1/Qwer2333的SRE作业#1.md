# Qwer2333的SRE作业#1

不知道说啥前言，就直接逐level写过程吧

------

### Level0-1:尝试在虚拟机用vim写一段C语言代码输出`hello,world`

虚拟机环境我采用的是WSL2，毕竟比较方便嘛       

编译器的话已经有gcc了，就不用再安装了        

直接贴上运行截图吧~~（本来还专门在阿里云oss上面创建了个图床来存md里面的图片来着，结果后面发现直接导出成pdf，直接存本地就行）~~

```c
#include <stdio.h>

int main() {
    printf("hello, world\n");
    return 0;
}

```

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510261701202.png)

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510261702414.png)

------

### Level0-2:掌握typora或者obsidian的使用，会写简单的.md文件（不检查）

额，这个文档就是用typora写的来着，不过不检查的话也就不用再详细说啥了吧（逃

------

### Level1:在你的虚拟机上配置一些编程语言环境，如gcc，python等,也可以试试如何实现python2和python3共存

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510261713782.png)

如图，自带gcc和python3环境。遂尝试安装python2。这里选择使用pyenv来管理python版本。

```bash
curl https://pyenv.run | bash
```

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510261718353.png)

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510261726591.png)

```bash
pyenv install 2.7.18
```

~~额，突然想到我没必要贴一堆终端输出截图啊，输出还是直接写文档里吧。。。（前面的部分懒得改了，请见谅）~~

出现报错如下，决定去查Wiki

```bash
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named readline
WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named zlib
ERROR: The Python zlib extension was not compiled. Missing the zlib?

Please consult to the Wiki page to fix the problem.
https://github.com/pyenv/pyenv/wiki/Common-build-problems


BUILD FAILED (Ubuntu 24.04 using python-build 2.6.11)

Inspect or clean up the working tree at /tmp/python-build.20251026172638.1681
Results logged to /tmp/python-build.20251026172638.1681.log

Last 10 log lines:
rm -f /home/qwer2333/.pyenv/versions/2.7.18/share/man/man1/python.1
(cd /home/qwer2333/.pyenv/versions/2.7.18/share/man/man1; ln -s python2.1 python.1)
if test "xno" != "xno"  ; then \
        case no in \
                upgrade) ensurepip="--upgrade" ;; \
                install|*) ensurepip="" ;; \
        esac; \
        LD_LIBRARY_PATH=/tmp/python-build.20251026172638.1681/Python-2.7.18 ./python -E -m ensurepip \
                $ensurepip --root=/ ; \
fi
```

查Wiki发现需要如下软件包：

```bash
sudo apt install zlib1g zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev
```

问题解决

```bash
❯ pyenv versions
* system (set by /home/qwer2333/.pyenv/version)
  2.7.18
```

按理说切换版本要用`pyenv global 2.7.18`，但是我不想切换到python2，所以跳过😋

------

### Level2:部署一个属于你自己的博客

以下部分在新租的2C2G阿里云轻量云服务器中完成，环境为Ubuntu24.04

~~人生苦短，我选WordPress！~~

纯小白，只用过hexo，遂去[阿里云教程](https://www.alibabacloud.com/help/zh/ecs/user-guide/manually-build-a-wordpress-website-on-a-centos-7-ecs-instance)（超链接在PDF里面似乎点不了），

这里通过[**LNMP**](https://www.alibabacloud.com/help/zh/ecs/user-guide/manually-build-an-lnmp-environment-on-a-centos-instance#7ff8db0dc8in5)部署**Nginx+MySQL+PHP**

先装**Nginx+MySQL**

```bash
sudo apt update -y
sudo apt install -y curl gnupg2 ca-certificates lsb-release ubuntu-keyring
curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.list
sudo apt install -y nginx
sudo apt update -y && sudo apt install -y mysql-server
```

安装**PHP**

```bash
sudo apt update && sudo apt install -y software-properties-common && sudo add-apt-repository -y ppa:ondrej/php
sudo apt install -y php8.4 php8.4-fpm php8.4-mysql
sudo grep '^listen =' /etc/php/8.4/fpm/pool.d/www.conf
```

查询php-fpm配置文件默认监听地址，返回sock文件地址说明默认监听sock文件。

故编辑`/etc/nginx/conf.d/default.conf`文件添加PHP转发规则

接着重启Nginx服务

```bash
 sudo systemctl restart nginx
```

在路径`/usr/share/nginx/html`下新建`test.php` 的 PHP 文件，并添加用于测试数据库连接的代码。

公网访问测试网页，返回`success`说明PHP代理设置成功并成功连接MySQL数据库。

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510272321408.png)

接下来开始部署WordPress

先配置WordPress数据库

```bash
mysql -u root -p
create database wordpress;
create user '用户'@'localhost' identified by '密码';
grant all privileges on wordpress.* to '用户'@'localhost';
flush privileges;
exit;
```

然后下载WordPress

```bash
cd /usr/share/nginx/html
sudo wget https://cn.wordpress.org/wordpress-6.4.4-zh_CN.zip
sudo apt install unzip -y
sudo unzip wordpress-6.4.4-zh_CN.zip
cd /usr/share/nginx/html/wordpress
sudo cp wp-config-sample.php wp-config.php
```

然后修改WordPress和Nginx配置文件并重启Nginx

```bash
sudo systemctl restart nginx
```

最后使用浏览器访问ECS的公网IP，进入WordPress安装页面就OK了

然后升级一下WordPress的核心，插件，补全需要的PHP拓展即可。

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510280028761.png)

至此博客的部署工作已完成，接下来就是撰写文章，美化，装插件，买域名，备案，cdn，waf等一系列后续工作了~~（遥遥无期ing）~~

~~突然想起已经没钱买域名了。。。~~

------

### Level3：使用docker！把你的博客用docker打包，想启动博客直接一键启动就好

还是纯新手，还是在本地WSL2里面弄吧，怕服务器环境炸掉(而且方便挂梯子来pull镜像)

之前已经装了docker desktop并启用WSL Integration了

直接创建文件结构

```bash
wordpress-docker/
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── php/
│   └── Dockerfile
├── wordpress/
│   └── (WordPress 文件)
└── db/
    └── .gitkeep
```

写好对应的文件后构建镜像并启动容器（这里似乎不科学上网就一直pull不到镜像）

```bash
cd ~/wordpress-docker
docker-compose up --build -d
```

现在能够访问http://localhost:8080/了但是提示建立数据库连接时出错

经排查发现`wordpress` 目录的`wp-config.php`中的

```php
define('DB_HOST',     'localhost'); 
```

在 Docker 网络里应该用服务名 `db`，故应改为

```php
define('DB_HOST',     'db:3306');
```

改完保存之后直接刷新浏览器就可以了😋

![](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202510282238769.png)

现在就可以把整个环境打包成镜像，方便迁移或分享了

```bash
docker-compose up -d
docker exec wordpress-docker-db-1 mysqldump -u$MYSQL_USER -p$MYSQL_PASSWORD --databases $MYSQL_DATABASE > dump.sql
docker exec wordpress-docker-php-1 tar -C /var/www/html -czf - wp-content/uploads > uploads.tar.gz
cd ..
tar -czf wordpress-docker.tar.gz wordpress-docker/
```

接下来把`wordpress-docker.tar.gz`拷到另一wsl中尝试载入镜像

```bash
tar -xzf wordpress-docker.tar.gz
cd wordpress-docker
docker-compose up -d
```

成功，现在启动博客就可以直接一键启动了。。。吧

~~（本来想在Ubuntu25虚拟机尝试的，但是网络问题导致镜像pull不下来。。。虚拟机挂VPN太麻烦，又懒得给docker换源故略过）~~

------

### 后记

额。。。不知道写啥啊，就随便碎碎念两句吧（

没想到整个作业#1最麻烦的部分竟然是博客的**LNMP**环境的搭建和docker的网络问题。。。。

总而言之感觉这份作业还是有很大提升空间的，~~比如说少点碎碎念~~



