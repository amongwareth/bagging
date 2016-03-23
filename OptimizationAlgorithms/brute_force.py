import logging
import time
from tqdm import tqdm
from itertools import combinations

import Config.config as config
import Config.variables as variables

logger = logging.getLogger(__name__)


class BruteForce(object):

    def __init__(self):
        self.best_comb = {'profit': 0, 'combination': [], 'quantity': 0}

    def run(self):
        # self._dumb_brute_force()
        start_time = time.time()
        self._dict_tree(0, 0, tuple(), variables.data.bids)
        logger.debug("--- %s seconds ---\n\n" % (time.time() - start_time))

    def _dumb_brute_force(self):
        best_price = None
        best_combination = []
        # generating combinations by all ways: C by 1 from n, C by 2 from n, ...
        for way in tqdm(range(len(variables.data.bids))):
            for comb in combinations(variables.data.bids, way + 1):
                q_tot = sum([bid.bid_q for bid in comb])
                p_tot = sum([bid.bid_p for bid in comb])
                if (best_price is None or best_price < p_tot) and q_tot <= config.__DEFAULT_Q_CAPACITY__:
                    best_price = p_tot
                    best_combination = comb
        variables.result = {'profit': best_price, 'combination': best_combination}
        # return best_price, best_combination

    def __repr__(self):
        ''' Returns the class name and its attributes '''
        return "%s(%r)" % (self.__class__.__name__, self.__dict__)

    def _dict_tree(self, qty, profit, combination, nodes):
        temp_dict = {}
        if nodes:
            for node in nodes:
                nodes_copy = list(nodes)
                nodes_copy.remove(node)
                new_qty = qty + node.bid_q
                if new_qty <= config.__DEFAULT_Q_CAPACITY__:
                    new_profit = profit + node.bid_p
                    new_combination = combination + (node,)
                    temp_dict[node] = {'qty': new_qty, 'profit': new_profit, 'combination': new_combination,
                                       'subtree': self._dict_tree(new_qty, new_profit, new_combination, nodes_copy)}
                    if self.best_comb['profit'] == 0 or self.best_comb['profit'] < new_profit:
                        self.best_comb['profit'] = new_profit
                        self.best_comb['combination'] = new_combination
                        self.best_comb['quantity'] = new_qty
                        variables.result = self.best_comb
                        logger.debug('New best combination : %s', self.best_comb)
                else:
                    temp_dict[node] = {'qty': new_qty}
            return temp_dict
        else:
            return {}
