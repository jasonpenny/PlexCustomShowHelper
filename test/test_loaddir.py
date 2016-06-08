"""
Plan:

get directory list

get list of files which don't have corresponding .nfo files

for each file
    parse filename into season, episode, video title
    create xml
    save xml to .nfo file

"""
from plexcustomshowhelper import create_nfo, parse_filename_attributes, \
        filter_video_files_without_nfo_files

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
    tests = (
        ('S01E01.title.mp4', ('title', 1, 1)),
        ('S3E12.show with space.mp4', ('show with space', 3, 12)),
        ('title first.S05E22.mp4', ('title first', 5, 22)),
    )
    for filename, attrs in tests:
        assert parse_filename_attributes(filename) == attrs

def test_filter_files_without_nfo_files():
    expected = []
    input_files = []
    assert filter_video_files_without_nfo_files(input_files) == expected

    expected = ['a.mp4', 'b.mp4', 'c.mp4']
    input_files = ['a.mp4', 'b.mp4', 'c.mp4']
    assert filter_video_files_without_nfo_files(input_files) == expected

    expected = ['a.mp4', 'c.mp4']
    input_files = ['a.mp4', 'b.mp4', 'c.mp4', 'b.nfo', 'd.mp4', 'd.nfo', 'e.nfo']
    assert filter_video_files_without_nfo_files(input_files) == expected

    # ignore jpg and gif image files
    expected = ['a.mp4', 'b.mp4', 'c.mp4']
    input_files = ['a.mp4', 'b.mp4', 'c.mp4', 'ignore1.jpg', 'ignore2.gif']
    assert filter_video_files_without_nfo_files(input_files) == expected
