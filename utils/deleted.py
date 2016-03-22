#!/usr/bin/env python

"""
Filters out deleted tweets.
"""
from __future__ import print_function

import json
import fileinput

for line in fileinput.input():
    tweet = json.loads(line)
    if 'created_at' in tweet:
        if tweet['created_at']:
            print(json.dumps(tweet))