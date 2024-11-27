import pandas as pd

def readfile(filename):
    data = pd.read_csv(filename)
    return data