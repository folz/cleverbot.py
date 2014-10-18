import unittest

import cleverbot


class Cleverbot(unittest.TestCase):
    def test_replay(self):
        cbc = cleverbot.Cleverbot()
        response = cbc.ask("Hi. How are you?")
        self.assertNotEquals(result, str())


def main():
    unittest.main()

if __name__ == '__main__':
    main()