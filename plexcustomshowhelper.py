def create_nfo(title, season, episode):
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n' \
            '<episodedetails>\n' \
            '<title>%s</title>\n' \
            '<season>%s</season>\n' \
            '<episode>%s</episode>\n' \
            '</episodedetails>' % (title, season, episode)
