# Plex Healthcheck
This script will verify that the plex server is up and running. If it is not, it will kill the app and attempt to restart it.

A few environment variables are necessary before running the script:

`PLEX_USER`: Your plex username
`PLEX_PASSWORD`: Your plex password
`PLEX_SERVER_NAME`: Your plex server name

To run it, simply install the requirements, then run `python main.py`

This script needs to be on the plex server itself. If you want to run it on onther machines, they at least need to be on the same network.

You can also set this up to run every x minutes. For windows, when running every 5 minutes, simply run:
`schtasks /create /tn PlexHealthCheck /tr "cmd /c python <PATH_TO_CODE>\main.py > %HOMEPATH%\Desktop\health.log 2>&1" /sc MINUTE /mo 5`
