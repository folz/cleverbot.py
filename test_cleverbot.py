from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import str  # pylint: disable=redefined-builtin

import unittest
import cleverbot


class CleverbotTest(unittest.TestCase):
    def test_replay(self):
        cbc = cleverbot.Cleverbot()
        response = cbc.ask("Hi. How are you?")
        self.assertNotEquals(response, str())
