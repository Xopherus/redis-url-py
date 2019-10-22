from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import int
from future import standard_library
standard_library.install_aliases()

import urllib.parse

def parse(url):
    """Parses a Redis URL."""

    url = urllib.parse.urlparse(url)

    config = {
        'host': url.hostname or 'localhost',
        'port': int(url.port or 6379),
        'password': url.password or None
    }

    # parse options from url
    options = urllib.parse.parse_qs(url.query)

    # if cluster mode is enabled, do not add db to config (unsupported)
    cluster_enabled = options.pop('cluster', ['false'])[0]

    if cluster_enabled == 'false':
        config['db'] = int(url.path[1:] or 0)

    for key, val in options.items():
        config[key] = val[0] if len(val) == 1 else val

        if key == 'skip_full_coverage_check':
            config[key] = True if config[key] == 'true' else False

    return config
