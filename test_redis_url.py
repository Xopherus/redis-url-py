import redis_url
import unittest


class RedisUrlTestSuite(unittest.TestCase):

    def test_redis_parse_localhost(self):
        self.assertEqual(
            redis_url.parse('redis://localhost:6379/0?cluster=false'),
            {
                'host': 'localhost',
                'port': 6379,
                'db': 0,
                'password': None
            }
        )

    def test_redis_parse_remote(self):
        self.assertEqual(
            redis_url.parse('redis://:138913@ec2-192-168-1-1.compute-1.amazon.aws.com:30001?cluster=false'),
            {
                'host': 'ec2-192-168-1-1.compute-1.amazon.aws.com',
                'port': 30001,
                'db': 0,
                'password': '138913'
            }
        )

    def test_redis_parse_cluster_localhost(self):
        self.assertEqual(
            redis_url.parse('redis://localhost:6379?cluster=true'),
            {
                'host': 'localhost',
                'port': 6379,
                'password': None
            }
        )

    def test_redis_parse_cluster_skip_full_coverage_check(self):
        self.assertEqual(
            redis_url.parse('redis://localhost:6379?cluster=true&skip_full_coverage_check=true'),
            {
                'host': 'localhost',
                'port': 6379,
                'password': None,
                'skip_full_coverage_check': True,
            }
        )


if __name__ == '__main__':
    unittest.main()
