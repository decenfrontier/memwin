from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='memwin',  # 包名
      version='0.0.1',  # 版本号
      description='一个python操作windows的 进程,线程,内存读写,HOOK的库',
      long_description=long_description,
      author='decenfrontier',
      author_email='decenfrontier@gmail.com',
      url='https://github.com/decenfrontier',
      install_requires=[],
      license='MIT License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: Windows',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
     )