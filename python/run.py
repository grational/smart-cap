#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TextFilter import SmartCap as sc

import sys

if len(sys.argv) < 2:
    print 'usage: ' + sys.argv[0] + ' <one [or more words]>'
    sys.exit(1)

input_string = " ".join(sys.argv[1:])
print sc.smart_cap(input_string)
