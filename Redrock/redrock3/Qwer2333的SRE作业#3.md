# 红岩SRE第三次作业

### Level0

```
完成 Learn Git Branching（https://learngitbranching.js.org/?locale=zh_CN）中的关卡(至少完成任意三小关)，截图上交  
```

直接附图吧：

![1](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202511201225160.png)

![QQ20251120-115343](https://qwerimage.oss-cn-shanghai.aliyuncs.com/202511201225448.png)

~~（后面有几个靠自己想没想出来最简指令。。。）~~

### Level1

```
使用git指令将任意仓库上传到自己的github中，并贴上自己github仓库的链接
```

[Qwer2333wwww/Ops-Learning: 这里是一些作业和碎碎念](https://github.com/Qwer2333wwww/Ops-Learning)

### Level2/3

```text
Level2:
使用指令克隆作业仓库：
git clone https://github.com/Habagouhei/Git-study-work.git clone
之后请你修复在main.c中的错误
Level3:
1. 开启一个新分支，以你的学号命名此分支，并切换到此分支进行下面的操作 
2. 把main.c复制到你的答题文件夹中，修复bug，修复完之后将新分支merge到main分支
3. 修复完成后提出Pull Request，向原仓库合并你的修改
```

这里附上过程：

```bash
git checkout -b 2025216050
git push
git checkout main
git merge 2025216050
git push
#然后就是创建PR
```

~~(好混沌的main.c。。。。)~~

