#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TextFilter import SmartCap as sc

import sys
args = sys.argv[1:]

def usage():
    print(('usage: ' + sys.argv[0] + ' default <one [or more words]>'))
    print(('       ' + sys.argv[0] + ' address <one [or more words]>'))
    print(('       ' + sys.argv[0] + ' tolerance <threshold> <one [or more words]>'))
    sys.exit(1)

if not len(args) > 0:
    usage()

if args[0] == 'default':
    input_string = " ".join(args[1:])
    print((sc.smart_cap(input_string)))
elif args[0] == 'address':
    input_string = " ".join(args[1:])
    print((sc.address_smart_cap(input_string)))
elif args[0] == 'tolerance':
    threshold = args[1]
    input_string = " ".join(args[2:])
    print((sc.conditional_smart_cap(input_string,threshold)))
else:
    usage()
