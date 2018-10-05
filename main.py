#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser

import vending_machine.tools.machine as mc_tool

config = configparser.ConfigParser()
config.read('config.cfg')
PATH = config['DEFAULT']['PATH']
FILENAME = config['DEFAULT']['FILENAME']
INIT_DATA = bool(int(config['DEFAULT']['INIT_DF']))


def main():
    if INIT_DATA is True:
        mc_tool.init_stock()
    while True:
        mc_tool.show_items()
        result_order, order = mc_tool.get_order()
        if result_order is True:
            result_cash, change = mc_tool.get_cash(order)
            if result_cash is True:
                mc_tool.pop_items(order)
                mc_tool.pop_change(change)
            else:
                print("잘못된 주문입니다.")
        else:
            print("잘못된 주문입니다.")


main()
