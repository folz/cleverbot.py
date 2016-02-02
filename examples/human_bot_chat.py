"""Chat with Cleverbot in Python."""
from __future__ import print_function
from builtins import input
import traceback

import cleverbot


def main():
    # instantiate a Cleverbot object
    cleverbot_client = cleverbot.Cleverbot()

    while True:
        question = input('>> You: ')
        answer = cleverbot_client.ask(question)
        print('>> Cleverbot: {}'.format(answer))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))