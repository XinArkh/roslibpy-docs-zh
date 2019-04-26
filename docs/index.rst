******************
roslibpy 中文文档
******************


:作者: `Gramazio Kohler Research <https://github.com/gramaziokohler>`_

:译者: `Wu Hsin <https://github.com/XinArkh>`_

:授权: 该文档遵循 `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`_ 许可协议。

.. note::
   
   该文档为\ **非官方**\ 中文文档。 官方文档可以\ `在此获得 <https://roslibpy.readthedocs.io/en/latest/>`_。

**Python ROS Bridge library**，简称 **roslibpy**，提供了用 Python 或 IronPython 与开源机器人平台 `ROS <http://www.ros.org>`_ 进行通信的一个途径。
该项目使用 WebSockets 与 `rosbridge 2.0 <http://wiki.ros.org/rosbridge_suite>`_ 建立连接，提供了 publishing、subscribing、service calls、actionlib、TF 等 ROS 中的基本功能。

与 `rospy <http://wiki.ros.org/rospy>`_ 不同，该项目\ **不需要在本地搭建 ROS 环境**，为 Linux 以外的平台使用 ROS 带来了方便。

**roslibpy** 的 API 构建参考了 `roslibjs <http://wiki.ros.org/roslibjs>`_ 的结构。


.. toctree::
   :maxdepth: 2
   :caption: 目录
   :numbered:

   introduction
   examples
   api
   contribution
   authors
   changelog


索引
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
