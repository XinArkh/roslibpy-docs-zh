.. _contribution:

开发者指南
==========


我们非常欢迎更多贡献者的参与到这个项目中来。


代码贡献
---------

我们欢迎任何人 pull request！
这里有一份改善代码的快速指南：

1. Fork并 clone \ `这个仓库 <https://github.com/gramaziokohler/roslibpy>`_\ ；
2. 用你喜欢的工具创建一个虚拟环境（如\ ``virtualenv``\ 、\ ``conda``\ 等）；
3. 安装开发依赖::

    pip install -r requirements-dev.txt

4. 确保所有的测试通过::

    invoke test

5. 把你的更改更新到主分支（或从主分支分叉的其它分支）；
6. 再次确保所有的测试通过::

    invoke test

7. 把你的名字添加到\ ``AUTHORS.rst``\ 里面；
8. Commit+push你的改变到 GitHub 仓库；
9. 通过 GitHub 页面新建一个\ `pull request <https://help.github.com/articles/about-pull-requests/>`_\ 。

在开发过程中，使用 `pyinvoke <http://docs.pyinvoke.org/>`_ 来简化重复操作：

* ``invoke clean``: 清除所有生成的内容；
* ``invoke check``: 运行多种代码和文档风格检查；
* ``invoke docs``: 生成文档；
* ``invoke test``: 用一个命令迅速运行所有的测试和检查；
* ``invoke``: 显示可供调用的任务。


文档贡献
--------

文档总是多多益善，无论是作为介绍/示例/使用文档的一部分，还是 docstrings 里面的 API 文档。

文档使用 `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ 撰写，
并用 `Sphinx <http://sphinx-doc.org/index.html>`_ 生成 HTML 格式的输出。

在你更改本地文档之后，运行以下命令来重新生成它::

    invoke docs


报告 BUG
---------

在你想要\ `报告一个 BUG <https://github.com/gramaziokohler/roslibpy/issues>`_ 的时候，请包括以下内容：

    * 操作系统名称及版本；
    * ROS 版本；
    * 任何可能有助于排除故障的、有关你的本地配置的细节；
    * 重现这个 BUG 的详细步骤。


Feature 的建议与反馈
--------------------

提供反馈最好的方式是新开一个 `GitHub issue <https://github.com/gramaziokohler/roslibpy/issues>`_。
如果你提出一个新的 feature，请：
    * 详细解释它的工作机理；
    * 使其涉及的范围尽可能小，以便实现。
