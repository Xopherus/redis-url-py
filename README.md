# redis-url-py

This utility allows you
to configure Redis
in your Python applications
using a url.
This library was inspired by
needing a way to seamlessly
switch between
[redis-py][] and
[redis-py-cluster][]
based on env configuration.

[redis-py]: https://github.com/andymccurdy/redis-py
[redis-py-cluster]: https://github.com/Grokzen/redis-py-cluster/

## Usage

Non-Clustered Redis

```
redis_url_py.parse('redis://:password@127.0.0.1:6379/0')

{
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
    'password': 'password'
}
```

Clustered Redis

```
redis_url_py.parse('redis://:password@127.0.0.1:6379?cluster=true')

{
    'host': '127.0.0.1',
    'port': 6379,
    'password': 'password',
}
```

## Options

You may also specify
options in your URL
which can be used
to configure a redis cluster.

- `cluster` {boolean} - set to true if the url refers to a clustered redis

- `skip_full_coverage_check` {boolean} - (used when connecting to ElastiCache instances, see http://redis-py-cluster.readthedocs.io/en/master/upgrading.html#id1)
