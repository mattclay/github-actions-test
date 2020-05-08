#!/usr/bin/env python

import os
import sys

job = sys.argv[1]

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))
print('Update 1')

print()

for key in sorted(os.environ):
    print('%s=%s' % (key, os.environ[key]))
