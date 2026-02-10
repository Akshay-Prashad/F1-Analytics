import os
import re

import pandas as pd

path = os.listdir()
df_list = []
path.pop(0)
path.pop(0)
for i in path:
    print(i)

    df = pd.read_csv(i)

    df["year"] = i.lstrip("Formula1_").rstrip(".csv")
    df_list.append(df)

df = pd.concat(df_list, ignore_index=True)
df.info()
df.to_csv("F1_Dataset.csv", index=False)
df.head()
