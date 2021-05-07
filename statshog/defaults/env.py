from __future__ import absolute_import
import os

from statshog import defaults
from statshog.client import StatsClient


statsd: StatsClient = None # type: ignore

if statsd is None:
    host = os.getenv("STATSD_HOST", defaults.HOST)
    port = int(os.getenv("STATSD_PORT", defaults.PORT))
    prefix = os.getenv("STATSD_PREFIX", defaults.PREFIX)
    maxudpsize = int(os.getenv("STATSD_MAXUDPSIZE", defaults.MAXUDPSIZE))
    ipv6 = bool(int(os.getenv("STATSD_IPV6", defaults.IPV6)))
    telegraf = bool(int(os.getenv("STATSD_TELEGRAF", defaults.TELEGRAF)))
    separator = os.getenv("STATSD_SEPARATOR", defaults.SEPARATOR)
    statsd = StatsClient(
        host=host, port=port, prefix=prefix, maxudpsize=maxudpsize, ipv6=ipv6, telegraf=telegraf, separator=separator
    )
