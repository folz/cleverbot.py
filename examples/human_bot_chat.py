"""Chat with Cleverbot in Python."""
from __future__ import print_function
from builtins import input
import traceback

from cleverbot import Cleverbot


def main():
    # instantiate a Cleverbot object
    client = Cleverbot('cleverbot-py-example')

    while True:
        question = input('>> You: ')
        answer = client.ask(question)
        print('>> Cleverbot: {}'.format(answer))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))
