"""
author: Ryan Jiau; rsj7519
"""

import pandas as pd

data1 = pd.read_table(FilePath)
data1.head()
tables.append(data1)

data2 = pd.read_table(FilePath)
data2.head()
tables.append(data2)

data3 = pd.read_table(FilePath)
data3.head()
tables.append(data3)

data4 = pd.read_table(FilePath)
data4.head()
tables.append(data4)

data5 = pd.read_table(FilePath)
data5.head()
tables.append(data5)

for x in tables:
    concate_data = pd.concat(tables)
    concate_data.head()

concate_data.to_csv(OutputFilePath, sep="\t", index=False)
print(concate_data)
