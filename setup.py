# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['modbus', 'module_io', 'serial_io', 'module_utils', 'exposed_resources', 'http_io', 'i2c_io', 'enums',
              'data_models', 'parameters'],
    package_dir={'': 'scripts'})

setup(**setup_args)
