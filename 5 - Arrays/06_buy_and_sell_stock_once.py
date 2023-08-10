#!/usr/bin/python3


# PROBLEM: Take an array denoting the daily stock price; return max profit
#

def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for p in prices:
        max_profit_sell_today = p - min_price_so_far
        max_profit            = max(max_profit, max_profit_sell_today)
        min_price_so_far      = min(min_price_so_far, p)
    return max_profit


'''
Variant: Write a program that takes an array of integers and finds the length of a longest subarray
all of whose entries are equal.
'''
