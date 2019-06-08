r"""

此模块依赖 Robot Web Tools 所开发的 `ROS bridge suite <http://wiki.ros.org/rosbridge_suite>`_\ ，
通过 WebSockets 实现与 ROS 的交互。

`ROS bridge protocol <https://github.com/RobotWebTools/rosbridge_suite/blob/master/ROSBRIDGE_PROTOCOL.md>`_
使用 JSON 格式信息传输
publishing, subscribing, service calls, actionlib, TF 等 ROS 中的功能。

.. _ros-setup:

ROS 设置
--------

使用本模块，必须在 ROS 环境中配置并运行\ ``rosbridge``\ 。

首次连接之前，在 ROS master所在环境用以下命令安装\ **rosbridge suite**::

    sudo apt-get install -y ros-kinetic-rosbridge-server
    sudo apt-get install -y ros-kinetic-tf2-web-republisher

在以后的每次连接之前，都要确保预先开启了以下服务::

    roslaunch rosbridge_server rosbridge_websocket.launch
    rosrun tf2_web_republisher tf2_web_republisher

.. note::

    执行\ ``roslaunch``\ 命令时，会自动运行\ ``roscore``\ 命令，因此使用启动文件运行节点时不需要新开终端运行\ ``roscore``\ 。


连接 ROS
--------

与 ROS 的连接是由\ :class:`Ros`\ 类来处理的。除了连接和信息处理，在需要的时候它也会自动重连。

其他需要与 ROS 进行连接的类会将此实例作为其构造函数的参数接收。

.. autoclass:: Ros
   :members:


ROS 主要概念
--------------

话题
^^^^^

ROS 是一个通信框架。 在 ROS 里面, 不同的 **节点** 通过 messages 与其它节点通信。\
**ROS messages** 在\ :class:`Message`\ 类中实现，\
并通过\ :class:`Topics <Topic>`\ 的\ **发布/订阅**\ 模型来传输。

.. autoclass:: Message
   :members:
.. autoclass:: Topic
   :members:

服务
^^^^^

除了话题的发布/订阅模型，ROS 还通过\ :class:`Services <Service>`\ 类提供了一套\ **请求/响应**\ 模型。

.. autoclass:: Service
   :members:
.. autoclass:: ServiceRequest
   :members:
.. autoclass:: ServiceResponse
   :members:


参数服务器
^^^^^^^^^^

ROS 提供了用于在不同节点之间分享数据的参数服务器。\
该服务通过\ :class:`Param`\ 类来实现。

.. autoclass:: Param
   :members:

"""

from .__version__ import __author__
from .__version__ import __author_email__
from .__version__ import __copyright__
from .__version__ import __description__
from .__version__ import __license__
from .__version__ import __title__
from .__version__ import __url__
from .__version__ import __version__
from .core import Message
from .core import Param
from .core import Service
from .core import ServiceRequest
from .core import ServiceResponse
from .core import Topic
from .ros import Ros

__all__ = ['Ros', 'Message', 'Param', 'Service', 'ServiceRequest', 'ServiceResponse', 'Topic', '__author__',
           '__author__', '__author_email__', '__copyright__', '__description__', '__license__', '__title__', '__url__', '__version__']
