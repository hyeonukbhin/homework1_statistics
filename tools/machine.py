#!/usr/bin/python3

import configparser

import pandas as pd
import vending_machine.tools.dataframe as df_tool

config = configparser.ConfigParser()
config.read('config.cfg')
FILEPATH = config['DEFAULT']['FILEPATH']


def init_stock():
    index = ["Pepchi", "KokeKola", "Starblues Caffe Latte", "Bottle Water"]
    # columns = ['price', 'stock']
    raw_data = {"price": [500, 550, 1000, 300],
                "stock": [10, 10, 25, 20],
                "available": ["O", "O", "O", "O"]}

    df = pd.DataFrame(raw_data, index=index)
    df_tool.save_df(df, FILEPATH)


def start_section():
    show_items()
    result_order, order = get_order()
    result_cash, change = get_cash()
    if (result_order == True) and (result_cash == True):
        pop_items(order)
        pop_change(change)
    else:
        print("잘못된 주문입니다.")


def get_order():
    order = input("음료를 입력해 주세요. : ")
    if check_index(order) is True:
        avail = df_tool.check_df(order, "available")
        if avail == "O":
            result = True
        else:  # result is "X"
            result = False
            print("잘못된 주문입니다.")
    else:
        result = False
    return result, order


def check_index(key=None):
    index = key
    index_list = df_tool.get_indexlist()
    if index is None:
        print(index_list)
        result = False
    else:
        result = index in index_list
    return result


def get_cash(order):
    cash = int(input("돈을 넣어 주세요. : "))
    price = df_tool.check_df(order, "price")
    change = calculate_change(cash, price)
    if change is not None:
        result = True
    else:  # result is "X"
        result = False
        print("잘못된 금액입니다.")
    return result, change


def show_items():
    print("=============================================")
    df = df_tool.read_df(FILEPATH)
    print(df)
    print("=============================================")


def calculate_change(cash, price):
    # Cash is input
    if cash >= price:
        result = cash - price
    else:
        result = None
        print("돈이 부족 합니다.")
    return result


def pop_items(order):
    print("{} 상품이 나왔습니다.".format(order))
    sale_item(order)


def pop_change(change):
    print("잔돈 {}원이 나왔습니다.".format(change))


def sale_item(index, df=None):
    if df is None:
        df = df_tool.read_df(FILEPATH)
    df = df.copy()
    columns = "stock"
    # pre_value = df[columns][index]
    pre_value = df.loc[index, columns]
    # print("ttttttttttt")
    # print(tools)
    post_value = pre_value - 1
    df.loc[index, columns] = post_value
    if post_value == 0:
        df.loc[index, "available"] = "X"
        # df["available"][index] = "X"

    df_tool.save_df(df, FILEPATH)
    return df
