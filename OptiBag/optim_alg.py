import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables


logger = logging.getLogger(__name__)


def launch(args, others):
    logger.debug('optim_alg parser args : %s', args)
    variables.algo = variables.loader.get_instance(config.__ALGS_PATHS__[args.algo])
    variables.algo.run()
    logger.debug('The result is %s', variables.result)


def parser(parent_parser):
    parser = parent_parser.add_parser('optim_alg', help='data generation command help', aliases=['alg', 'optim', 'o'])
    parser.add_argument('--algo', default=config.__DEFAULT_ALGO__, type=str, help='optimization algorithm to be used')
    parser.set_defaults(action=launch)
    return parser
