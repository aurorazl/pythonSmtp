
from distutils.core import setup, Extension
from Cython.Build import cythonize
setup(name='foo',
      version='1.0',
      ext_modules=cythonize([Extension('foo', ['build_test.py'])]),
      )
# setup(name='foo',
#       version='1.0',
#       ext_modules=cythonize('config.py'),
#       )