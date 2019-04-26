快速上手
========

**roslibpy** 上手非常简单。在接下来的例子中你将看到如何使用它与一个 ROS 环境相连接。

.. Note::

    在连接的过程中，确保在你网络中的 ROS 服务器配置并打开了 **rosbridge server** 和 **TF2 web republisher**\ （具体请戳 :ref:`ros-setup`\ ）

这些例子假定了 ROS 服务器运行在同一台主机上。对于不在同一台主机的情况，只需要将\ ``host``\ 参数从\ ``'localhost'``\ 改为 ROS master 的 *IP 地址*\ 。

.. Note::

    ``port``\ 参数必须设定为\ ``9090``\ ，因为\ ``rosbridge``\ 的默认端口号是\ ``9090``\ 。如果想改变端口号，可参考\ `这里 <https://github.com/gramaziokohler/roslibpy/issues/21#issuecomment-481685223>`_\ 。


第一个例子
----------

用以下命令导入\ ``roslibpy``::

    >>> import roslibpy

用以下命令初始化连接::

    >>> ros = roslibpy.Ros(host='localhost', port=9090)
    >>> ros.run()

是不是很简单？

上面的命令开启了一个非阻塞的连接，也就是说，与 ROS 的连接是在后台建立的，但是函数不等连接建立成功就会马上返回。

让我们检查一下连接状态::

    >>> ros.is_connected
    True

**耶( •̀ ω •́ )y 这就是我们的第一个例子！**


等待连接
--------

前面的例子能够成功，是因为我们是在终端敲代码输入命令，这对于建立一个连接所需要的时间来说\ **通常**\ 是足够慢的。但是，当代码以脚本的形式运行，处理速度会很快，我们希望确保一些代码只有在连接成功建立后才会执行。

对于这种情况，我们需要使用 **roslibpy.Ros.on_ready** 方法，这个方法会在连接成功建立后调用我们设定的一个函数或 lambda 表达式。

在这里我们简单地打印输出是否成功连接的信息::

    ros.on_ready(lambda: print('Is ROS connected?', ros.is_connected))


在实际使用中你可以将这部分修改为任何 ROS 相关的操作，如话题的订阅或呼叫一个服务等。


融会贯通
--------

让我们以 Python 文件的形式建立一个完整的例子。

新建一个文件并命名为\ ``ros-hello-world.py``\ ，然后复制粘贴以下内容：

.. literalinclude:: files/ros-hello-world.py
    :language: python

在命令行中输入以下命令运行该程序::

    $ python ros-hello-world.py

这个程序运行起来之后，会进入一个死循环，同时等待与 ROS 建立连接后打印输出。

.. Note::

    **roslibpy.Ros.on_ready** 方法只是一次性地设定连接成功后的回调函数，并不会阻塞程序来等待连接。

要中断程序并回到终端，按下\ ``Ctrl+C``\ 即可。


控制事件循环
------------

在之前的例子里，我们通过调用\ ``run()``\ 来开启与 ROS 的连接，但是有时候我们想要\ ``roslibpy``\ 来操心主事件循环。在这种情况下，调用\ ``run_forever()``\ 更方便一点。

接下来的代码片段用\ ``run_forever()``\ 实现了与之前的例子同样的功能：

.. literalinclude:: files/ros-hello-world-run-forever.py
    :language: python

.. Note::

    \ ``run()``\ 与\ ``run_forever()``\ 的区别在于，前者新开一个单独的线程来处理事件，而后者会阻塞当前线程。


Hello World: 话题（Topics）
---------------------------

ROS 中的\ ``Hello World``\ 例子是开启两个节点，并利用话题的订阅/发布来建立通讯。这两个节点（一个 talker 和一个 listener）非常简单，但是透过它们可以便于理解在 ROS 框架下的分布式系统中，两个进程之间的通信是如何工作的。

接下来，我们用 **roslibpy** 来建立一个简单的话题通讯。


一个 talker 节点
^^^^^^^^^^^^^^^^

接下来的例子是开启一个 ROS 节点并循环发布信息（按下\ ``Ctrl+C``\ 来关闭）。


.. literalinclude:: files/ros-hello-world-talker.py
    :language: python

* :download:`ros-hello-world-talker.py <files/ros-hello-world-talker.py>`


一个 listener 节点
^^^^^^^^^^^^^^^^^^

现在让我们把视线移到 listener 端：

.. literalinclude:: files/ros-hello-world-listener.py
    :language: python

* :download:`ros-hello-world-listener.py <files/ros-hello-world-listener.py>`


跑起来
^^^^^^

打开一个终端，开启 talker 节点::

    $ python ros-hello-world-talker.py

打开另一个终端，开启 listener 节点::

    $ python ros-hello-world-listener.py

.. Note::

    两个文件的位置不必在一起，它们可以在不同的路径、甚至不同的计算机中，只要保证是同一个 Ros master 即可。

使用服务（Services）
--------------------

节点之间的另一种通讯方式是通过 ROS 服务来进行。

服务需要定义请求和回应的类型，所以所以下面的例子使用了现成的\ ``get_loggers``\ 服务：

.. literalinclude :: files/ros-service-caller.py
    :language: python

* :download:`ros-service-caller.py <files/ros-service-caller.py>`
