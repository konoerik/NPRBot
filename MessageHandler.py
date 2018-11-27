from feeds import  FEEDS

class MessageHandler():
    """
    > pprint(msg)
    {'chat': {'first_name': 'Erikton Konomi',
              'id': 457490,
              'type': 'private',
              'username': 'konoerik'},
     'date': 1543281379,
     'entities': [{'length': 6, 'offset': 0, 'type': 'bot_command'}],
     'from': {'first_name': 'Erikton Konomi',
              'id': 457490,
              'is_bot': False,
              'language_code': 'en',
              'username': 'konoerik'},
     'message_id': 68,
     'text': '/hello'}
    """

    def __init__(self, msg):

        # from telegram msg
        self._chat = msg['chat']
        self._date = msg['date']
        self._entities = msg['entities']
        self._from = msg['from']
        self._message_id = msg['message_id']
        self._text = msg['text']

        # extra parsing
        self._cmd = self._text.split()[0]
        self._arg = self._text.split()[1:]

    def reply(self):
        if self._cmd == '/help':
            return self.help()
        elif self._cmd == '/recent':
            return self.recent()
        elif self._cmd == '/list':
            return self.list()
        elif self._cmd == '/host':
            return self.host()
        elif self._cmd == '/guest':
            return self.guest()
        elif self._cmd == '/last':
            return self.last()
        else:
            return "Unsupported command!"

    def help(self):
        """Return a simple help message"""

        message = """
        Use this bot to look up podcasts from NPR!
        For a list of available commands, type '/' and follow the prompt.
        Have fun! 
        """

        return message

    def recent(self):
        """Query the DB for the last ten items and return"""

        temp_list = ['abc', 'def', '123']
        return "\n".join(temp_list)

    def list(self):
        """Return a list of all podcast series being tracked"""

        return "\n".join(FEEDS.keys())

    def host(self):
        """Query the DB for podcast series where the host matches the description"""

        temp_list = ['pod_a', 'pod_b']
        return "\n".join(temp_list)

    def guest(self):
        """Query the DB for episodes where the guest matches the description"""

        temp_list = ['episode_a', 'episode_b']
        return "\n".join(temp_list)

    def last(self):
        """Query the DB for the most recent episode for the given podcast series"""

        return "episode_255"