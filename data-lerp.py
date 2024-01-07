import pandas as pd
import numpy as np

target = 15

def lerp_chunk(chunk_df):
    if len(chunk_df) == target :
        return chunk_df

    linspace = pd.DataFrame(
        index=pd.RangeIndex(target),
        columns=chunk_df.columns
    )

    linspace["time"] = chunk_df["time"].iloc[0]
    linspace["is_exploiting"] = chunk_df["is_exploiting"].iloc[0]

    for col in ["x", "y", "z"]:
        linspace[col] = pd.Series(np.interp(
            np.linspace(0, 1, num=target_rows),
            np.linspace(0, 1, num=len(chunk_df)),
            chunk_df[col]
        ))

    return linspace

df = pd.read_csv("data/data.csv")
df.sort_values(by=["time"], inplace=True)
result_df = df.groupby("time", group_keys=False).apply(lerp_chunk)

result_df.reset_index(drop=True, inplace=True)
result_df.to_csv("data/lerped-data.csv", index=False)