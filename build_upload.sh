# # 第一次运行要装:
# ```sh
# python3 -m pip install --user --upgrade setuptools wheel
# pip install twine
# ```

# # 单元测试
# ```sh
# pip install pytest
# pytest -s
# ```


rm -Force .\dist\*
python setup.py sdist build
twine upload dist/*