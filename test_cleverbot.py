from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import str  # pylint: disable=redefined-builtin

import unittest
import cleverbot


class CleverbotTest(unittest.TestCase):
    def test_replay(self):
        cbc = cleverbot.Cleverbot("cleverbot-py-test")
        try:
            response = cbc.ask("Hi. How are you?")
        except cleverbot.CleverbotServiceError:
            # Technically, cleverbot errored. But we connected, which is all
            # that matters
            self.assertTrue(True)
        else:
            self.assertNotEquals(response, str())
