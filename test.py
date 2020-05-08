#!/usr/bin/env python

import os
import sys
import json

job = sys.argv[1]

print('Hello %s on %s' % (job, '.'.join('%s' % v for v in sys.version_info)))
print('Update 1')

print()

for key in sorted(os.environ):
    print('%s=%s' % (key, os.environ[key]))

event_path = os.environ['GITHUB_EVENT_PATH']

with open(event_path, 'r') as event_file:
    event = json.load(event_file)

print()

print(json.dumps(event, indent=4, sort_keys=True))
