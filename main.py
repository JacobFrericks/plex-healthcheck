import requests
import os
import subprocess
from plexapi.myplex import MyPlexAccount

# Get environment variables
USER = os.getenv('PLEX_USER')
PASSWORD = os.environ.get('PLEX_PASSWORD')
SERVERNAME = os.environ.get('PLEX_SERVER_NAME')

account = MyPlexAccount(USER, PASSWORD)

try:
    plex = account.resource(SERVERNAME).connect()
    movies = plex.library.section('Movies')
    print("Plex is up!")
except:
    print("Plex is down! Attempting to restart...")
    print("Killing PLEX...")
    os.system("taskkill /f /im  \"Plex Media Server.exe\" >nul 2>&1")
    print("Starting PLEX...")
    os.chdir("C:\\Program Files (x86)\\Plex\\Plex Media Server\\")
    subprocess.Popen(["Plex Media Server.exe"])
