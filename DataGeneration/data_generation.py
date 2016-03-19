import logging

import Config.config as config

logger = logging.getLogger(__name__)


class DataGeneration(object):

    def __init__(self, **kwargs_gen):
        super().__init__()
        self.nb_bid = kwargs_gen.get(nb_bids, config.__DEFAULT_NB_BIDS__)
        self.maxp = kwargs_gen.get(max_p, config.__DEFAULT_MAX_P__)
        self.minp = kwargs_gen.get(min_p, config.__DEFAULT_MIN_P__)
        self.maxq = kwargs_gen.get(max_q, config.__DEFAULT_MAX_Q__)
        self.minq = kwargs_gen.get(min_q, config.__DEFAULT_MIN_Q__)
        self.nb_classes = kwargs_gen.get(nb_classes, config.__DEFAULT_NB_CLASSES__)
        self.nb_groups = kwargs_gen.get(nb_groups, config.__DEFAULT_NB_GROUPS__)
        print('bob')

    def run(self):
        pass

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.__dict__)


class OneBid(object):

    def __init__(self, max_q=None, min_q=None, max_p=None, min_p=None):
        self.bidder_class = None
        self.bidder_group = None
        self.bid_p = None
        self.bid_q = None

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.__dict__)
