import requests
import os
from plexapi.myplex import MyPlexAccount

# Get environment variables
USER = os.getenv('PLEX_USER')
PASSWORD = os.environ.get('PLEX_PASSWORD')
SERVERNAME = os.environ.get('PLEX_SERVER_NAME')

account = MyPlexAccount(USER, PASSWORD)
plex = account.resource(SERVERNAME).connect()

movies = plex.library.section('Movies')
if not movies.search(unwatched=True):
    # Plex is not working...
    print("RESTARTING PLEX...")
    os.system("taskkill /f /im  Plex Media Server.exe")
    os.system('"C:\\Program Files (x86)\\Plex\\Plex Media Server\\Plex Media Server.exe"')
else:
    print("Plex is up!")
