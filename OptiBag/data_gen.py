import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables
from DataGeneration.data_generation import DataGeneration


logger = logging.getLogger(__name__)


def launch(args, others):
    kwargs_gen = {'nb_bids': args.nb_bids, 'max_q': args.max_q,
                  'min_q': args.min_q, 'max_p': args.max_p, 'min_p': args.min_p}
    kwargs_gen.update({'nb_classes': args.nb_classes, 'nb_groups': args.nb_groups})
    generator = DataGeneration(**kwargs_gen)
    variables.data = generator.run()
    print('generator', generator, '\n')
    print(variables.data.classes)


def parser(parent_parser):
    parser = parent_parser.add_parser('data_gen', help='data generation command help', aliases=['dg'])
    parser.add_argument('--nb_bids', default=config.__DEFAULT_NB_BIDS__, type=int, help='number of bids to generate')
    parser.add_argument('--max_q', default=config.__DEFAULT_MAX_Q__, type=float, help='maximum q for a bid')
    parser.add_argument('--min_q', default=config.__DEFAULT_MIN_Q__, type=float, help='minimum q for a bid')
    parser.add_argument('--max_p', default=config.__DEFAULT_MAX_P__, type=float, help='maximum p for a bid')
    parser.add_argument('--min_p', default=config.__DEFAULT_MIN_P__, type=float, help='minimum p for a bid')
    parser.add_argument('--nb_classes', default=config.__DEFAULT_NB_CLASSES__,
                        type=int, help='number of exclusive classes')
    parser.add_argument('--nb_groups', default=config.__DEFAULT_NB_GROUPS__,
                        type=int, help='number of groups per class')
    parser.set_defaults(action=launch)
    return parser
