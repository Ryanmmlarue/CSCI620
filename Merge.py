"""
author: Ryan Jiau; rsj7519
"""

import pandas as pd

data1 = pd.read_table(FilePath)
data1.head()

data2 = pd.read_table(FilePath)
data2.head()

data3 = pd.read_table(FilePath)
data3.head()

data4 = pd.read_table(FilePath)
data4.head()

data5 = pd.read_table(FilePath)
data5.head()

concate_data = pd.concat([data1,data2,data3,data4,data5])
concate_data.head()

concate_data.to_csv(OutputFilePath, sep="\t", index=False)
print(concate_data)