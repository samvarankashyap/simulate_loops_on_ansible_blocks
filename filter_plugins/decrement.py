#!/usr/bin/env python


def decrement(output):
    return int(output) -1


class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'decrement': decrement
        }
