#!/usr/bin/env python
import os
import re
import sys

def create_nfo(title, season, episode):
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n' \
            '<episodedetails>\n' \
            '<title>%s</title>\n' \
            '<season>%s</season>\n' \
            '<episode>%s</episode>\n' \
            '</episodedetails>' % (title, season, episode)

_season_episode_re = re.compile(r'S(\d+)E(\d+)')
def parse_filename_attributes(filename):
    sections = filename.split('.')

    title = sections[1]
    m = _season_episode_re.match(sections[0])
    if m is None:
        title = sections[0]
        m = _season_episode_re.match(sections[1])

    season, episode = m.group(1), m.group(2)

    return title, int(season), int(episode)

def filter_video_files_without_nfo_files(input_files):
    nfo_and_img_files = [f[:-4] for f in input_files
                         if f.endswith('.nfo') or
                         f.endswith('.jpg') or
                         f.endswith('.gif')]
    return [f for f in input_files
            if f[:-4] not in nfo_and_img_files]

def run(directory):
    file_list = [f for f in os.listdir(directory)
                 if not f.startswith('.')]
    files_to_process = filter_video_files_without_nfo_files(file_list)
    for filename in files_to_process:
        title, season, episode = parse_filename_attributes(filename)

        xml_content = create_nfo(title, season, episode)

        nfo_filename = os.path.join(directory, filename[:-4] + '.nfo')
        with open(nfo_filename, 'w') as f:
            f.write(xml_content)

if __name__ == '__main__':
    if sys.argv[1:]:
        run(sys.argv[1])
    else:
        print 'Usage: %s <directory>' % sys.argv[0]
