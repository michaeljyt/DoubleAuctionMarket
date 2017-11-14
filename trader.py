import random
class SimpleTrader(object):
    """ A class that makes a trader"""

    def __init__(self):
        self.name = ""
        self.limits = (0, 0)
        self.type = ""
        self.values = []
        self.costs = []

    def offer(self, contracts, standing_bid, standing_ask):
        num_contracts = 0  # intialize number of contracts

        if self.type == "buyer":
            # find out how many contracts you have
            for contract in contracts:
                if contract[1] == self.name:  # second position is buyer_id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.values):
                return [] # You can't bid anymore
            cur_value = self.values[num_contracts]  # this is the current value working on

            # TODO Put in bidding or buying strategy
            if standing_bid:
                if cur_value > standing_bid:
                    bid = max(cur_value, standing_bid + 10)  # 10 is an arbitrary increment
                    return ["B", self.name, bid]
                else:
                    return []
            else:
                if cur_value > 0:
                    bid = 1
                    return["B", self.name, bid]
                else:
                    return[]
        else:
            # find out how many contracts you have
            for contract in contracts:
                if contract[2] == self.name:  # third position is seller id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.costs):
                return  [] # You can't ask anymore
            cur_cost = self.costs[num_contracts]  # this is the current value working on

            # TODO Put in asking or selling strategy
            if standing_ask:
                if cur_cost < standing_ask:
                    ask = max(standing_ask - 10, cur_cost)  # 10 is an arbitrary decrement
                    return ["S", self.name, ask]
                else:
                    return []
            else:
                if cur_cost > 0:
                    ask = 999
                    return["B", self.name, ask]

class KaplanTrader(object):
    """Trader based on Kaplan's Sniping Trader, waits in background until certain threshold met then
    places last minute bid/ask to steal trade"""

    def __init__(self):
        self.name = ""
        self.type = ""
        self.values = []
        self.costs = []

    def offer(self, contracts, standing_bid, standing_ask):
        num_contracts = 0  # intialize number of contracts

        if self.type == "buyer":
            # find out how many contracts you have
            for contract in contracts:
                if contract[1] == self.name:  # second position is buyer_id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.values):
                return []  # You can't bid anymore
            cur_value = self.values[num_contracts]  # this is the current value working on

            if standing_bid:
                if standing_ask:
                    if standing_bid/standing_ask >= 0.98 and cur_value > standing_bid:
                        bid = standing_ask - 1
                        return ["B", self.name, bid]
                    else:
                        return []
                else:
                    if cur_value > standing_bid:
                        bid = standing_bid + 1
                        return ["B", self.name, bid]
                    else:
                        return []
            else:
                if cur_value > 0:
                    bid = 1
                    return ["B", self.name, bid]
                else:
                    return []

        else:
            # find out how many contracts you have
            for contract in contracts:
                if contract[2] == self.name:  # third position is seller id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.costs):
                return []  # You can't ask anymore
            cur_cost = self.costs[num_contracts]  # this is the current value working on

            if standing_ask:
                if standing_bid:
                    if standing_bid/standing_ask >= 0.98 and cur_cost < standing_ask:
                        ask = standing_bid + 1  # random number between cost and standing ask
                        return ["S", self.name, ask]
                    else:
                        return []

                else:
                    if cur_cost < 999:
                        ask = standing_ask - 1
                        return ["S", self.name, ask]
                    else:
                        return []
            else:
                if cur_cost > 0:
                    ask = 999
                    return ["S", self.name, ask]
                else:
                    return []


