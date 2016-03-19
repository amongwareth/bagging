#!/usr/bin/env python3

import argparse
import sys

from OptiBag.common import treat_common_args, parser as pcommon, describe
from OptiBag.data_gen import parser as pd
# from OptiBag.optim_alg import parser as po

parser = argparse.ArgumentParser(prog='OPTIBAG', argument_default=argparse.SUPPRESS)
pcommon(parser)
# Sub-parser section
subparsers = parser.add_subparsers(help='sub-command help')
# get data_gen sub command
pd(subparsers)
# get optim_alg sub command
# po(subparsers)

'''
TODO
-----
	+ set up github for this repo
	+ check what argparse.Namespace() man
	+ implement optim_alg parser 
'''
if __name__ == '__main__':
    """ OPTIBAG entry point. """
    # Remove prog name
    rest = sys.argv[1::]
    args = argparse.Namespace()
    common = False
    # Do all chaining sub command
    if not rest:
        describe(args, [])
        exit(0)

    while rest:
        args, nrest = parser.parse_known_args(rest, namespace=args)
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
