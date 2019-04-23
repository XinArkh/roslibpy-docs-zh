快速上手
========

**roslibpy** 上手非常简单。在接下来的例子中你将看到如何使用它与一个 ROS 环境相连接。

.. Note::

    在连接的过程中，确保在你网络中的 ROS 服务器配置并打开了 **rosbridge server** 和 **TF2 web republisher**\ （具体请戳 :ref:`ros-setup`\ ）

这些例子假定了 ROS 服务器运行在同一台主机上。对于不在同一台主机的情况，只需要将 ``host`` 参数从 ``'localhost'`` 改为 ROS master 的 *IP 地址*\ 。

.. Note::

    ``port`` 参数必须设定为 ``9090``，因为 ``rosbridge`` 的默认端口号是 ``9090``。如果想改变端口号，可参考\ `这里 <https://github.com/gramaziokohler/roslibpy/issues/21#issuecomment-481685223>`_\ 。


首次连接
~~~~~~~~

用以下命令导入 ``roslibpy``::

    >>> import roslibpy

用以下命令初始化连接::

    >>> ros = roslibpy.Ros(host='localhost', port=9090)
    >>> ros.run()

是不是很简单？

上面的命令开启了一个非阻塞的连接，也就是说，连接是在后台建立的，但是函数不等连接建立成功就会马上返回。

让我们检查一下连接状态::

    >>> ros.is_connected
    True

**耶( •̀ ω •́ )y 这就是我们与 ROS 的首次连接！**


等待连接
~~~~~~~~

前面的例子能够成功，是因为我们是在终端敲代码输入命令，这对于建立一个连接所需要的时间来说\ **通常**\ 是足够慢的。但是，当代码以脚本的形式运行，处理速度会很快，我们希望确保一些代码只有在连接成功建立后才会执行。

对于这种情况，我们需要使用 **roslibpy.Ros.on_ready** 方法，这个方法会在连接成功建立后调用我们设定的一个函数或 lambda 表达式。

在这里我们简单地打印输出是否成功连接的信息::

    ros.on_ready(lambda: print('Is ROS connected?', ros.is_connected))


在实际使用中你可以将这部分修改为任何 ROS 相关的操作，如话题的订阅或呼叫一个服务等。


融会贯通
~~~~~~~~

让我们将一个完整的例子以一个 Python 文件的形式建立。

新建一个文件并命名为 ``ros-hello-world.py``\ ，然后复制粘贴以下内容：
