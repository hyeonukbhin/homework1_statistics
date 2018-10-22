#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

excel_file = "data.xlsx"

df_all = pd.read_excel(excel_file, index_col=0)

df_population = df_all["데이터"].reset_index(drop=True)

# set parameter
# N = 10
Ns = [10, 20, 30, 40, 50]


def cal_mean_std(df):
    mean = df.mean()
    std = df.std()
    return mean, std


def add_df(index, columns, value, df=None):
    df.loc[index, columns] = value
    return df


def draw_box_plot(df, x=[], y=[], title="E vs Subfeature", with_swarmplot=False):
    fig = plt.figure(figsize=(30, 15))
    fig.suptitle(title, fontsize=20)

    for idx, val in enumerate(x):
        ax = fig.add_subplot("{}{}{}".format(len(x), 1, idx + 1))
        sns.boxplot(x=df[val], y=df[y[idx]], ax=ax)
        ax.grid(color='k', linestyle='-', linewidth=0.5)
        if with_swarmplot is True:
            sns.swarmplot(x=df[val], y=df[y[idx]], color="0.9", ax=ax)


df_mean_std = pd.DataFrame(dtype=float)
writer = pd.ExcelWriter("result.xlsx", engine='openpyxl')

for N in Ns:
    df_samples = pd.DataFrame(dtype=float)
    coll_names = ["sample_1", "sample_2", "sample_3", "sample_4", "sample_5", "sample_6", "sample_7", "sample_8",
                  "sample_9", "sample_10"]

    for coll_name in coll_names:
        df_samples[coll_name] = df_population.sample(N).reset_index(drop=True)

    df_sample_mean_std = pd.DataFrame(dtype=float)
    for coll_name in coll_names:
        mean, std = cal_mean_std(df_samples[coll_name])
        df_sample_mean_std = add_df(coll_name, "mean", mean, df_sample_mean_std)
        df_sample_mean_std = add_df(coll_name, "std", std, df_sample_mean_std)

    mean, _ = cal_mean_std(df_sample_mean_std["mean"])
    _, std = cal_mean_std(df_sample_mean_std["std"])
    df_mean_std = add_df(N, "mean", mean, df_mean_std)
    df_mean_std = add_df(N, "std", std, df_mean_std)

    print("========================================")
    print("sample raw data, N = {}".format(N))
    print(df_samples)
    print("========================================")
    print("sample's mean, std, N = {}".format(N))
    print(df_sample_mean_std)

    df_samples.to_excel(writer, index=False, sheet_name="sample_{}".format(N))
    df_sample_mean_std.to_excel(writer, startcol=df_samples.shape[1] + 2, index=False, sheet_name="sample_{}".format(N))

print("========================================")
print("mean, std of sample's means According to Ns".format(N))
print(df_mean_std)
df_mean_std.to_excel(writer, index=False, sheet_name="total")
writer.save()

title = "E vs Subfeature",
fig = plt.figure()
plt.plot(df_mean_std.index, df_mean_std["mean"], label="mean")
plt.plot(df_mean_std.index, df_mean_std["std"], label="std")
plt.legend()
plt.show()
