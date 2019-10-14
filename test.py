#!/usr/bin/env python

import sys

job = sys.argv[1]

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))

if job == 'J001':
    print('Fail %s' % job)
    sys.exit(1)
