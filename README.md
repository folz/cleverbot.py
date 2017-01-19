# Cleverbot.py [![Travis](https://img.shields.io/travis/folz/cleverbot.py.svg?style=flat-square)](https://travis-ci.org/folz/cleverbot.py) [![PyPI Version](https://img.shields.io/pypi/v/cleverbot.svg?style=flat-square)](https://pypi.python.org/pypi/cleverbot) [![Python Versions](https://img.shields.io/pypi/pyversions/cleverbot.svg?style=flat-square)](https://pypi.python.org/pypi/cleverbot)

Cleverbot.py is an unofficial library to access the Cleverbot service.

```python
>>> from cleverbot import Cleverbot

>>> cb = Cleverbot('my-app')
>>> cb.ask("Hi. How are you?")
"I'm good, thanks. How are you?"
```

(Note: actual reply may vary, and will probably make fun of you. This _is_ Cleverbot, after all.)

## Installation

To install cleverbot.py, simply:

```bash
$ pip install cleverbot
```

Boom!

How to Contribute
-----

Comments, pull requests, documentation, and other feedback are warmly welcome!

1. Check for [open issues](https://github.com/folz/cleverbot.py/issues) or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :)