class ZI_Ctrader(object):
    """ A trader that bids and asks based on random amount"""

    def __init__(self):
        self.name = ""
        self.type = ""
        self.values = []
        self.costs = []

    def offer(self, contracts, standing_bid, standing_ask):
        num_contracts = 0  # intialize number of contracts

        if self.type == "buyer":
            # find out how many contracts you have
            for contract in contracts:
                if contract[1] == self.name:  # second position is buyer_id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.values):
                return []  # You can't bid anymore
            cur_value = self.values[num_contracts]  # this is the current value working on

            # TODO Put in bidding or buying strategy
            if standing_bid:
                if cur_value > standing_bid:
                        bid = random.randint(standing_bid + 1, cur_value)  # random number between
                        return ["B", self.name, bid]
                else:
                    return []

            else:
                if cur_value > 0:
                    bid = 1
                    return["B", self.name, bid]
                else:
                    return[]
        else:
            # find out how many contracts you have
            for contract in contracts:
                if contract[2] == self.name:  # third position is seller id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.costs):
                return []  # You can't ask anymore
            cur_cost = self.costs[num_contracts]  # this is the current value working on

            # TODO Put in asking or selling strategy
            if standing_ask:
                if cur_cost < standing_ask:
                        ask = random.randint(cur_cost, standing_ask - 1)  # random number between
                        return ["S", self.name, ask]
                else:
                    return []

            else:
                if cur_cost < 999:
                    ask = 999
                    return["S", self.name, ask]
                else:
                    return[]

class ZI_Utrader(object):
    """ A class always increases bid by 3, decreases ask by 3, does not take cur_value or cur_cost into account
    makes a trader that is subject to Winner's Curse"""

    def __init__(self):
        self.name = ""
        self.type = ""
        self.values = []
        self.costs = []

    def offer(self, contracts, standing_bid, standing_ask):
        num_contracts = 0  # intialize number of contracts

        if self.type == "buyer":
            # find out how many contracts you have
            for contract in contracts:
                if contract[1] == self.name:  # second position is buyer_id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.values):
                return []  # You can't bid anymore
            cur_value = self.values[num_contracts]  # this is the current value working on

            # TODO Put in bidding or buying strategy

            if standing_bid:
                bid = random.randint(standing_bid + 1, 999)  # random number between standing_bid and cur_value
                return ["B", self.name, bid]
            else:
                bid = 1
                return ["B", self.name, bid]
        else:
            # find out how many contracts you have
            for contract in contracts:
                if contract[2] == self.name:  # third position is seller id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.costs):
                return []  # You can't ask anymore
            cur_cost = self.costs[num_contracts]  # this is the current value working on

            # TODO Put in asking or selling strategy

            if standing_ask:
                ask = random.randint(1, standing_ask - 1)  # random number between cost and standing ask
                return ["S", self.name, ask]
            else:
                ask = 999
                return ["S", self.name, ask]

class GDtrader(object):
    """Trader using belief function of order histories to predict prob"""

    def __init__(self):
        self.name = ""
        self.type = ""
        self.values = []
        self.costs = []

    def offer(self, contracts, standing_bid, standing_ask):
        num_contracts = 0  # intialize number of contracts

        if self.type == "buyer":
            # find out how many contracts you have
            for contract in contracts:
                if contract[1] == self.name:  # second position is buyer_id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.values):
                return []  # You can't bid anymore
            cur_value = self.values[num_contracts]  # this is the current value working on

            if standing_bid:
                if standing_ask:
                    if standing_bid/standing_ask >= 0.98 and cur_value > standing_bid:
                        bid = standing_ask - 1
                        return ["B", self.name, bid]
                    else:
                        return []
                else:
                    if cur_value > standing_bid:
                        bid = standing_bid + 1
                        return ["B", self.name, bid]
                    else:
                        return []
            else:
                if cur_value > 0:
                    bid = 1
                    return ["B", self.name, bid]
                else:
                    return []

        else:
            # find out how many contracts you have
            for contract in contracts:
                if contract[2] == self.name:  # third position is seller id
                    num_contracts = num_contracts + 1
            if num_contracts >= len(self.costs):
                return []  # You can't ask anymore
            cur_cost = self.costs[num_contracts]  # this is the current value working on

            if standing_ask:
                if standing_bid:
                    if standing_bid/standing_ask >= 0.98 and cur_cost < standing_ask:
                        ask = standing_bid + 1  # random number between cost and standing ask
                        return ["S", self.name, ask]
                    else:
                        return []

                else:
                    if cur_cost < 999:
                        ask = standing_ask - 1
                        return ["S", self.name, ask]
                    else:
                        return []
            else:
                if cur_cost > 0:
                    ask = 999
                    return ["S", self.name, ask]
                else:
                    return []

if __name__ == "__main__":
    zi = ZeroIntelligenceTrader()