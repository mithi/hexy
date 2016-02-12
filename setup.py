from setuptools import setup

setup(name = 'hexy',
      version = '0.1',
      description = 'Hexapod Robot Code',
      url = 'http://github.com/mithi/hexy',
      author = 'Mithi',
      author_email = 'mithi.sevilla@gmail.com',
      license = 'MIT',
      packages = ['hexy', 'hexy.robot', 'hexy.demo', 'hexy.comm'],
      zip_safe = False)
