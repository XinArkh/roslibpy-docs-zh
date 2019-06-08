简介
====


**Python ROS Bridge library**，简称 **roslibpy**，提供了用 Python 或 IronPython 与开源机器人平台 `ROS <http://www.ros.org>`_ 进行通信的一个途径。\
该项目使用 WebSockets 与 `rosbridge 2.0 <http://wiki.ros.org/rosbridge_suite>`_ 建立连接，提供了 publishing、subscribing、service calls、actionlib、TF 等 ROS 中的基本功能。

与 `rospy <http://wiki.ros.org/rospy>`_ 不同，该项目\ **不需要在本地搭建 ROS 环境**，为 Linux 以外的平台使用 ROS 带来了方便。

**roslibpy** 的 API 构建参考了 `roslibjs`_ 的结构。


主要特性
--------

* 话题 (Topic) 的发布和订阅；
* 服务 (Service) 的发布和查询；
* ROS 参数管理 (get/set/delete)；
* ROS API 服务；
* Actionlib 支持；
* 通过 `tf2_web_republisher <http://wiki.ros.org/tf2_web_republisher>`_ 实现 TF Client。

**Roslibpy** 可以在 Python 2.7、Python 3.x 和 IronPython 2.7 上运行。


安装
----

使用\ ``pip``\ 命令安装 **roslibpy**::

    pip install roslibpy

对于 IronPython 来说，\ ``pip``\ 命令略有不同::

    ipy -X:Frames -m pip install --user roslibpy


文档
----

完整版英文官方文档\ `见此 <https://roslibpy.readthedocs.io/>`_。

`本文档 <https://roslibpy.readthedocs.io/>`_\ 为中文非官方文档。


贡献
----

确保您的本地环境配置正确：

* 将仓库 `roslibpy <https://github.com/gramaziokohler/roslibpy>`_ 克隆到本地；
* 创建一个虚拟环境；
* 安装开发依赖::

    pip install -r requirements-dev.txt

**现在你可以开始编程了！**

在开发过程中，使用 `pyinvoke <http://docs.pyinvoke.org/>`_ 来简化重复操作：

* ``invoke clean``: 清除所有生成的内容；
* ``invoke check``: 运行多种代码和文档风格检查；
* ``invoke docs``: 生成文档；
* ``invoke test``: 用一个命令迅速运行所有的测试和检查；
* ``invoke``: 显示可供调用的任务。

更多的细节请参考\ :ref:`contribution`\ 。


发布项目
--------

准备好发布 **roslibpy** 的新版本了吗？接下来是发布新版本的步骤：

* 我们使用 `semver <http://semver.org/>`_，即我们按照如下方式迭代版本：

    * ``patch``: 修复 BUG；
    * ``minor``: 增加向下兼容的 Feature；
    * ``major``: 向下兼容的修改。

* 所有的更改都要记录在 ``CHANGELOG.rst`` 中！
* 准备好了吗？用下面的命令来发布新版本::

    invoke release [patch|minor|major]

* Profit!


Credits
-------

本模块是基于 `roslibjs`_ 实现的，在很大程度上，它是到 Python 的逐行移植，只在其它惯用代码范式更有意义的地方才进行修改，\
所以很大一部分功劳要归于 `roslibjs 的作者 <https://github.com/RobotWebTools/roslibjs/blob/develop/AUTHORS.md>`_\ 。

.. _roslibjs: http://wiki.ros.org/roslibjs
