from distutils.core import setup

setup(
    name='cleverbot',
    version='0.2.1',
    description='An unofficial library to access the Cleverbot API',
    packages=['cleverbot'],
    install_requires=['future', 'requests'],
    tests_require=['pytest'],
    author='Rodney Folz',
    author_email='folz@rodneyfolz.com',
    url='https://github.com/folz/cleverbot.py',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
