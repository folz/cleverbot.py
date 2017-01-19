"""Cleverbot chats with himself."""
from __future__ import print_function
import traceback

from cleverbot import Cleverbot


def main():
    # Create two Cleverbot connections
    alice = Cleverbot('cleverbot-py-example')
    bob = Cleverbot('cleverbot-py-example')

    print('>> Alice: Hi.')
    answer = bob.ask('Hi.')

    while True:
        print('>> Bob: {}'.format(answer))
        answer = alice.ask(answer)
        print('>> Alice: {}'.format(answer))
        answer = bob.ask(answer)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))
