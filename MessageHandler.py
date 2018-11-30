from feeds import  FEEDS
import sqlite3

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
        # the idea is: for commands like "/host guy raz", /host is the cmd and 'guy raz' is the argument
        self._cmd = self._text.split()[0]
        self._arg = ' '.join(self._text.split()[1:])



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

        message = """Use this bot to look up podcasts from NPR! For a list of available commands, type '/' and follow the prompt. Have fun! """

        return message

    def recent(self):
        """Query the DB for the last ten items and return"""

        return self.query_db("SELECT * from test_table order by episode_date desc limit 10;")

    def list(self):
        """Return a list of all podcast series being tracked"""

        return "\n".join(FEEDS.keys())

    def host(self):
        """Query the DB for podcast series where the host matches the description"""

        return self.query_db("SELECT * from test_table where pod_description like '%{}%' limit 10;".format(self._arg))

    def guest(self):
        """Query the DB for episodes where the guest matches the description"""

        return self.query_db("SELECT * from test_table where episode_description like '%{}%' limit 10;".format(self._arg))

    def last(self):
        """Query the DB for the most recent episode for the given podcast series"""

        return self.query_db("SELECT * from test_table where pod_title like '%{}%' order by episode_date desc limit 1;".format(self._arg))


    def get_db_connector(self, db_file='useraudio.db'):
        """Not needed by all commands, use as needed"""

        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return None


    def query_db(self, sql_cmd):
        """Querry db and return list of PODCAST_TITLE, EPISODE_SUMMARY and URL"""

        db_conn = self.get_db_connector()
        with db_conn:
            db_cur = db_conn.cursor()
            db_cur.execute(sql_cmd)
            rows = db_cur.fetchall()

        formatted_message_list = []
        for row in rows:
            formatted_message_list.append("{}, {}, {}".format(row[0], row[2], row[5]))
            # TODO: modify using HTML Templates

        return formatted_message_list