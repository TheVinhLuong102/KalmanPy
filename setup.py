# Ref: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
from setuptools import setup


setup(name='Kalman',
      version='0.3',
      packages=['Kalman'],
      url='http://github.com/MBALearnsToCode/KalmanPy',
      author='Vinh Luong (a.k.a. MBALearnsToCode)',
      author_email='MBALearnsToCode@UChicago.edu',
      description='Kalman Filters',
      long_description=open('README.txt').read(),
      license='MIT License')
