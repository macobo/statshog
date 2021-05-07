from __future__ import absolute_import
from django.conf import settings  # type: ignore

from statshog import defaults
from statshog.client import StatsClient


statsd: StatsClient = None # type: ignore

if statsd is None:
    host = getattr(settings, "STATSD_HOST", defaults.HOST)
    port = getattr(settings, "STATSD_PORT", defaults.PORT)
    prefix = getattr(settings, "STATSD_PREFIX", defaults.PREFIX)
    maxudpsize = getattr(settings, "STATSD_MAXUDPSIZE", defaults.MAXUDPSIZE)
    ipv6 = getattr(settings, "STATSD_IPV6", defaults.IPV6)
    telegraf = getattr(settings, "STATSD_TELEGRAF", defaults.TELEGRAF)
    separator = getattr(settings, "STATSD_SEPARATOR", defaults.SEPARATOR)
    statsd = StatsClient(
        host=host, port=port, prefix=prefix, maxudpsize=maxudpsize, ipv6=ipv6, telegraf=telegraf, separator=separator
    )
