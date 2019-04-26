# roslibpy-docs-zh

项目[roslibpy](https://github.com/gramaziokohler/roslibpy)的**非官方**中文文档。

完整版文档页面可[在此处](https://roslibpy-docs-zh.readthedocs.io/zh/latest/)浏览。

roslibpy是一个连接Python与ROS环境的工具，安装roslibpy的主机无需再安装ROS环境便可以与ROS Master进行通信。

## 本地构建

Clone 该仓库到本地，然后进入项目根目录。

按照`requirements.txt`的要求自行安装所需要的 Python 依赖库。

### Linux

```shell
make html
```

### Windows

```shell
.\make.bat html
```

构建好的html文档位于`root/build/html`。