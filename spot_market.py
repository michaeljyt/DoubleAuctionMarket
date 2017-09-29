import build_environment.py as b
import double_auction_institution as ins
import tournament as trna
import trader as t

# input - output and display options
input_path = "C:\\Users\\kevin\\Desktop\\spot_market_working\\projects\\"  # TODO change file path
#input_path = "C:\\Users\\Admin\\Notebooks\\envs\\"
input_file = "env_0616_4x4w3_sym"  # TODO change file to TEST
t_name = "REU 2017"
display = True

# market/auction parameters
num_buyers = 4  # number of buyers
num_sellers = 4  # number of sellers
limits = (999, 0)  # ceiling and floor for bidding
num_market_periods = 100  # number of periods auction runs

# Put Trader Class Names Here - note traders strategy is named trader class name
zi = "ZeroIntelligenceTrader"
si = "SimpleTrader"
trader_names = [zi, si, zi, si, zi, si, zi, si]  # Order of trader strategies in generic trader array

# tournament parameters
num_trials = 1  # number of times market is run

# create objects to run tournament
mkt = b.BuildMarketEnv(t_name, 4, 4)  # instantiate market object
mkt.prepare_market(input_path, input_file) # set and show market parameters
da = ins.Auction('da', limits[0], limits[1]) # instantiate auction
trn = trna.Tournament(t_name, num_market_periods, da)  # instatiate tournament
trader_info = trn.prepare_traders(trader_names, mkt, limits) # instantiate traders
trn.sim(display, num_trials, trader_info)
del mkt
