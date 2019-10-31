#!/usr/bin/env python

import os
import sys

job = sys.argv[1]

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))
print('Update 1')
print('\n'.join('%s=%s' % (key, value) for key, value in os.environ.items()))
