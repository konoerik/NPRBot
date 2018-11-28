import feedparser
import sqlite3
from sqlite3 import Error
# TODO
# Create SQLite database
# Update feeds from URL, parse and store to database
# Run all the above as thread so it can be initialized from <app.py>
#
# SCOPE (can be changed)
#     To create an RssFeed instance for each RSS feed, and have them run in their own thread
#     That way, even if some URL is unresponsive, the others will not be affected



"""
def create_connection(db_file):
    #create a database connection to a SQLite database 
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)


created_db=create_connection("useraudio.db")

"""


FEEDS = {
    "Planet Money" : "https://www.npr.org/templates/rss/podcast.php?id=510289",
    "How I Built This" : "https://www.npr.org/rss/podcast.php?id=510313",
    "Hidden Brain" : "https://www.npr.org/rss/podcast.php?id=510308",
}

class RssFeed(object):
    """
    Class that represents an NPR RSS Feed
    """

    def __init__(self, feed_url):
        self._url = feed_url        # defaults to FEEDS but can be overwritten

    def run_as_thread(self, update_freq=15):
        '''
        Update feeds and database every <update_freq> minutes, default=15
        :return: thread handle
        '''
        pass

def run_everything():
    '''
    Use to initialize all threads
    :return: list of threads handles
    '''
    pass
