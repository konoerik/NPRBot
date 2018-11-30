"""
Use this file to refresh the feeds and update the database
A few ways to use:
    Run as standalone from separate Python invocation
    Invoke from app.py on certain commands (i.e. /refresh)

TODO: implement threading (potential issues with SQlite connector)
"""

import feedparser
import sqlite3
from time import sleep

FEEDS = {
    "Planet Money" :        "https://www.npr.org/templates/rss/podcast.php?id=510289",
    "How I Built This" :    "https://www.npr.org/rss/podcast.php?id=510313",
    "Hidden Brain" :        "https://www.npr.org/rss/podcast.php?id=510308",
    "Up First" :            "https://www.npr.org/rss/podcast.php?id=510318",
    "Wait Don't Tell Me" :  "https://www.npr.org/templates/rss/podcast.php?id=344098539",
    "TED Radio Hour" :      "https://www.npr.org/templates/rss/podcast.php?id=510298",
    "Fresh Air" :           "https://www.npr.org/rss/podcast.php?id=381444908",
    "NPR Politics" :        "https://www.npr.org/rss/podcast.php?id=510310",
    "Tiny Desks" :          "https://www.npr.org/templates/rss/podcast.php?id=510306",
    "The Indicator" :       "https://www.npr.org/rss/podcast.php?id=510325",
    "WAMU" :                "https://www.npr.org/rss/podcast.php?id=510316",
    "Pop Culture Happy Hour" : "https://www.npr.org/rss/podcast.php?id=510282",
    "Only A Game" :         "https://www.npr.org/templates/rss/podcast.php?id=510052",
    "Car Talk" :            "https://www.npr.org/templates/rss/podcast.php?id=510208",
}


def update_local_db(update_freq=15):
    """
    Fetches updates from RSS feed and inserts into database
    :param update_freq: int, use value of 0 when standalone run
    :return: None
    """
    while True:
        conn = sqlite3.connect('useraudio.db')
        cur = conn.cursor()

        for feed in FEEDS.values():
            f = feedparser.parse(feed)
            podcast_title = f['feed']['title']
            podcast_summary = f['feed']['summary']

            for entry in f['entries']:
                episode_title = entry['title']
                episode_summary = entry['summary']
                episode_link = entry['links'][0]['href']
                t = entry['published_parsed'] # time_struct
                episode_date = "{}-{}-{}".format(t.tm_year, t.tm_mon, t.tm_mday)

                try:
                    # slow method, needs improvement
                    cur.execute("INSERT INTO test_table VALUES (?, ?, ?, ?, ?, ?)", (podcast_title, podcast_summary, episode_title, episode_summary, episode_date, episode_link))
                except sqlite3.IntegrityError as e:
                    # print("Entry exists, ignore error <{}>".format(e)) # for debugging
                    pass

        conn.commit()
        if update_freq <= 0:
            break
        else:
            print("Commit completed. Sleeping before next iteration...")
            sleep(update_freq)


if __name__ == '__main__':
    update_local_db(update_freq=0)