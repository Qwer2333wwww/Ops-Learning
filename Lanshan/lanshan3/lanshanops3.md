# 蓝山第三次课作业

### Level0：了解课上的shell和git相关知识，下载好git

![QQ20251111-105509](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202511111055446.png)

如图，已安装

### Level1：试着通过运行shell脚本来执行一些命令

![QQ20251111-103128](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202511111056228.png)

如图所示，成功输出'Hello,world!'

### Level2：用shell做一个石头剪刀布的脚本

![QQ20251111-104640](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202511111057010.png)

运行效果如图

### Level3：尝试使用git上传作业，把自己的GitHub(Gitee也可以)地址用邮箱发过来

这里贴上Gitee账号吧，GitHub有账号，但是这边暂时不上传到仓库。

[Qwer2333 (qwer2333wwww) - Gitee.com](https://gitee.com/qwer2333wwww)

```bash
❯ ssh-keygen -t ed25519 -C "Gitee SSH Key"
❯ cat ~/.ssh/id_ed25519.pub
❯ ssh -T git@gitee.com
❯ git config --global user.name 'Qwer2333' 
❯ git config --global user.email '略'
❯ git remote add origin git@gitee.com:qwer2333wwww/lanshanops-task-3.git
❯ git push origin main
```   