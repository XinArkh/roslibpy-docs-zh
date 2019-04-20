from setuptools import setup, find_packages

setup(name="roslibpy-docs-zh",
      version="0.0.0",
      description="",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      author='Wu Hsin',
      install_requires=['setuptools',
                        'sphinx',
                        'sphinx_rtd_theme',
                        ],
      )
