#!/usr/bin/env python3

import argparse
import sys
import logging

from OptiBag.common import treat_common_args, parser as pcommon, describe
from OptiBag.data_gen import parser as pd
from OptiBag.optim_alg import parser as po

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(prog='OPTIBAG', argument_default=argparse.SUPPRESS)
pcommon(parser)
# Sub-parser section
subparsers = parser.add_subparsers(help='sub-command help')
# get data_gen sub command
pd(subparsers)
# get optim_alg sub command
po(subparsers)

'''
TODO
-----
'''
if __name__ == '__main__':
    ''' OPTIBAG entry point. '''
    rest = sys.argv[1::]
    common = False
    describe([])
    while rest:
        logger.debug('Successive command line arguments during parsing : %s', rest)
        args, nrest = parser.parse_known_args(rest)
        if common and nrest == rest:
            break
        if not common:
            treat_common_args(args)
            common = True
        if rest and rest[0] == '--':
            # end of parsing, append rest to action
            args.action(args, rest[1::])
            break
        else:
            args.action(args, [])
        rest = nrest
    exit(0)
