#!/usr/bin/env python3
import sys

'''A module for demo exceptions'''


def convert(s):
    '''Convert to an INT'''
    try:
        # x = int(s)
        # print("conversion succeeded, converted {} ".format(x))
        # one way
        return int(s)
    except (ValueError, TypeError) as e:
        # print("confiversion failed for {}".format(x))
        print("conversion error: {}".format(str(e)), file=sys.stderr)
        return -1
