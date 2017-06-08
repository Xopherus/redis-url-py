try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


def parse(url):
    """Parses a Redis URL."""

    url = urlparse.urlparse(url)

    config = {
        'host': url.hostname or 'localhost',
        'port': int(url.port or 6379),
        'password': url.password or None
    }

    # parse options from url
    for option in url.query.split('&'):
        option = option.split('=')
        key, val = option[0].lower(), option[1]

        if key == 'skip_full_coverage_check':
            config[key] = True if val.lower() == 'true' else False
        else:
            config[key] = val

    if 'cluster' not in options:
        config['db'] = int(url.path[1:] or 0)

    return config
