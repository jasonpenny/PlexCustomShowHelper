import re

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
