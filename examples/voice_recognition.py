#!/usr/bin/python
# -*- coding: utf-8 -*-
import traceback
import speech_recognition as sr
import cleverbot
import sys
import unittest

r = sr.Recognizer()
with sr.Microphone() as source:  # audio source microphone ( computer default)

    def main():
        bot = cleverbot.Cleverbot()
        while True:
            audio = r.listen(source)
            question = r.recognize(audio)
            if question == 'exit' or question == 'Exit':
                print('Goodbye')
                sys.exit()
            print('Me:' + question)
            answer = bot.ask(question)
            print('Cleverbot: {}'.format(answer))

    if __name__ == '__main__':
        try:
            main()
        except Exception :
            print(traceback.format_exc(err))

