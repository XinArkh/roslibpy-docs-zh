简介
====


主要特性
~~~~~~~~

* 话题 (Topic) 的发布和订阅；
* 服务 (Service) 的参数查询 (client端)；
* 服务 (Service) 的参数发布 (server端)；
* ROS 参数管理 (get/set/delete)；
* 用于获取 ROS 元信息 (meta-information) 的 ROS API 服务；
* 用于与可抢占任务连接的 Actionlib 支持；
* 通过 ``tf2_web_republisher`` 实现 TF Client。

**Roslibpy** 可以在 Python 2.7、Python 3.x 和 IronPython 2.7 上运行。


安装
~~~~

使用 ``pip`` 命令安装 **roslibpy**::
	pip install roslibpy

对于 IronPython 来说， ``pip`` 命令略有不同::
	ipy -X:Frames -m pip install --user roslibpy

.. Note::

   在连接的过程中需要保证你的网络中的 ROS 服务器配置并打开了 **rosbridge server** 和 **TF2 web republisher** 


文档
~~~~
完整版英文官方文档 `见此 <https://roslibpy.readthedocs.io/>`_。

`本文档 <https://roslibpy.readthedocs.io/>`_ 为中文非官方文档。


贡献
~~~~
