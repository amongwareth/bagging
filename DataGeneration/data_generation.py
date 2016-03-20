import logging
import numpy as np

import Config.config as config

logger = logging.getLogger(__name__)


class DataGeneration(object):
    ''' General class to generate random bids in order to test the bagging algorithms '''

    def __init__(self, **kwargs_gen):
        ''' Initialize the attributes with default values defined in the Config.config file '''
        super().__init__()
        self.nb_bids = kwargs_gen.get('nb_bids', config.__DEFAULT_NB_BIDS__)
        self.maxp = kwargs_gen.get('max_p', config.__DEFAULT_MAX_P__)
        self.minp = kwargs_gen.get('min_p', config.__DEFAULT_MIN_P__)
        self.maxq = kwargs_gen.get('max_q', config.__DEFAULT_MAX_Q__)
        self.minq = kwargs_gen.get('min_q', config.__DEFAULT_MIN_Q__)
        self.nb_classes = kwargs_gen.get('nb_classes', config.__DEFAULT_NB_CLASSES__)
        self.nb_groups = kwargs_gen.get('nb_groups', config.__DEFAULT_NB_GROUPS__)

    def run(self):
        ''' Method that generates random bids, given the attributes.'''
        classes = np.floor(np.random.random_sample(self.nb_bids) * self.nb_classes)
        groups = np.floor(np.random.random_sample(self.nb_bids) * self.nb_groups)
        bids_q = np.round(np.random.random_sample(self.nb_bids) * (self.maxq - self.minq) + self.minq)
        bids_p = np.random.random_sample(self.nb_bids) * (self.maxp - self.minp) + self.minp
        self.data = [OneBid(oneclass, group, bid_p, bid_q)
                     for (oneclass, group, bid_p, bid_q) in zip(classes, groups, bids_p, bids_q)]
        return self

    @property
    def classes(self):
        ''' Method that orders the random bids by bid class and bid group'''
        ret = {i: {j: [] for j in range(self.nb_groups)} for i in range(self.nb_classes)}
        for bid in self.data:
            ret[bid.bidder_class][bid.bidder_group].append(bid)
        return ret

    def __repr__(self):
        ''' Returns the class name and its attributes'''
        return "%s(%r)" % (self.__class__.__name__, self.__dict__)


class OneBid(object):
    ''' Bid class. '''

    def __init__(self, oneclass, group, bid_p, bid_q):
        '''
        Initialize one bid with four attributes :
            + bidder class, bidder group : if a bid from class A and group B is accepted then any bidder from class A
            but other groups is to be rejected from the auction
            + bid_p : price bidded
            + bid_q : quantity bidded
        '''
        self.bidder_class = oneclass
        self.bidder_group = group
        self.bid_p = bid_p
        self.bid_q = bid_q

    def __repr__(self):
        ''' Returns the class name and its attributes '''
        return "%s(%r)" % (self.__class__.__name__, self.__dict__)
