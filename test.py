#!/usr/bin/env python

import sys
import time

job = sys.argv[1]

time.sleep(20)

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))
