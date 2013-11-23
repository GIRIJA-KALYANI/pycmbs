from distutils.core import setup
import os


install_requires=["numpy>0.1","cdo>1.2",]


setup(name='pyCMBS',
      version='0.1.4-rev',
      py_modules=['pyCMBS',],
      author = "Alexander Loew",
      author_email='alexander.loew@mpimet.mpg.de',
      maintainer='Alexander Loew',
      maintainer_email='alexander.loew@mpimet.mpg.de',
      url='https://code.zmaw.de/projects/pycmbs',
      description='pyCMBS - python Climate Model Benchmarking Suite',
      long_description='The pyCMBS project is a suite of tools to process, analyze, visualize and benchmark scientific model output against each other or against observational data. It is in particular useful for analyzing in an efficient way output from climate model simulations.',
      install_requires=install_requires,
      license = ""      )

#print('Compressing sample data ...')
#ofile='./dist/example_data.tgz'
#cmd='tar -cvzf ' + ofile + ' example_data'
#if os.path.exists(ofile):
#    os.remove(ofile)
#os.system(cmd)


print ''
print 'Your original PYTHONPATH is:'
print os.environ['PYTHONPATH']
print''
print 'Please change your PYTHONPATH (permanently) in your shell configuration file as follows:'
print ''
print 'For BASH shell users include in your .bashrc:'
curdir = os.getcwd()
print '     export PYTHONPATH=' + curdir + ':$PYTHONPATH'
print '     export SEP="/pool/SEP"'
print 'The latter is only for users at ZMAW'


#todo:
#- set PYTHONPATH to directory, where user installs pyCMBS, sys.path ???
#
#what to do with the TAR-file
#1) download and extract it
#2) rename directory with version number to 'pyCMBS'
#3) put pyCMBS directory in your path



#PIP
#~ py_modules --> remote identifier ???
#~
#~
#~ python setup.py register
#~ python setup.py sdist
#~ python setup.py upload




#python GMT !!!



#ARcLinux ???



