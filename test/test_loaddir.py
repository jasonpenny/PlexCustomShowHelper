"""
Plan:

get directory list

get list of files which don't have corresponding .nfo files

for each file
    parse filename into season, episode, video title
    create xml
    save xml to .nfo file

"""
from plexcustomshowhelper import create_nfo

def test_create_nfo_xml():
    expected = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n' \
            '<episodedetails>\n' \
            '<title>Name of Show</title>\n' \
            '<season>1</season>\n' \
            '<episode>5</episode>\n' \
            '</episodedetails>'

    actual = create_nfo('Name of Show', 1, 5)

    assert actual == expected

def test_parse_filename_attributes():
    pass

def test_filter_files_without_nfo_files():
    pass
