from setuptools import setup, find_packages

setup(
  name="toolbox",
  version="1.0",
  py_modules="info",
  packages=find_packages(),
  install_requires=[
    'click',
    'rich'
  ],
  entry_points='''
  [console_scripts]
  tb=commands:cli
  '''
)