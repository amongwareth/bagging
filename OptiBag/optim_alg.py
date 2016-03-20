import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables


logger = logging.getLogger(__name__)


def launch(args, others):
    print('AAAAAAAAA', args)


def parser(parent_parser):
    parser = parent_parser.add_parser('optim_alg', help='data generation command help', aliases=['alg', 'optim', 'o'])
    parser.add_argument('--alg', default=config.__DEFAULT_ALG__, type=str, help='optimization algorithm to be used')
    parser.set_defaults(action=launch)
    return parser
