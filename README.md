PlexCustomShowHelper
====================

This tool helps to generate NFO files which allow Plex or XMBC/Kodi to
display custom shows.

Creating a file named tvshow.nfo allows Plex (with the correct setup)
and/or XBMC/Kodi to define a custom tv show. Each video file should then
be named with a season and episode number, like S01E01.file.mp4 and then
there needs to be a matching file named S01E01.file.nfo with a specific
xml format. I use this functionality to keep Youtube videos and organize
them how I want.

Using the tool
--------------

Run the tool and pass a directory as the first argument:
`./plexcustomshowhelper <directory>`

It will find video files which do not have corresponding .nfo files and
create them automatically parsing the filename.

Setup and Development
---------------------
Install the required packages with `pip install -r requirements`

Run the tests with `py.test test`
