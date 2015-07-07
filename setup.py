# Ref: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
from setuptools import setup


setup(name='Kalman',
      version='0.1.3',
      packages=['Kalman'],
      url='http://github.com/MBALearnsToCode/KalmanPy',
      author='Vinh Luong (a.k.a. MBALearnsToCode)',
      author_email='MBALearnsToCode@UChicago.edu',
      description='Kalman Filters',
      long_description='(please read README.md on GitHub repo)',
      license='MIT License',
      install_requires=['NumPy'],
      classifiers=[],   # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='kalman filter')
