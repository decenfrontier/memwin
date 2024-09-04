from distutils.core import setup
from setuptools import find_packages
from version import version

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name='memwin',  # 包名
      version=version,  # 版本号
      description='一个python操作windows的 进程,线程,内存读写,DLL注入的库',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='decenfrontier',
      author_email='decenfrontier@gmail.com',
      url='https://github.com/decenfrontier/memwin',
      license='MIT License',
      packages=find_packages(),
      platforms=["win32"],
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
      ],
      python_requires='>=3.8',
      install_requires=[
          'pywin32',
          'psutil',
      ]
     )