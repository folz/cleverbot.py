from hashlib import md5
import pprint
import urllib, urllib2

class Cleverbot:

    HOST = "www.cleverbot.com"
    PROTOCOL = "http://"
    RESOURCE = "/webservicemin"
    API_URL = PROTOCOL + HOST + RESOURCE

    DEBUG = False

    headers = \
        { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        , 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        , 'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
        , 'Accept-Language' : 'en-us,en;q=0.8,en-us;q=0.5,en;q=0.3'
        , 'Cache-Control' : 'no-cache'
        , 'Host' : HOST
        , 'Referer' : PROTOCOL + HOST + '/'
        , 'Pragma' : 'no-cache'
        }

    def __init__(self, debug=False):
        self.DEBUG = debug
        self.__debug("Initializing new session")

        """ The data that will get passed to Cleverbot's web API """
        self.data = \
            { 'stimulus' : ''
            , 'start' : 'y' # Never modified
            , 'sessionid' : ''
            , 'vText8' : ''
            , 'vText7' : ''
            , 'vText6' : ''
            , 'vText5' : ''
            , 'vText4' : ''
            , 'vText3' : ''
            , 'vText2' : ''
            , 'icognoid' : 'wsf' # Never modified
            , 'icognocheck' : ''
            , 'fno' : 0 # Never modified
            , 'prevref' : ''
            , 'emotionaloutput' : '' # Never modified
            , 'emotionalhistory' : '' # Never modified
            , 'asbotname' : '' # Never modified
            , 'ttsvoice' : '' # Never modified
            , 'typing' : '' # Never modified
            , 'lineref' : ''
            , 'sub' : 'Say' # Never modified
            , 'islearning' : 1 # Never modified
            , 'cleanslate' : False # Never modified
            }

        """ The log of our conversation with Cleverbot """
        self.conversation=[]

    def ask(self,q):
        """Asks Cleverbot a question.
        
        Maintains message history.

        Args:
            q (str): The question to ask
        Returns:
            Cleverbot's answer
        """
        self.__debug("Asking a question", q)

        # Set the current question
        self.data['stimulus'] = q

        # Connect to Cleverbot's API and remember the response
        resp = self._send()

        # TODO ensure Cleverbot received the question properly

        # Add the current question to the conversation log
        self.conversation.append(q)

        parsed = self._parse(resp)

        # Set data as appropriate
        if self.data['sessionid'] != '':
            self.data['sessionid'] = parsed['conversation_id']

        # Add Cleverbot's reply to the conversation log
        self.conversation.append(parsed['answer'])

        return parsed['answer']

    def _send(self):
        """POST the user's question and all required information to the 
        Cleverbot API

        Cleverbot tries to prevent unauthorized access to its API by
        obfuscating how it generates the 'icognocheck' token, so we have
        to URLencode the data twice: once to generate the token, and
        twice to add the token to the data we're sending to Cleverbot.
        """
        self.__debug("Sending data")

        # Set data as appropriate
        if self.conversation:
            linecount = 1
            for line in reversed(self.conversation):
                linecount += 1
                self.data['vText'+str(linecount)] = line
                if linecount == 8:
                    break

        # Generate the token
        enc_data = urllib.urlencode(self.data)
        digest_txt = enc_data[9:29]
        token = md5(digest_txt).hexdigest()
        self.data['icognocheck'] = token

        # Add the token to the data
        enc_data = urllib.urlencode(self.data)
        req = urllib2.Request(self.API_URL, enc_data, self.headers)

        # POST the data to Cleverbot's API
        conn = urllib2.urlopen(req)
        resp = conn.read()

        # Return Cleverbot's response
        return resp

    def _parse(self, text):
        """Parses Cleverbot's response"""

        self.__debug("Parsing response")

        parsed = map(lambda e: e.split('\r'), text.split('\r\r\r\r\r\r')[:-1])

        return \
            { 'answer' : parsed[0][0]
            , 'conversation_id' : parsed[0][1]
            , 'conversation_log_id' : parsed[0][2]
            , 'unknown': parsed[1][-1]
            }

    def __debug(self, *args):
        """Print stuff to stdin if DEBUG is true"""

        if self.DEBUG:
            print args

if __name__ == "__main__":
    cb1 = Cleverbot()
    cb2 = Cleverbot()

    resp1 = cb1.ask("Hello.")
    print "Bob:", "Hello"

    while True:
        print "Alice:", resp1
        resp2 = cb2.ask(resp1)
        print "Bob:", resp2
        resp1 = cb1.ask(resp2)
