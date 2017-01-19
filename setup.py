from distutils.core import setup

setup(
    name='cleverbot',
    version='2.0.0',
    url='https://github.com/folz/cleverbot.py',
    author='Rodney Folz',
    author_email='pypi@rodneyfolz.com',
    description='An unofficial library to access the Cleverbot service',
    license='BSD-2-Clause',
    packages=['cleverbot'],
    install_requires=['future', 'requests'],
    tests_require=['pytest'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
