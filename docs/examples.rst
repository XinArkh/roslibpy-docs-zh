快速上手
========


**roslibpy** 上手非常简单。在接下来的例子中你将看到如何使用它与一个 ROS 环境相连接。

.. note::

    在连接的过程中，确保在你网络中的 ROS 服务器配置并打开了 **rosbridge server** 和 **TF2 web republisher**\ （具体请戳 :ref:`ros-setup`\ ）

这些例子假定了 ROS 服务器运行在同一台主机上。对于不在同一台主机的情况，只需要将\ ``host``\ 参数从\ ``'localhost'``\ 改为 ROS master 的 *IP 地址*\ 。

.. note::

    ``port``\ 参数必须设定为\ ``9090``\ ，因为\ ``rosbridge``\ 的默认端口号是\ ``9090``\ 。如果想改变端口号，\
    可参考\ `这里 <https://github.com/gramaziokohler/roslibpy/issues/21#issuecomment-481685223>`_\ 。


第一个例子
----------

用以下命令导入\ ``roslibpy``::

    >>> import roslibpy

用以下命令初始化连接::

    >>> ros = roslibpy.Ros(host='localhost', port=9090)
    >>> ros.run()

是不是很简单？

让我们检查一下连接状态::

    >>> ros.is_connected
    True

**耶( •̀ ω •́ )y 我们的第一个例子成功跑通！**


融会贯通
--------

让我们以 Python 文件的形式建立一个完整的例子。

新建一个文件并命名为\ ``ros-hello-world.py``\ ，然后复制粘贴以下内容：

.. literalinclude:: files/ros-hello-world.py
    :language: python

在命令行中输入以下命令运行该程序::

    $ python ros-hello-world.py

这个程序运行起来之后，会尝试建立与 ROS 的连接，连接建立后打印输出信息，并终止连接。


控制事件循环
------------

在之前的例子里，我们通过调用\ ``run()``\ 来开启与 ROS 的连接，这样会在后台开启一个事件循环。在某些情况下，\
我们希望在前台更明确地处理主事件循环，\ :class:`roslibpy.Ros` 提供了一个\ ``run_forever()``\ 方法来做这件事。

如果我们如果使用这个方法启动事件循环，则需要事先设置好所有连接处理配置。我们使用\ :meth:`roslibpy.Ros.on_ready`\ 来做这件事。


接下来的代码片段用\ ``run_forever()``\ 和\ ``on_ready()``\ 实现了与之前的例子同样的功能：

.. literalinclude:: files/ros-hello-world-run-forever.py
    :language: python

.. note::

    \ ``run()``\ 与\ ``run_forever()``\ 的区别在于，前者新开一个单独的线程来处理事件，而后者会阻塞当前线程。


Hello World: 话题（Topics）
---------------------------

ROS 中的\ ``Hello World``\ 例子是开启两个节点，并利用话题的订阅/发布来建立通讯。这两个节点（一个 talker 和一个 listener）非常简单，\
但是透过它们可以便于理解在 ROS 框架下的分布式系统中，两个进程之间的通信是如何工作的。

接下来，我们用 **roslibpy** 来建立一个简单的话题通讯。


一个 talker 节点
^^^^^^^^^^^^^^^^

接下来的例子是开启一个 ROS 节点并循环发布信息（按下\ ``Ctrl+C``\ 来终止）。


.. literalinclude:: files/ros-hello-world-talker.py
    :language: python

* :download:`ros-hello-world-talker.py <files/ros-hello-world-talker.py>`

.. note::

    这里以 ROS 中的 `std_msgs/String <http://docs.ros.org/api/std_msgs/html/msg/String.html>`_ 消息类型为例，其它消息类型\
    也可以利用 Python 字典的方式构建，参考\ `这个例子 <https://github.com/gramaziokohler/roslibpy/issues/11#issuecomment-428178646>`_\ 。


一个 listener 节点
^^^^^^^^^^^^^^^^^^

Listener 端的代码如下：

.. literalinclude:: files/ros-hello-world-listener.py
    :language: python

* :download:`ros-hello-world-listener.py <files/ros-hello-world-listener.py>`


运行例程
^^^^^^^^^^^

打开一个终端，开启 talker 节点::

    $ python ros-hello-world-talker.py

打开另一个终端，开启 listener 节点::

    $ python ros-hello-world-listener.py

.. note::

    两个文件的位置不必在一起，它们可以在不同的路径、甚至不同的计算机中，只要保证是同一个 Ros master 即可。

使用服务（Services）
--------------------

节点之间的另一种通讯方式是通过 ROS 服务来进行。

服务一般需要定义请求和回应的类型，为了简单，下面的例子使用了现成的\ ``get_loggers``\ 服务：

.. literalinclude :: files/ros-service-call-logger.py
    :language: python

* :download:`ros-service-call-logger.py <files/ros-service-call-logger.py>`

创建服务（Services）
-----------

只要服务类型的定义存在于您的 ROS 环境中，就可以创建新服务。

下面的例子展示了如何创建一个简单的服务，它使用ROS 中定义的标准服务类型之一（``std_srvs/SetBool``）:

.. literalinclude :: files/ros-service.py
    :language: python

* :download:`ros-service.py <files/ros-service.py>`

下载该脚本，并输入如下命令::

    $ python ros-service.py

程序开始运行，期间服务会一直处于活动状态（按下\ ``Ctrl+C``\ 来终止）。

不要关闭这个服务，下载并运行以下代码示例来调用服务，以验证服务是否正常工作:

* :download:`ros-service-call-set-bool.py <files/ros-service-call-set-bool.py>`

下载后在一个新的终端中键入以下命令::

    $ python ros-service-call-set-bool.py

.. note::

    现在您已经掌握了 **roslibpy** 的基础知识，更多细节请查看 :ref:`ros-api-reference`\ 。

Actions
--------

除了话题和服务之外，ROS还提供 **Actions**，它们被用于长时间运行的任务，比如导航，因为它们是非阻塞的，并且允许任务执行时被抢占和取消。

**roslibpy** 既支持 action 客户端，也可以通过 :class:`roslibpy.actionlib.SimpleActionServer`\ 提供 action 服务器。

下面的例子使用\ **斐波那契** action，该 action 的定义可在 `actionlib_tutorials <http://wiki.ros.org/actionlib_tutorials>`_ 中查看。

Action 服务器
^^^^^^^^^^^^^^^^

让我们从斐波那契服务器的定义开始：

.. literalinclude :: files/ros-action-server.py
    :language: python

* :download:`ros-action-server.py <files/ros-action-server.py>`

下载后键入以下命令::

    $ python ros-action-server.py

在程序运行时，\ action 服务器将保持活动状态（按下\ ``Ctrl+C``\ 来终止）。

如果您想在下一个示例中测试这个窗口，请不要关闭它。

Action 客户端
^^^^^^^^^^^^^^^^^

现在，让我们看看如何为新创建的服务器编写一个 action 客户端。

下面的程序显示了一个简单的 action 客户端：

.. literalinclude :: files/ros-action-client.py
    :language: python

* :download:`ros-action-client.py <files/ros-action-client.py>`

下载后键入以下命令::

    $ python ros-action-client.py

您将立即看到我们的 action 服务器的所有中间计算，并在最后一行显示生成的斐波那契数列。

这个例子非常简单，使用了 :meth:`roslibpy.actionlib.Goal.wait` 函数，以使代码更易于阅读。一个更鲁棒的处理方法是使用回调把结果连接到 ``result`` 事件。
