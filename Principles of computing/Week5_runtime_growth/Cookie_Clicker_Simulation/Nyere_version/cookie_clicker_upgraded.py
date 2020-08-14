"""
Cookie Clicker Simulator
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import matplotlib.pyplot as plt

import poc_clicker_provided as provided
import math

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies_produced = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
                        #(time, item, cost of item, total cookies)
        self._purchases = {}

    def __str__(self):
        """
        Return human readable state
        """
        text = "\n"
        text += "Total cookies: " + str(self._total_cookies_produced) + "\n"
        text += "Current cookies: " + str(self._current_cookies) + "\n"
        text += "CPS: " + str(self._current_cps) + "\n"
        text += "Time: " + str(self._current_time) + "\n"
        #for item, number in self._purchases.items():
        #   text += item + "s: " + str(number) + ". "
        #text += "\n"
        return text

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        copy = list(self._history)
        return copy

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            return math.ceil((cookies - self._current_cookies)/self._current_cps)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            produced_while_waiting = time * self._current_cps
            self._current_time += time
            self._current_cookies += produced_while_waiting
            self._total_cookies_produced += produced_while_waiting


    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, cost, self._total_cookies_produced))
            self._purchases[item_name] = self._purchases.get(item_name, 0) + 1

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    current_build_info = build_info.clone()
    clicker_state = ClickerState()

    while clicker_state.get_time() <= duration:

        current_cookies = clicker_state.get_cookies()
        current_cps = clicker_state.get_cps()
        history = clicker_state.get_history()
        time_left = duration - clicker_state.get_time()

        next_item = strategy(current_cookies, current_cps, history, time_left, current_build_info)

        if next_item == None:
            clicker_state.wait(time_left)
            break

        else:
            item_price = current_build_info.get_cost(next_item)
            time_to_wait = clicker_state.time_until(item_price)
            if time_to_wait > time_left:
                clicker_state.wait(time_left)
                break
            else:
                clicker_state.wait(time_to_wait)
                add_cps = current_build_info.get_cps(next_item)
                clicker_state.buy_item(next_item, item_price, add_cps)
                current_build_info.update_item(next_item)
    return clicker_state

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cookie_potential_at_current_cps = cookies + time_left * cps
    items = build_info.build_items()
    cheapest_item = None
    cheapest_price = float('inf')
    for item in items:
        item_price = build_info.get_cost(item)
        if cookie_potential_at_current_cps >= item_price < cheapest_price:
            cheapest_item = item
            cheapest_price = item_price
    return cheapest_item


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    cookie_potential_at_current_cps = cookies + time_left * cps
    items = build_info.build_items()
    most_expensive_affordable_item = None
    highest_affordable_price = None
    for item in items:
        item_price = build_info.get_cost(item)
        if highest_affordable_price < item_price <= cookie_potential_at_current_cps:
            most_expensive_affordable_item = item
            highest_affordable_price = item_price
    return most_expensive_affordable_item

def strategy_cps_pr_cookie(cookies, cps, history, time_left, build_info):
    """
    Always buy the item you can afford with the highest cps/cookie_prize ratio
    """
    cookie_potential_at_current_cps = cookies + time_left * cps
    items = build_info.build_items()

    best_buy = None
    best_cps_pr_cookie = None

    for item in items:
        item_price = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        item_cps_pr_cookie = item_cps/item_price

        possible = item_price <= cookie_potential_at_current_cps
        best_ratio = item_cps_pr_cookie > best_cps_pr_cookie

        if possible and best_ratio:
            best_buy = item
            best_cps_pr_cookie = item_cps_pr_cookie
    return best_buy

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    Chooses best cpu/cost unless to long waiting time. Some fine tuning would make it
    better, but not much.
    """
    cookie_potential_at_current_cps = cookies + time_left * cps
    items = build_info.build_items()

    best_ratio_buy = None
    price = 0
    best_cps_pr_cookie = None
    cheapest_item = strategy_cheap(cookies, cps, history, time_left, build_info)

    for item in items:
        item_price = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        item_cps_pr_cookie = item_cps/item_price

        possible = item_price <= cookie_potential_at_current_cps
        best_ratio = item_cps_pr_cookie > best_cps_pr_cookie

        if possible and best_ratio:
            best_ratio_buy = item
            best_cps_pr_cookie = item_cps_pr_cookie
            price = item_price

    if price/cps > 1000000000.0:
        return cheapest_item
    else:
        return best_ratio_buy

def run_strategies(strategies, print_history = True, plot = True):
    """
    Run all simulations for the given
    """

    for strategy_name, info in strategies.items():
        time, strategy = info
        state = simulate_clicker(provided.BuildInfo(), time, strategy)
        print strategy_name, ":", state
        if plot:
            history = state.get_history()
            time = [item[0] for item in history]
            total_cookies = [item[3] for item in history]
            plt.plot(time, total_cookies, label = strategy_name)
            #plt.plot(time, total_cookies, 'ro')

    if plot:
        plt.xlabel('time')
        plt.ylabel('total production')
        plt.legend()
        plt.title("Strategy overview")
        plt.show()

def run():
    """
    Run the simulator with all mentioned strategies.
    Plots all strategies if wanted.
    """
    time = SIM_TIME
    #time = 1000

    plot_all = True

    strategies = {
                   "Cheap": (time, strategy_cheap),
                  "Expensive": (time, strategy_expensive),
                  "CPS pr cookie": (time, strategy_cps_pr_cookie),
                  "Best": (time, strategy_best),
                  }
    run_strategies(strategies, plot_all)
run()
