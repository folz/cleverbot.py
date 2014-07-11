"""Chat with Cleverbot in Python."""
import traceback

import cleverbot


def main():
    # instantiate a Cleverbot object
    cleverbot_client = cleverbot.Cleverbot()

    while True:
        question = raw_input('>> You: ')
        answer = cleverbot_client.ask(question)
        print '>> Cleverbot: {}'.format(answer)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '>> Exiting...'
    except Exception, err:
        print traceback.format_exc(err)