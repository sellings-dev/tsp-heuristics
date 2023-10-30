import pandas as pd

def readData(filepath):
    df = pd.read_csv(
        filepath_or_buffer=filepath,
        header=None,
        skiprows=6,
        skip_blank_lines=True,
        delim_whitespace=True,
        usecols=[1, 2],
        names=("n", "x", "y"),
    )
    df.dropna(inplace=True)

    return df.to_numpy()