#!/usr/bin/env python

import sys

job = sys.argv[1]

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))

if job == 'J003':
    print('Fail')
    sys.exit(1)
