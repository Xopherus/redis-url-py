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
    options = urlparse.parse_qs(url.query)

    # if cluster mode is enabled, do not add db to config (unsupported)
    cluster_enabled = options.pop('cluster', ['false'])[0]

    if cluster_enabled == 'false':
        config['db'] = int(url.path[1:] or 0)

    for key, val in options.iteritems():
        config[key] = val[0] if len(val) == 1 else val

        if key == 'skip_full_coverage_check':
            config[key] = True if config[key] == 'true' else False

    return config
