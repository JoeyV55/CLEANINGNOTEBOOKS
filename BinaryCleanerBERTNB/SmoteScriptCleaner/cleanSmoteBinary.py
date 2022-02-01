import pandas as pd
import numpy as np

smoteBinary = pd.read_csv("binarySmote.csv")
#print(smoteBinary.head())
print("Num columns: ", len(smoteBinary.columns))
smoteBinary.drop(smoteBinary.iloc[:, 1:2], inplace=True, axis=1)
print(smoteBinary.head())