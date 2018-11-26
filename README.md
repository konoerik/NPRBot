# NPRBot

## Overview
A Telegram Bot that helps users search and listen to podcasts from NPR

## How to run locally
### Prerequisites
1. Python 3.X + PIP
2. Flask (lightweight web-server) | `pip install flask`
3. Feedparser (for RSS feeds)     | `pip install feedparser`
4. Ngrok (for temporary public URL)  | https://ngrok.com/
5. A Telegram account (search for npr bot)

### Steps
1. Start ngrok at port 5000 (default for flask) | ngrok.exe http 5000
2. Use the HTTPS resulting address as an URL for the bot to send requests to
3. Run app.py as
    ```script
    C:\Workspace\PyCharm\NPRBot>python -u app.py 797980983:AAGlz1dXeRmPzh-gL2n89qBLD6X4S_8Fvks 5000 https://91651a79.ngrok.io/webhook
    # Make sure to replace the URL and ports accordingly
    ```
4. Start chatting with `npr` bot on Telegram
5. At this point it will just return the same message always

## How to deploy online (TODO)
## Examples (TODO)